import logging

"""
    Sound 播放音频
    @author: chen
    @version 1.0
"""

class Sound:
    # 尝试引入 winsound
    try:
        import winsound
        __SOUND = winsound
    except ImportError as e:
        logging.error({ e })
        __SOUND = None

    """
        产生蜂鸣
        @param frequency 频率
        @param duration 持续时间
    """
    @staticmethod
    def Beep(frequency= 2500, duration= 1000) -> None:
        if Sound.__SOUND == None:
            return
        Sound.__SOUND.Beep(frequency, duration)

    """
        产生信息提示音
        @param type 提示类型
    """
    @staticmethod
    def MessageBeep(type= 0) -> None:
        if Sound.__SOUND == None:
            return
        Sound.__SOUND.MessageBeep(type)