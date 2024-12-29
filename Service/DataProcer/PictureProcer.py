import logging
import threading
import cv2
from Model.Data.TypeData import TypeData
from Resource.String.ServiceString import DataProcerString
from Service.DataProcer.ListenProcer import ListenProcer
from Service.Time.TimeLine import TimeLine

"""
    PictureNew 数据处理
    @author: chen
"""
class PictureProcer(ListenProcer):
    WIN_NAME = DataProcerString.WIN_NAME_PICTURE
    CAP_WIDTH = 2560
    CAP_HEIGHT = 1440
    CAP_NUM = 10

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
                cap = cv2.VideoCapture(i)
                # 如果是可以使用的摄像头
                if cap.isOpened():
                    break
            # 如果全都无法开启
            if cap == None or not cap.isOpened():
                raise Exception("Unable to open the camera")
            # 设置清晰度
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, PictureProcer.CAP_WIDTH)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, PictureProcer.CAP_HEIGHT)

            logging.info(f"_getPicture: CAP_PROP_FRAME = { cap.get(cv2.CAP_PROP_FRAME_WIDTH) } : { cap.get(cv2.CAP_PROP_FRAME_HEIGHT) }")

            while self.running:
                # 读取每一帧
                ret, frame = cap.read()
                if not ret:
                    logging.warning("_getPicture: Unable to read frames")
                    continue
                cv2.imshow(PictureProcer.WIN_NAME, frame)
                # 等待按键 s
                if not cv2.waitKey(1) == ord("s"):
                    continue
                # 添加记录
                initDataDict = vars(self.TypeData(TimeLine.getBaseToNow()))
                initDataDict.pop(TypeData.ATTR_TYPE, None)
                self.addData(initDataDict)
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