# Form implementation generated from reading ui file 'image_display.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ImageDisplay(object):
    def setupUi(self, ImageDisplay):
        ImageDisplay.setObjectName("ImageDisplay")
        ImageDisplay.resize(1000, 1000)
        ImageDisplay.setMinimumSize(QtCore.QSize(1000, 1000))
        self.mouse_pos = QtWidgets.QLabel(parent=ImageDisplay)
        self.mouse_pos.setGeometry(QtCore.QRect(20, 10, 241, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouse_pos.sizePolicy().hasHeightForWidth())
        self.mouse_pos.setSizePolicy(sizePolicy)
        self.mouse_pos.setText("")
        self.mouse_pos.setObjectName("mouse_pos")

        self.retranslateUi(ImageDisplay)
        QtCore.QMetaObject.connectSlotsByName(ImageDisplay)

    def retranslateUi(self, ImageDisplay):
        _translate = QtCore.QCoreApplication.translate
        ImageDisplay.setWindowTitle(_translate("ImageDisplay", "Form"))
