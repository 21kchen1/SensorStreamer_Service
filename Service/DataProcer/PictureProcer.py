import logging
import os
import threading
import cv2
from Resource.String.ServiceString import DataProcerString
from Service.DataProcer.DataProcer import DataProcer

"""
    Picture 数据处理
    @author: chen
"""
class PictureProcer(DataProcer):
    WIN_NAME = DataProcerString.WIN_NAME_PICTURE

    def __init__(self, TypeData) -> None:
        super().__init__(TypeData)

    """
        创建图片存储文件夹，并做对应的校验
    """
    def create(self, storagePath: str, dataCode: str) -> bool:
        if not super().create(storagePath, dataCode):
            return False

        # 生成存储路径
        self.pathDirName = f"{self.storagePath}/{self.TypeData.TYPE}"
        # 检查是否已经存在文件夹
        self.fileExists = os.path.isdir(self.pathDirName)
        if self.fileExists:
            return False
        # 创建文件路径
        if not os.path.exists(self.pathDirName):
            os.makedirs(self.pathDirName)

        # 创建图片存储路径
        self.running = True
        # 开启摄像机线程
        threading.Thread(target= self.addData).start()
        return True

    """
        打开摄像头并监听按键，并保存图片
    """
    def addData(self) -> bool:
        if not super().addData({}):
            return False

        try:
            # 打开摄像头
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                raise Exception("Unable to open the camera")

            while self.running:
                # 读取每一帧
                ret, frame = cap.read()
                if not ret:
                    logging.warning("addData: Unable to read frames")
                    continue
                cv2.imshow(PictureProcer.WIN_NAME, frame)
                # 等待按键 s
                if not cv2.waitKey(1) == ord("s"):
                    continue
                self._addTypeNum()
                # 保存图片
                cv2.imwrite(f"{self.pathDirName}/{self.getTypeNum()}.jpg", frame)
            # 释放摄像头
            cap.release()
            cv2.destroyWindow(PictureProcer.WIN_NAME)
            return True
        except Exception as e:
            logging.warning(f"addData: {e}")
            self.getPath()
            return False

    """
        关闭存储并返回 csv 文件路径
    """
    def getPath(self) -> str:
        if super().getPath() == None:
            return None
        return self.pathDirName