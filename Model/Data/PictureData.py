from Model.Data.TypeData import TypeData

"""
    图片数据结构
    @author chen
"""

class PictureData(TypeData):
    TYPE = "PICTURE"

    def __init__(self, value):
        super().__init__(PictureData.TYPE, 0)
        # 照片
        self.value = value