from Model.Data.TypeData import TypeData
from Resource.String.ModelString import DataString
from Service.DataProcer.PictureProcer import PictureProcer

"""
    图片数据结构
    @author chen
"""

class PictureData(TypeData):
    TYPE = DataString.TYPE_PICTURE

    def __init__(self, unixTimestamp):
        super().__init__(PictureData.TYPE, unixTimestamp)

PictureData.DATA_PROCER = PictureProcer(PictureData)