import io
import logging
import threading
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
    def __init__(self, TypeData, bufRowSize= 500) -> None:
        super().__init__(TypeData, bufRowSize)
        self.image = None

    """
        父函数拓展，增加图像显示线程的启动
    """
    def create(self, storagePath, dataCode) -> bool:
        if not super().create(storagePath, dataCode):
            return False

        self.image = None
        # 显示图像的线程
        threading.Thread(target= self._showVideo).start()
        return True

    """
        图像显示函数
    """
    def _showVideo(self) -> None:
        if not self.running:
            return

        while self.running:
            if self.image is None:
                continue
            cv2.imshow(VideoProcer.WIN_NAME, self.image)
            cv2.waitKey(1)
        # 检测窗口是否存在
        if cv2.getWindowProperty(VideoProcer.WIN_NAME, cv2.WND_PROP_VISIBLE) < 1:
            return
        cv2.destroyWindow(VideoProcer.WIN_NAME)

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
            self.image = cv2.imdecode(np.frombuffer(imageData, np.uint8), cv2.IMREAD_UNCHANGED)
            return True
        except Exception as e:
            logging.error(f"_procData: {e}")
            return False