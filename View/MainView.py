# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1000, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QtCore.QSize(1000, 1000))
        MainWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWidget.setWindowOpacity(1.0)
        MainWidget.setStyleSheet("font: 75 9pt \"Times New Roman\";")
        self.gridLayout = QtWidgets.QGridLayout(MainWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.topWidget = QtWidgets.QWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.topWidget.sizePolicy().hasHeightForWidth())
        self.topWidget.setSizePolicy(sizePolicy)
        self.topWidget.setObjectName("topWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.topWidget)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.topRightwidget = QtWidgets.QWidget(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topRightwidget.sizePolicy().hasHeightForWidth())
        self.topRightwidget.setSizePolicy(sizePolicy)
        self.topRightwidget.setObjectName("topRightwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topRightwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dataInfoLabel = QtWidgets.QLabel(self.topRightwidget)
        self.dataInfoLabel.setObjectName("dataInfoLabel")
        self.verticalLayout_2.addWidget(self.dataInfoLabel)
        self.dataInfoText = QtWidgets.QTextEdit(self.topRightwidget)
        self.dataInfoText.setReadOnly(True)
        self.dataInfoText.setObjectName("dataInfoText")
        self.verticalLayout_2.addWidget(self.dataInfoText)
        self.gridLayout_2.addWidget(self.topRightwidget, 0, 1, 1, 1)
        self.topLeftwidget = QtWidgets.QWidget(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLeftwidget.sizePolicy().hasHeightForWidth())
        self.topLeftwidget.setSizePolicy(sizePolicy)
        self.topLeftwidget.setObjectName("topLeftwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.topLeftwidget)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.settingWidget = QtWidgets.QWidget(self.topLeftwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.settingWidget.sizePolicy().hasHeightForWidth())
        self.settingWidget.setSizePolicy(sizePolicy)
        self.settingWidget.setObjectName("settingWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settingWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.codeSetWidget = QtWidgets.QWidget(self.settingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.codeSetWidget.sizePolicy().hasHeightForWidth())
        self.codeSetWidget.setSizePolicy(sizePolicy)
        self.codeSetWidget.setObjectName("codeSetWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.codeSetWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.codeSetLabel = QtWidgets.QLabel(self.codeSetWidget)
        self.codeSetLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.codeSetLabel.setStyleSheet("")
        self.codeSetLabel.setObjectName("codeSetLabel")
        self.verticalLayout_3.addWidget(self.codeSetLabel)
        self.codeSetEdit = QtWidgets.QLineEdit(self.codeSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeSetEdit.sizePolicy().hasHeightForWidth())
        self.codeSetEdit.setSizePolicy(sizePolicy)
        self.codeSetEdit.setObjectName("codeSetEdit")
        self.verticalLayout_3.addWidget(self.codeSetEdit)
        self.verticalLayout.addWidget(self.codeSetWidget)
        self.sensorSetWidget = QtWidgets.QWidget(self.settingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.sensorSetWidget.sizePolicy().hasHeightForWidth())
        self.sensorSetWidget.setSizePolicy(sizePolicy)
        self.sensorSetWidget.setObjectName("sensorSetWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sensorSetWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sensorSetlabel = QtWidgets.QLabel(self.sensorSetWidget)
        self.sensorSetlabel.setObjectName("sensorSetlabel")
        self.verticalLayout_4.addWidget(self.sensorSetlabel)
        self.videoCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoCheck.sizePolicy().hasHeightForWidth())
        self.videoCheck.setSizePolicy(sizePolicy)
        self.videoCheck.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.videoCheck.setChecked(True)
        self.videoCheck.setTristate(False)
        self.videoCheck.setObjectName("videoCheck")
        self.verticalLayout_4.addWidget(self.videoCheck)
        self.audioCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioCheck.sizePolicy().hasHeightForWidth())
        self.audioCheck.setSizePolicy(sizePolicy)
        self.audioCheck.setChecked(True)
        self.audioCheck.setObjectName("audioCheck")
        self.verticalLayout_4.addWidget(self.audioCheck)
        self.heartRateCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heartRateCheck.sizePolicy().hasHeightForWidth())
        self.heartRateCheck.setSizePolicy(sizePolicy)
        self.heartRateCheck.setChecked(True)
        self.heartRateCheck.setObjectName("heartRateCheck")
        self.verticalLayout_4.addWidget(self.heartRateCheck)
        self.accelerometerCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accelerometerCheck.sizePolicy().hasHeightForWidth())
        self.accelerometerCheck.setSizePolicy(sizePolicy)
        self.accelerometerCheck.setChecked(True)
        self.accelerometerCheck.setObjectName("accelerometerCheck")
        self.verticalLayout_4.addWidget(self.accelerometerCheck)
        self.gyroscopeCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyroscopeCheck.sizePolicy().hasHeightForWidth())
        self.gyroscopeCheck.setSizePolicy(sizePolicy)
        self.gyroscopeCheck.setChecked(True)
        self.gyroscopeCheck.setObjectName("gyroscopeCheck")
        self.verticalLayout_4.addWidget(self.gyroscopeCheck)
        self.rotationVectorCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotationVectorCheck.sizePolicy().hasHeightForWidth())
        self.rotationVectorCheck.setSizePolicy(sizePolicy)
        self.rotationVectorCheck.setChecked(True)
        self.rotationVectorCheck.setObjectName("rotationVectorCheck")
        self.verticalLayout_4.addWidget(self.rotationVectorCheck)
        self.magneticFieldCheck = QtWidgets.QCheckBox(self.sensorSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magneticFieldCheck.sizePolicy().hasHeightForWidth())
        self.magneticFieldCheck.setSizePolicy(sizePolicy)
        self.magneticFieldCheck.setChecked(True)
        self.magneticFieldCheck.setObjectName("magneticFieldCheck")
        self.verticalLayout_4.addWidget(self.magneticFieldCheck)
        self.verticalLayout.addWidget(self.sensorSetWidget)
        self.gridLayout_3.addWidget(self.settingWidget, 2, 0, 1, 1)
        self.statusWidget = QtWidgets.QWidget(self.topLeftwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.statusWidget.sizePolicy().hasHeightForWidth())
        self.statusWidget.setSizePolicy(sizePolicy)
        self.statusWidget.setObjectName("statusWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.statusWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.phoneStatus = QtWidgets.QLineEdit(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneStatus.sizePolicy().hasHeightForWidth())
        self.phoneStatus.setSizePolicy(sizePolicy)
        self.phoneStatus.setReadOnly(True)
        self.phoneStatus.setObjectName("phoneStatus")
        self.gridLayout_4.addWidget(self.phoneStatus, 1, 1, 1, 1)
        self.watchStatus = QtWidgets.QLineEdit(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watchStatus.sizePolicy().hasHeightForWidth())
        self.watchStatus.setSizePolicy(sizePolicy)
        self.watchStatus.setReadOnly(True)
        self.watchStatus.setObjectName("watchStatus")
        self.gridLayout_4.addWidget(self.watchStatus, 0, 1, 1, 1)
        self.watchLabel = QtWidgets.QLabel(self.statusWidget)
        self.watchLabel.setObjectName("watchLabel")
        self.gridLayout_4.addWidget(self.watchLabel, 0, 0, 1, 1)
        self.phoneLabel = QtWidgets.QLabel(self.statusWidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.gridLayout_4.addWidget(self.phoneLabel, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.statusWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.topLeftwidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.topWidget, 1, 0, 1, 1)
        self.buttomWidget = QtWidgets.QWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttomWidget.sizePolicy().hasHeightForWidth())
        self.buttomWidget.setSizePolicy(sizePolicy)
        self.buttomWidget.setObjectName("buttomWidget")
        self.buttomWidgetLayout = QtWidgets.QGridLayout(self.buttomWidget)
        self.buttomWidgetLayout.setContentsMargins(9, 18, -1, 18)
        self.buttomWidgetLayout.setObjectName("buttomWidgetLayout")
        self.startStream = QtWidgets.QPushButton(self.buttomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startStream.sizePolicy().hasHeightForWidth())
        self.startStream.setSizePolicy(sizePolicy)
        self.startStream.setObjectName("startStream")
        self.buttomWidgetLayout.addWidget(self.startStream, 0, 1, 1, 1)
        self.stopStream = QtWidgets.QPushButton(self.buttomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stopStream.sizePolicy().hasHeightForWidth())
        self.stopStream.setSizePolicy(sizePolicy)
        self.stopStream.setStyleSheet("")
        self.stopStream.setObjectName("stopStream")
        self.buttomWidgetLayout.addWidget(self.stopStream, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.buttomWidgetLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.buttomWidgetLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.buttomWidgetLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.buttomWidget, 2, 0, 1, 1)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Device controller"))
        self.dataInfoLabel.setText(_translate("MainWidget", "UDPLink Recv Data:"))
        self.dataInfoText.setHtml(_translate("MainWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">waitting for data...</p></body></html>"))
        self.codeSetLabel.setText(_translate("MainWidget", "Setting Data Code:"))
        self.sensorSetlabel.setText(_translate("MainWidget", "Setting Sensor Launch:"))
        self.videoCheck.setText(_translate("MainWidget", "Video"))
        self.audioCheck.setText(_translate("MainWidget", "Audio"))
        self.heartRateCheck.setText(_translate("MainWidget", "Heart Rate"))
        self.accelerometerCheck.setText(_translate("MainWidget", "Accelerometer"))
        self.gyroscopeCheck.setText(_translate("MainWidget", "Gyroscope"))
        self.rotationVectorCheck.setText(_translate("MainWidget", "Rotation Vector"))
        self.magneticFieldCheck.setText(_translate("MainWidget", "Magnetic Field"))
        self.phoneStatus.setText(_translate("MainWidget", "off"))
        self.watchStatus.setText(_translate("MainWidget", "off"))
        self.watchLabel.setText(_translate("MainWidget", "Watch Status:"))
        self.phoneLabel.setText(_translate("MainWidget", "Phone Status:"))
        self.startStream.setText(_translate("MainWidget", "Start Stream"))
        self.stopStream.setText(_translate("MainWidget", "Stop Stream"))
