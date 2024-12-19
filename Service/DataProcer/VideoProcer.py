import io
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
        if not super()._procData(typeData):
            return False

        try:
            # 将字节列表转换为字节数据
            dataBytes = np.array(typeData.values, dtype=np.uint8).tobytes()
            # 使用 io.BytesIO 将字节数据转换为文件类对象
            imageData = io.BytesIO(dataBytes).getvalue()
            # 使用 cv2 读取图像数据
            image = cv2.imdecode(np.frombuffer(imageData, np.uint8), cv2.IMREAD_UNCHANGED)

            # 检查图像是否加载成功
            if image is not None:
                # 显示
                cv2.imshow(VideoProcer.WIN_NAME, image)
                cv2.waitKey(1)
            return True
        except Exception as e:
            logging.error(f"_procData: {e}")
            return False