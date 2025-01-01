
"""
    Capture 拍摄功能
    @author: chen
    @version 1.0
"""

import logging
import cv2


class Capture:
    # 最大分辨率
    MAX_CAP_WIDTH = 2560
    MAX_CAP_HEIGHT = 1440
    # 最大数量
    MAX_CAP_NUM = 10

    """
        设置分辨率
        @param capWidth 横向像素
        @param capHeight 纵向像素
    """
    def __init__(self, capWidth= MAX_CAP_WIDTH, capHeight= MAX_CAP_HEIGHT) -> None:
        self.capWidth = min(capWidth, Capture.MAX_CAP_WIDTH)
        self.capHeight = min(capHeight, Capture.MAX_CAP_HEIGHT)
        self.cap = None

    """
        根据下标创建相机
        @param index 下标
    """
    def create(self, index= 0) -> bool:
        if self.cap != None:
            return False

        theCap = cv2.VideoCapture(index)
        if not theCap.isOpened():
            return False
        self.cap = theCap
        # 设置分辨率
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.capWidth)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capHeight)
        logging.info(f"create : CAP_PROP_FRAME = { self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) } : { self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) }")
        return True

    """
        获取最接近目标清晰度的相机
    """
    def create(self) -> int:
        if self.cap != None:
            return False
        # 记录相机下标
        index = False
        for i in range(Capture.MAX_CAP_NUM):
            nextCap = cv2.VideoCapture(i)
            if not nextCap.isOpened():
                continue
            nextCap.set(cv2.CAP_PROP_FRAME_WIDTH, self.capWidth)
            nextCap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capHeight)
            # 如果是可用摄像头
            if self.cap == None:
                self.cap = nextCap
                continue
            # 比较分辨率
            if self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) >= nextCap.get(cv2.CAP_PROP_FRAME_WIDTH):
                nextCap.release()
            self.cap.release()
            self.cap = nextCap
            index = i

        return index