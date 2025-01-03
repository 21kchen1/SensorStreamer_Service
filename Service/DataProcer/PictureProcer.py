import logging
import os
import threading
import cv2
from Model.Data.TypeData import TypeData
from Resource.String.ServiceString import DataProcerString
from Service.DataProcer.ListenProcer import ListenProcer
from Component.Sound.Sound import Sound
from Component.Time.TimeLine import TimeLine

"""
    Picture 数据处理
    @author: chen
"""
class PictureProcer(ListenProcer):
    WIN_NAME = DataProcerString.WIN_NAME_PICTURE
    CAP_WIDTH = 2560
    CAP_HEIGHT = 1440
    CAP_NUM = 3

    """
        @TypeData: 数据构造函数
        @bufRowSize: 缓冲区行数
    """
    def __init__(self, TypeData, bufRowSize= 500) -> None:
        super().__init__(TypeData, bufRowSize)

    """
        父函数拓展，创建图片存储文件夹，并做对应的校验
    """
    def create(self, storagePath: str, dataCode: str) -> bool:
        if not super().create(storagePath, dataCode):
            return False

        # 开启摄像机线程
        threading.Thread(target= self._getPicture).start()
        return True

    """
        打开摄像头并监听按键，并保存图片
    """
    def _getPicture(self) -> bool:
        if not self.running:
            return False

        try:
            # 先获取电脑的摄像头
            cap = None
            # 打开最新的摄像头
            for i in range(PictureProcer.CAP_NUM - 1, -1, -1):
                nextCap = cv2.VideoCapture(i, cv2.CAP_DSHOW if os.name == "nt" else cv2.CAP_ANY)
                if not nextCap.isOpened():
                    nextCap.release()
                    continue
                # 设置分辨率
                nextCap.set(cv2.CAP_PROP_FRAME_WIDTH, PictureProcer.CAP_WIDTH)
                nextCap.set(cv2.CAP_PROP_FRAME_HEIGHT, PictureProcer.CAP_HEIGHT)
                # 如果是可以使用的摄像头
                if cap == None:
                    cap = nextCap
                    continue
                elif cap.get(cv2.CAP_PROP_FRAME_WIDTH) < nextCap.get(cv2.CAP_PROP_FRAME_WIDTH):
                    cap.release()
                    cap = nextCap
                    continue
                nextCap.release()
            # 如果全都无法开启
            if cap == None or not cap.isOpened():
                raise Exception("Unable to open the camera")

            logging.info(f"_getPicture: CAP_PROP_FRAME = { cap.get(cv2.CAP_PROP_FRAME_WIDTH) } : { cap.get(cv2.CAP_PROP_FRAME_HEIGHT) }")
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
            cap.set(cv2.CAP_PROP_FPS, 30)
            cv2.namedWindow(PictureProcer.WIN_NAME, cv2.WINDOW_KEEPRATIO)
            while self.running:
                # 读取每一帧
                ret, frame = cap.read()
                if not ret:
                    logging.warning("_getPicture: Unable to read frames")
                    continue
                cv2.imshow(PictureProcer.WIN_NAME, frame)
                # 等待按键 s
                theKey = cv2.waitKey(1)
                if not theKey == ord("S") and not theKey == ord("L"):
                    continue
                # 添加记录
                initDataDict = vars(self.TypeData(TimeLine.getBaseToNow()))
                initDataDict.pop(TypeData.ATTR_TYPE, None)
                self.addData(initDataDict)
                # 发声提示
                Sound.Beep()
                # 保存图片
                cv2.imwrite(f"{self.pathDirName}/{self.getTypeNum()}.jpg", frame)
            # 释放摄像头
            cap.release()
            cv2.destroyWindow(PictureProcer.WIN_NAME)
            return True
        except Exception as e:
            logging.warning(f"_getPicture: {e}")
            self.getPath()
            return False