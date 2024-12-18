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
    def create(self, storagePath: str, dataCode: str, callBack= None) -> bool:
        if self.running:
            return False

        # 生成存储路径
        self.pathDirName = f"{storagePath}/{self.TypeData.TYPE}"
        # 检查是否已经存在文件夹
        self.fileExists = os.path.isdir(self.pathDirName)
        if self.fileExists:
            return False
        # 创建文件路径
        if not os.path.exists(self.pathDirName):
            os.makedirs(self.pathDirName)

        self.callBack = callBack
        # 创建图片存储路径
        self.running = True

        # 开启摄像机线程
        threading.Thread(target= self.addData).start()

    """
        打开摄像头并监听按键，并保存图片
    """
    def addData(self):
        if not self.running:
            return

        try:
            # 打开摄像头
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                logging.error("addData: Unable to open the camera")
                return
            # 照片计数
            pictureNum = 0

            while self.running:
                # 读取每一帧
                ret, frame = cap.read()
                if not ret:
                    logging.error("addData: Unable to read frames")
                    return
                cv2.imshow(PictureProcer.WIN_NAME, frame)
                # 等待按键 s
                if not cv2.waitKey(1) == ord("s"):
                    continue
                pictureNum += 1
                # 保存图片
                cv2.imwrite(f"{self.pathDirName}/{pictureNum}.jpg", frame)
                if self.callBack == None:
                    continue
                self.callBack(self.TypeData.TYPE)
            # 释放摄像头
            cap.release()
            cv2.destroyWindow(PictureProcer.WIN_NAME)
        except Exception as e:
            logging.warning(f"addData: {e}")

    """
        关闭存储并返回 csv 文件路径
    """
    def getPath(self) -> str:
        if not self.running:
            return None
        # 关闭存储
        self.running = False
        return self.pathDirName