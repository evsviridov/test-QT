# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TestWindow(object):
    def setupUi(self, TestWindow):
        if not TestWindow.objectName():
            TestWindow.setObjectName(u"TestWindow")
        TestWindow.resize(1054, 733)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TestWindow.sizePolicy().hasHeightForWidth())
        TestWindow.setSizePolicy(sizePolicy)
        TestWindow.setMouseTracking(True)
        self.horizontalLayout = QHBoxLayout(TestWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QweLayout = QVBoxLayout()
        self.QweLayout.setObjectName(u"QweLayout")

        self.horizontalLayout.addLayout(self.QweLayout)

        self.AnsLayout = QVBoxLayout()
        self.AnsLayout.setObjectName(u"AnsLayout")

        self.horizontalLayout.addLayout(self.AnsLayout)


        self.retranslateUi(TestWindow)

        QMetaObject.connectSlotsByName(TestWindow)
    # setupUi

    def retranslateUi(self, TestWindow):
        TestWindow.setWindowTitle(QCoreApplication.translate("TestWindow", u"TEST", None))
    # retranslateUi

