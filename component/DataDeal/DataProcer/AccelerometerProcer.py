import logging
import pandas as pd
from Model.Data.AccelerometerData import AccelerometerData
from component.DataDeal.DataProcer.DataProcer import DataProcer

"""
    通用数据处理
    @author: chen
"""

class AccelerometerProcer(DataProcer):

    def __init__(self) -> None:
        super().__init__()
        self.dataSet = []

    def resetDataSet(self) -> None:
        self.dataSet = []

    def addData(self, data: dict) -> None:
        try:
            # 解包生成类
            classData = AccelerometerData(**data)
            dataDict = vars(classData)

            with self.lock:
                self.dataSet.append(dataDict)
        except Exception as e:
            logging.warning(f"addData: {e}")

    def getDataSet(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict(self.dataSet)