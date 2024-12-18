import logging
import cv2
import numpy as np
from Resource.String.ServiceString import DataProcerString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    Video 视频处理
    @author: chen
"""

class VideoProcer(ListenProcer):
    WIN_NAME = DataProcerString.WIN_NAME_VIDEO

    """
        @TypeData: 数据构造函数
        @bufRowSize: 缓冲区行数
    """
    def __init__(self, TypeData, bufRowSize=500):
        super().__init__(TypeData, bufRowSize)


    """
        @Override 重写，将结构化数据转化为图像并显示
    """
    def _procData(self, typeData) -> bool:
        if not isinstance(typeData, self.TypeData):
            return False

        try:
            # 图片框架
            frame = np.frombuffer(typeData.values, dtype= np.uint8).reshape((typeData.height, typeData.width, 3))
            cv2.imshow(, frame)
            cv2.waitKey(50)
            return True
        except Exception as e:
            logging.error(f"_procData: {e}")
            return False