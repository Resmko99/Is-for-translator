# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QTextEdit, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 768)
        MainWindow.setMinimumSize(QSize(1156, 768))
        MainWindow.setMaximumSize(QSize(3840, 2160))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimazeBtn = QPushButton(self.widget_2)
        self.minimazeBtn.setObjectName(u"minimazeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimazeBtn.setIcon(icon1)
        self.minimazeBtn.setIconSize(QSize(20, 20))
        self.minimazeBtn.setCheckable(True)
        self.minimazeBtn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.minimazeBtn)

        self.expandBtn = QPushButton(self.widget_2)
        self.expandBtn.setObjectName(u"expandBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expandBtn.setIcon(icon2)
        self.expandBtn.setIconSize(QSize(20, 20))
        self.expandBtn.setCheckable(True)
        self.expandBtn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.expandBtn)

        self.closeBtn = QPushButton(self.widget_2)
        self.closeBtn.setObjectName(u"closeBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/close-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setIconSize(QSize(20, 20))
        self.closeBtn.setCheckable(True)
        self.closeBtn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(10000000, 10000000))
        self.pageLog = QWidget()
        self.pageLog.setObjectName(u"pageLog")
        self.gridLayout_11 = QGridLayout(self.pageLog)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.pageLog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setPixmap(QPixmap(u":/icon/icon/Logo(100x100).png"))
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setMargin(8)

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.pageLog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setMargin(10)

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.pageLog)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.lineEdit = QLineEdit(self.pageLog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.label_13 = QLabel(self.pageLog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMargin(0)

        self.verticalLayout_6.addWidget(self.label_13)

        self.lineEdit_2 = QLineEdit(self.pageLog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_6.addWidget(self.lineEdit_2)

        self.inLogBtn = QPushButton(self.pageLog)
        self.inLogBtn.setObjectName(u"inLogBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inLogBtn.sizePolicy().hasHeightForWidth())
        self.inLogBtn.setSizePolicy(sizePolicy3)
        self.inLogBtn.setMaximumSize(QSize(16777215, 16777215))
        self.inLogBtn.setLayoutDirection(Qt.LeftToRight)
        self.inLogBtn.setAutoFillBackground(True)

        self.verticalLayout_6.addWidget(self.inLogBtn, 0, Qt.AlignHCenter)

        self.notRegLabel = QLabel(self.pageLog)
        self.notRegLabel.setObjectName(u"notRegLabel")
        self.notRegLabel.setMargin(4)

        self.verticalLayout_6.addWidget(self.notRegLabel, 0, Qt.AlignHCenter)

        self.forgotPasLabel = QLabel(self.pageLog)
        self.forgotPasLabel.setObjectName(u"forgotPasLabel")

        self.verticalLayout_6.addWidget(self.forgotPasLabel, 0, Qt.AlignHCenter)


        self.gridLayout_11.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageLog)
        self.pageChangePas = QWidget()
        self.pageChangePas.setObjectName(u"pageChangePas")
        self.gridLayout_12 = QGridLayout(self.pageChangePas)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalSpacer_10 = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_26 = QLabel(self.pageChangePas)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setTextFormat(Qt.AutoText)
        self.label_26.setPixmap(QPixmap(u":/icon/icon/Logo(100x100).png"))
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(False)
        self.label_26.setMargin(8)

        self.verticalLayout_12.addWidget(self.label_26)

        self.label_27 = QLabel(self.pageChangePas)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setMargin(10)

        self.verticalLayout_12.addWidget(self.label_27)

        self.label_28 = QLabel(self.pageChangePas)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_12.addWidget(self.label_28)

        self.lineEdit_9 = QLineEdit(self.pageChangePas)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_12.addWidget(self.lineEdit_9)

        self.label_29 = QLabel(self.pageChangePas)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_12.addWidget(self.label_29)

        self.lineEdit_10 = QLineEdit(self.pageChangePas)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_12.addWidget(self.lineEdit_10)

        self.changePasBtn = QPushButton(self.pageChangePas)
        self.changePasBtn.setObjectName(u"changePasBtn")
        sizePolicy3.setHeightForWidth(self.changePasBtn.sizePolicy().hasHeightForWidth())
        self.changePasBtn.setSizePolicy(sizePolicy3)
        self.changePasBtn.setMinimumSize(QSize(110, 0))
        self.changePasBtn.setMaximumSize(QSize(16777215, 16777215))
        self.changePasBtn.setSizeIncrement(QSize(0, 0))
        self.changePasBtn.setLayoutDirection(Qt.LeftToRight)
        self.changePasBtn.setAutoFillBackground(True)

        self.verticalLayout_12.addWidget(self.changePasBtn, 0, Qt.AlignHCenter)

        self.backChangePasBtn = QPushButton(self.pageChangePas)
        self.backChangePasBtn.setObjectName(u"backChangePasBtn")
        self.backChangePasBtn.setMinimumSize(QSize(110, 0))
        self.backChangePasBtn.setMaximumSize(QSize(16777215, 16777215))
        self.backChangePasBtn.setSizeIncrement(QSize(100, 0))

        self.verticalLayout_12.addWidget(self.backChangePasBtn, 0, Qt.AlignHCenter)


        self.gridLayout_12.addLayout(self.verticalLayout_12, 1, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageChangePas)
        self.pageResPas = QWidget()
        self.pageResPas.setObjectName(u"pageResPas")
        self.gridLayout_9 = QGridLayout(self.pageResPas)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_8 = QSpacerItem(20, 262, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_23 = QLabel(self.pageResPas)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setTextFormat(Qt.AutoText)
        self.label_23.setPixmap(QPixmap(u":/icon/icon/Logo(100x100).png"))
        self.label_23.setScaledContents(False)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setWordWrap(False)
        self.label_23.setMargin(8)

        self.verticalLayout_11.addWidget(self.label_23)

        self.label_24 = QLabel(self.pageResPas)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setMargin(10)

        self.verticalLayout_11.addWidget(self.label_24)

        self.label_25 = QLabel(self.pageResPas)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_11.addWidget(self.label_25)

        self.lineEdit_8 = QLineEdit(self.pageResPas)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_11.addWidget(self.lineEdit_8)

        self.nextResBtn = QPushButton(self.pageResPas)
        self.nextResBtn.setObjectName(u"nextResBtn")
        sizePolicy3.setHeightForWidth(self.nextResBtn.sizePolicy().hasHeightForWidth())
        self.nextResBtn.setSizePolicy(sizePolicy3)
        self.nextResBtn.setMaximumSize(QSize(16777214, 16777215))
        self.nextResBtn.setLayoutDirection(Qt.LeftToRight)
        self.nextResBtn.setAutoFillBackground(True)

        self.verticalLayout_11.addWidget(self.nextResBtn, 0, Qt.AlignHCenter)

        self.backResBtn = QPushButton(self.pageResPas)
        self.backResBtn.setObjectName(u"backResBtn")
        self.backResBtn.setMinimumSize(QSize(60, 0))
        self.backResBtn.setSizeIncrement(QSize(100, 0))

        self.verticalLayout_11.addWidget(self.backResBtn, 0, Qt.AlignHCenter)


        self.gridLayout_9.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 261, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageResPas)
        self.pageReg = QWidget()
        self.pageReg.setObjectName(u"pageReg")
        self.gridLayout = QGridLayout(self.pageReg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.pageReg)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setPixmap(QPixmap(u":/icon/icon/Logo(100x100).png"))
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setWordWrap(False)
        self.label_16.setMargin(8)

        self.verticalLayout_8.addWidget(self.label_16)

        self.label_17 = QLabel(self.pageReg)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setMargin(10)

        self.verticalLayout_8.addWidget(self.label_17)

        self.label_19 = QLabel(self.pageReg)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_8.addWidget(self.label_19)

        self.lineEdit_3 = QLineEdit(self.pageReg)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_8.addWidget(self.lineEdit_3)

        self.label_20 = QLabel(self.pageReg)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMargin(0)

        self.verticalLayout_8.addWidget(self.label_20)

        self.lineEdit_4 = QLineEdit(self.pageReg)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_8.addWidget(self.lineEdit_4)

        self.label_22 = QLabel(self.pageReg)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_8.addWidget(self.label_22)

        self.lineEdit_5 = QLineEdit(self.pageReg)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_8.addWidget(self.lineEdit_5)

        self.regBtn = QPushButton(self.pageReg)
        self.regBtn.setObjectName(u"regBtn")
        sizePolicy3.setHeightForWidth(self.regBtn.sizePolicy().hasHeightForWidth())
        self.regBtn.setSizePolicy(sizePolicy3)
        self.regBtn.setMaximumSize(QSize(16777215, 16777215))
        self.regBtn.setLayoutDirection(Qt.LeftToRight)
        self.regBtn.setAutoFillBackground(True)

        self.verticalLayout_8.addWidget(self.regBtn, 0, Qt.AlignHCenter)

        self.backBtnReg = QPushButton(self.pageReg)
        self.backBtnReg.setObjectName(u"backBtnReg")
        self.backBtnReg.setMinimumSize(QSize(100, 0))
        self.backBtnReg.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.backBtnReg, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.gridLayout.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.pageReg)
        self.pageMain = QWidget()
        self.pageMain.setObjectName(u"pageMain")
        self.pageMain.setEnabled(True)
        self.gridLayout_10 = QGridLayout(self.pageMain)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.pageMain)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.widget_3)

        self.openMenuBtn = QPushButton(self.widget)
        self.openMenuBtn.setObjectName(u"openMenuBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/rev.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/icon/free-icon-chevron-248744.png", QSize(), QIcon.Active, QIcon.On)
        icon4.addFile(u":/icon/icon/rev.png", QSize(), QIcon.Selected, QIcon.On)
        self.openMenuBtn.setIcon(icon4)
        self.openMenuBtn.setIconSize(QSize(20, 20))
        self.openMenuBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.openMenuBtn)

        self.horizontalSpacer_3 = QSpacerItem(742, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout_10.addWidget(self.widget, 0, 2, 1, 1)

        self.fullMenu = QWidget(self.pageMain)
        self.fullMenu.setObjectName(u"fullMenu")
        self.verticalLayout_4 = QVBoxLayout(self.fullMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.fullMenu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/icon/icon/Logo(100x100).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.fullMenu)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(9)
        font.setBold(False)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleBtn_2 = QPushButton(self.fullMenu)
        self.titleBtn_2.setObjectName(u"titleBtn_2")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/free-icon-book-9193009.png", QSize(), QIcon.Normal, QIcon.Off)
        self.titleBtn_2.setIcon(icon5)
        self.titleBtn_2.setIconSize(QSize(20, 20))
        self.titleBtn_2.setCheckable(True)
        self.titleBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.titleBtn_2)

        self.incomeBtn_2 = QPushButton(self.fullMenu)
        self.incomeBtn_2.setObjectName(u"incomeBtn_2")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/free-icon-coin-550650.png", QSize(), QIcon.Normal, QIcon.Off)
        self.incomeBtn_2.setIcon(icon6)
        self.incomeBtn_2.setIconSize(QSize(20, 20))
        self.incomeBtn_2.setCheckable(True)
        self.incomeBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.incomeBtn_2)

        self.scheduleBtn_2 = QPushButton(self.fullMenu)
        self.scheduleBtn_2.setObjectName(u"scheduleBtn_2")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/free-icon-clock-2902894.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scheduleBtn_2.setIcon(icon7)
        self.scheduleBtn_2.setIconSize(QSize(20, 20))
        self.scheduleBtn_2.setCheckable(True)
        self.scheduleBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.scheduleBtn_2)

        self.socialNetworksBtn_2 = QPushButton(self.fullMenu)
        self.socialNetworksBtn_2.setObjectName(u"socialNetworksBtn_2")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/free-icon-social-media-9351311.png", QSize(), QIcon.Normal, QIcon.Off)
        self.socialNetworksBtn_2.setIcon(icon8)
        self.socialNetworksBtn_2.setIconSize(QSize(20, 20))
        self.socialNetworksBtn_2.setCheckable(True)
        self.socialNetworksBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.socialNetworksBtn_2)

        self.fileSharingBtn_2 = QPushButton(self.fullMenu)
        self.fileSharingBtn_2.setObjectName(u"fileSharingBtn_2")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/free-icon-file-sharing-10004135.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileSharingBtn_2.setIcon(icon9)
        self.fileSharingBtn_2.setIconSize(QSize(20, 20))
        self.fileSharingBtn_2.setCheckable(True)
        self.fileSharingBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fileSharingBtn_2)

        self.acceptFileBtn_2 = QPushButton(self.fullMenu)
        self.acceptFileBtn_2.setObjectName(u"acceptFileBtn_2")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/free-icon-envelope-2168955.png", QSize(), QIcon.Normal, QIcon.Off)
        self.acceptFileBtn_2.setIcon(icon10)
        self.acceptFileBtn_2.setIconSize(QSize(20, 20))
        self.acceptFileBtn_2.setCheckable(True)
        self.acceptFileBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.acceptFileBtn_2)

        self.accountBtn_2 = QPushButton(self.fullMenu)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn_2.setIcon(icon11)
        self.accountBtn_2.setIconSize(QSize(20, 20))
        self.accountBtn_2.setCheckable(True)
        self.accountBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.accountBtn_2)

        self.translateBtn_2 = QPushButton(self.fullMenu)
        self.translateBtn_2.setObjectName(u"translateBtn_2")
        icon12 = QIcon()
        icon12.addFile(u":/icon/icon/education.png", QSize(), QIcon.Normal, QIcon.Off)
        self.translateBtn_2.setIcon(icon12)
        self.translateBtn_2.setIconSize(QSize(20, 20))
        self.translateBtn_2.setCheckable(True)
        self.translateBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.translateBtn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 382, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.aboutUs_2 = QPushButton(self.fullMenu)
        self.aboutUs_2.setObjectName(u"aboutUs_2")
        icon13 = QIcon()
        icon13.addFile(u":/icon/icon/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutUs_2.setIcon(icon13)
        self.aboutUs_2.setIconSize(QSize(20, 20))
        self.aboutUs_2.setCheckable(True)
        self.aboutUs_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.aboutUs_2)


        self.gridLayout_10.addWidget(self.fullMenu, 0, 1, 3, 1)

        self.icon = QWidget(self.pageMain)
        self.icon.setObjectName(u"icon")
        self.verticalLayout_3 = QVBoxLayout(self.icon)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icon/icon/Logo(100x100).png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleBtn_1 = QPushButton(self.icon)
        self.titleBtn_1.setObjectName(u"titleBtn_1")
        self.titleBtn_1.setIcon(icon5)
        self.titleBtn_1.setIconSize(QSize(20, 20))
        self.titleBtn_1.setCheckable(True)
        self.titleBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.titleBtn_1)

        self.incomeBtn_1 = QPushButton(self.icon)
        self.incomeBtn_1.setObjectName(u"incomeBtn_1")
        self.incomeBtn_1.setIcon(icon6)
        self.incomeBtn_1.setIconSize(QSize(20, 20))
        self.incomeBtn_1.setCheckable(True)
        self.incomeBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.incomeBtn_1)

        self.scheduleBtn_1 = QPushButton(self.icon)
        self.scheduleBtn_1.setObjectName(u"scheduleBtn_1")
        self.scheduleBtn_1.setIcon(icon7)
        self.scheduleBtn_1.setIconSize(QSize(20, 20))
        self.scheduleBtn_1.setCheckable(True)
        self.scheduleBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.scheduleBtn_1)

        self.socialNetworksBtn_1 = QPushButton(self.icon)
        self.socialNetworksBtn_1.setObjectName(u"socialNetworksBtn_1")
        self.socialNetworksBtn_1.setIcon(icon8)
        self.socialNetworksBtn_1.setIconSize(QSize(20, 20))
        self.socialNetworksBtn_1.setCheckable(True)
        self.socialNetworksBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.socialNetworksBtn_1)

        self.fileSharingBtn_1 = QPushButton(self.icon)
        self.fileSharingBtn_1.setObjectName(u"fileSharingBtn_1")
        self.fileSharingBtn_1.setIcon(icon9)
        self.fileSharingBtn_1.setIconSize(QSize(20, 20))
        self.fileSharingBtn_1.setCheckable(True)
        self.fileSharingBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.fileSharingBtn_1)

        self.acceptFileBtn_1 = QPushButton(self.icon)
        self.acceptFileBtn_1.setObjectName(u"acceptFileBtn_1")
        self.acceptFileBtn_1.setIcon(icon10)
        self.acceptFileBtn_1.setIconSize(QSize(20, 20))
        self.acceptFileBtn_1.setCheckable(True)
        self.acceptFileBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.acceptFileBtn_1)

        self.accountBtn_1 = QPushButton(self.icon)
        self.accountBtn_1.setObjectName(u"accountBtn_1")
        self.accountBtn_1.setIcon(icon11)
        self.accountBtn_1.setIconSize(QSize(20, 20))
        self.accountBtn_1.setCheckable(True)
        self.accountBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.accountBtn_1)

        self.translateBtn_1 = QPushButton(self.icon)
        self.translateBtn_1.setObjectName(u"translateBtn_1")
        self.translateBtn_1.setIcon(icon12)
        self.translateBtn_1.setIconSize(QSize(20, 20))
        self.translateBtn_1.setCheckable(True)
        self.translateBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.translateBtn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 382, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.aboutUs_1 = QPushButton(self.icon)
        self.aboutUs_1.setObjectName(u"aboutUs_1")
        self.aboutUs_1.setIcon(icon13)
        self.aboutUs_1.setIconSize(QSize(20, 20))
        self.aboutUs_1.setCheckable(True)
        self.aboutUs_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.aboutUs_1)


        self.gridLayout_10.addWidget(self.icon, 0, 0, 3, 1)

        self.stackedWidget_2 = QStackedWidget(self.pageMain)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setEnabled(True)
        self.pageTitle = QWidget()
        self.pageTitle.setObjectName(u"pageTitle")
        self.gridLayout_13 = QGridLayout(self.pageTitle)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.pageTitle)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(250, 0))
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushOpenAdd = QPushButton(self.widget_4)
        self.pushOpenAdd.setObjectName(u"pushOpenAdd")
        self.pushOpenAdd.setMinimumSize(QSize(0, 0))
        self.pushOpenAdd.setMaximumSize(QSize(16777215, 16777215))
        icon14 = QIcon()
        icon14.addFile(u":/icon/icon/free-icon-add-7222864.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushOpenAdd.setIcon(icon14)
        self.pushOpenAdd.setIconSize(QSize(20, 20))

        self.verticalLayout_13.addWidget(self.pushOpenAdd)

        self.pushOpenEdit = QPushButton(self.widget_4)
        self.pushOpenEdit.setObjectName(u"pushOpenEdit")
        icon15 = QIcon()
        icon15.addFile(u":/icon/icon/free-icon-pencil-7266923.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushOpenEdit.setIcon(icon15)
        self.pushOpenEdit.setIconSize(QSize(20, 20))

        self.verticalLayout_13.addWidget(self.pushOpenEdit)

        self.pushOpenDel = QPushButton(self.widget_4)
        self.pushOpenDel.setObjectName(u"pushOpenDel")
        icon16 = QIcon()
        icon16.addFile(u":/icon/icon/free-icon-minus-button-4315581 \u043a\u043e\u043f\u0438\u044f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushOpenDel.setIcon(icon16)
        self.pushOpenDel.setIconSize(QSize(20, 20))

        self.verticalLayout_13.addWidget(self.pushOpenDel)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_12, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_4, 0, 1, 2, 2)

        self.titleWidget = QWidget(self.pageTitle)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy4)
        self.gridLayout_24 = QGridLayout(self.titleWidget)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.titleGrid = QGridLayout()
        self.titleGrid.setSpacing(6)
        self.titleGrid.setObjectName(u"titleGrid")

        self.gridLayout_24.addLayout(self.titleGrid, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.titleWidget, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.SearchEdit = QLineEdit(self.pageTitle)
        self.SearchEdit.setObjectName(u"SearchEdit")

        self.horizontalLayout_3.addWidget(self.SearchEdit)

        self.SearchBtn = QPushButton(self.pageTitle)
        self.SearchBtn.setObjectName(u"SearchBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icon/icon/free-icon-loupe-216463.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SearchBtn.setIcon(icon17)
        self.SearchBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.SearchBtn)

        self.pushButton = QPushButton(self.pageTitle)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        icon18 = QIcon()
        icon18.addFile(u":/icon/icon/rev.png", QSize(), QIcon.Normal, QIcon.Off)
        icon18.addFile(u":/icon/icon/free-icon-chevron-248744.png", QSize(), QIcon.Active, QIcon.On)
        self.pushButton.setIcon(icon18)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.gridLayout_13.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageTitle)
        self.pageTranslator = QWidget()
        self.pageTranslator.setObjectName(u"pageTranslator")
        self.gridLayout_56 = QGridLayout(self.pageTranslator)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_55, 1, 2, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 379, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_56.addItem(self.verticalSpacer_32, 2, 1, 1, 1)

        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_94 = QLabel(self.pageTranslator)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(50, 50))
        self.label_94.setMaximumSize(QSize(50, 50))
        self.label_94.setPixmap(QPixmap(u":/icon/icon/education.png"))
        self.label_94.setScaledContents(True)
        self.label_94.setWordWrap(False)

        self.horizontalLayout_27.addWidget(self.label_94)

        self.label_9 = QLabel(self.pageTranslator)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_27.addWidget(self.label_9)


        self.gridLayout_55.addLayout(self.horizontalLayout_27, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.pageTranslator)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.gridLayout_55.addWidget(self.comboBox, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.pageTranslator)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_55.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.pageTranslator)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_55.addWidget(self.textEdit, 2, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.pageTranslator)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_55.addWidget(self.textEdit_2, 2, 1, 1, 1)


        self.gridLayout_56.addLayout(self.gridLayout_55, 1, 1, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_56, 1, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_56.addItem(self.verticalSpacer_33, 0, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.pageTranslator)
        self.pageIncome = QWidget()
        self.pageIncome.setObjectName(u"pageIncome")
        self.gridLayout_17 = QGridLayout(self.pageIncome)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tableIncome = QTableView(self.pageIncome)
        self.tableIncome.setObjectName(u"tableIncome")

        self.gridLayout_17.addWidget(self.tableIncome, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.pageIncome)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.widget_8)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMargin(5)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMargin(5)

        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)

        self.totalIncomeEdit = QLineEdit(self.widget_8)
        self.totalIncomeEdit.setObjectName(u"totalIncomeEdit")
        sizePolicy2.setHeightForWidth(self.totalIncomeEdit.sizePolicy().hasHeightForWidth())
        self.totalIncomeEdit.setSizePolicy(sizePolicy2)
        self.totalIncomeEdit.setMinimumSize(QSize(540, 0))
        self.totalIncomeEdit.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_3.addWidget(self.totalIncomeEdit, 2, 2, 1, 1)

        self.crewComboBox = QComboBox(self.widget_8)
        self.crewComboBox.setObjectName(u"crewComboBox")
        sizePolicy2.setHeightForWidth(self.crewComboBox.sizePolicy().hasHeightForWidth())
        self.crewComboBox.setSizePolicy(sizePolicy2)
        self.crewComboBox.setMinimumSize(QSize(540, 0))
        self.crewComboBox.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_3.addWidget(self.crewComboBox, 2, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 2, 1, 1, 1)


        self.gridLayout_17.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.pageIncome)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(855, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)

        self.incomeDeleteBtn = QPushButton(self.widget_9)
        self.incomeDeleteBtn.setObjectName(u"incomeDeleteBtn")
        self.incomeDeleteBtn.setMinimumSize(QSize(140, 30))
        self.incomeDeleteBtn.setMaximumSize(QSize(140, 30))
        self.incomeDeleteBtn.setIcon(icon16)
        self.incomeDeleteBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.incomeDeleteBtn)

        self.incomeAddBtn = QPushButton(self.widget_9)
        self.incomeAddBtn.setObjectName(u"incomeAddBtn")
        self.incomeAddBtn.setMinimumSize(QSize(140, 30))
        self.incomeAddBtn.setMaximumSize(QSize(140, 30))
        self.incomeAddBtn.setIcon(icon14)
        self.incomeAddBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.incomeAddBtn)


        self.gridLayout_17.addWidget(self.widget_9, 2, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageIncome)
        self.pageDesc = QWidget()
        self.pageDesc.setObjectName(u"pageDesc")
        self.gridLayout_14 = QGridLayout(self.pageDesc)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.photoDesc = QLabel(self.pageDesc)
        self.photoDesc.setObjectName(u"photoDesc")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.photoDesc.sizePolicy().hasHeightForWidth())
        self.photoDesc.setSizePolicy(sizePolicy5)
        self.photoDesc.setMinimumSize(QSize(193, 265))
        self.photoDesc.setMaximumSize(QSize(250, 380))
        self.photoDesc.setAcceptDrops(False)
        self.photoDesc.setLayoutDirection(Qt.LeftToRight)
        self.photoDesc.setPixmap(QPixmap(u":/Photo/Photo/EyX_7safWuU.jpg"))
        self.photoDesc.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.photoDesc, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.textEditDesc = QTextEdit(self.pageDesc)
        self.textEditDesc.setObjectName(u"textEditDesc")

        self.horizontalLayout_7.addWidget(self.textEditDesc)


        self.gridLayout_14.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_13, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.pageDesc)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy6)
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(949, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.backBtnDesc = QPushButton(self.widget_5)
        self.backBtnDesc.setObjectName(u"backBtnDesc")
        self.backBtnDesc.setMinimumSize(QSize(140, 30))
        self.backBtnDesc.setMaximumSize(QSize(140, 30))
        icon19 = QIcon()
        icon19.addFile(u":/icon/icon/free-icon-back-2644908.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtnDesc.setIcon(icon19)
        self.backBtnDesc.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.backBtnDesc)


        self.gridLayout_14.addWidget(self.widget_5, 2, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageDesc)
        self.pageSchedule = QWidget()
        self.pageSchedule.setObjectName(u"pageSchedule")
        self.gridLayout_20 = QGridLayout(self.pageSchedule)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget_14 = QWidget(self.pageSchedule)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_4 = QGridLayout(self.widget_14)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.gridLayout_21 = QGridLayout(self.widget_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_18 = QLabel(self.widget_15)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.gridLayout_21.addWidget(self.label_18, 0, 0, 1, 1)

        self.comboBoxMonth = QComboBox(self.widget_15)
        self.comboBoxMonth.setObjectName(u"comboBoxMonth")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.comboBoxMonth.sizePolicy().hasHeightForWidth())
        self.comboBoxMonth.setSizePolicy(sizePolicy7)
        self.comboBoxMonth.setMinimumSize(QSize(0, 0))
        self.comboBoxMonth.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_21.addWidget(self.comboBoxMonth, 1, 0, 1, 1)

        self.comboBoxYear = QComboBox(self.widget_15)
        self.comboBoxYear.setObjectName(u"comboBoxYear")
        sizePolicy7.setHeightForWidth(self.comboBoxYear.sizePolicy().hasHeightForWidth())
        self.comboBoxYear.setSizePolicy(sizePolicy7)
        self.comboBoxYear.setMinimumSize(QSize(0, 0))
        self.comboBoxYear.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_21.addWidget(self.comboBoxYear, 1, 2, 1, 1)

        self.label_21 = QLabel(self.widget_15)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)

        self.gridLayout_21.addWidget(self.label_21, 0, 2, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_24, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_15, 0, 0, 1, 2)

        self.widgetCalender = QWidget(self.widget_14)
        self.widgetCalender.setObjectName(u"widgetCalender")
        sizePolicy7.setHeightForWidth(self.widgetCalender.sizePolicy().hasHeightForWidth())
        self.widgetCalender.setSizePolicy(sizePolicy7)
        self.gridLayout_22 = QGridLayout(self.widgetCalender)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.widgetCalender, 1, 0, 1, 2)


        self.gridLayout_20.addWidget(self.widget_14, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageSchedule)
        self.pageAddTitle = QWidget()
        self.pageAddTitle.setObjectName(u"pageAddTitle")
        self.gridLayout_15 = QGridLayout(self.pageAddTitle)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_13 = QSpacerItem(540, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(540, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_14, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_30 = QLabel(self.pageAddTitle)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_14.addWidget(self.label_30)

        self.imageArea = QTextEdit(self.pageAddTitle)
        self.imageArea.setObjectName(u"imageArea")

        self.verticalLayout_14.addWidget(self.imageArea)

        self.label_31 = QLabel(self.pageAddTitle)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_14.addWidget(self.label_31)

        self.nameAddTitle = QLineEdit(self.pageAddTitle)
        self.nameAddTitle.setObjectName(u"nameAddTitle")

        self.verticalLayout_14.addWidget(self.nameAddTitle)

        self.label_32 = QLabel(self.pageAddTitle)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_14.addWidget(self.label_32)

        self.nameCrewTranslatorAddTitle = QComboBox(self.pageAddTitle)
        self.nameCrewTranslatorAddTitle.setObjectName(u"nameCrewTranslatorAddTitle")

        self.verticalLayout_14.addWidget(self.nameCrewTranslatorAddTitle)

        self.label_33 = QLabel(self.pageAddTitle)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_14.addWidget(self.label_33)

        self.translatorsAddTitle = QLineEdit(self.pageAddTitle)
        self.translatorsAddTitle.setObjectName(u"translatorsAddTitle")

        self.verticalLayout_14.addWidget(self.translatorsAddTitle)

        self.label_34 = QLabel(self.pageAddTitle)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_14.addWidget(self.label_34)

        self.dateReleaseAddTitle = QDateEdit(self.pageAddTitle)
        self.dateReleaseAddTitle.setObjectName(u"dateReleaseAddTitle")

        self.verticalLayout_14.addWidget(self.dateReleaseAddTitle)


        self.gridLayout_15.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.pageAddTitle)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QSize(0, 40))
        self.widget_6.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(809, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.backAddTitleBtn = QPushButton(self.widget_6)
        self.backAddTitleBtn.setObjectName(u"backAddTitleBtn")
        self.backAddTitleBtn.setMinimumSize(QSize(140, 30))
        self.backAddTitleBtn.setMaximumSize(QSize(140, 30))
        self.backAddTitleBtn.setIcon(icon19)
        self.backAddTitleBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.backAddTitleBtn)

        self.addTitleBtn = QPushButton(self.widget_6)
        self.addTitleBtn.setObjectName(u"addTitleBtn")
        self.addTitleBtn.setMinimumSize(QSize(140, 30))
        self.addTitleBtn.setMaximumSize(QSize(140, 30))
        self.addTitleBtn.setIcon(icon14)
        self.addTitleBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.addTitleBtn)


        self.gridLayout_15.addWidget(self.widget_6, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageAddTitle)
        self.pageEditTitle = QWidget()
        self.pageEditTitle.setObjectName(u"pageEditTitle")
        self.gridLayout_16 = QGridLayout(self.pageEditTitle)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_40 = QLabel(self.pageEditTitle)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_16.addWidget(self.label_40)

        self.imageAreaEdit = QTextEdit(self.pageEditTitle)
        self.imageAreaEdit.setObjectName(u"imageAreaEdit")

        self.verticalLayout_16.addWidget(self.imageAreaEdit)

        self.label_41 = QLabel(self.pageEditTitle)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_16.addWidget(self.label_41)

        self.nameEditTitle = QLineEdit(self.pageEditTitle)
        self.nameEditTitle.setObjectName(u"nameEditTitle")

        self.verticalLayout_16.addWidget(self.nameEditTitle)

        self.label_42 = QLabel(self.pageEditTitle)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_16.addWidget(self.label_42)

        self.nameCrewTranslatorEditTitle = QComboBox(self.pageEditTitle)
        self.nameCrewTranslatorEditTitle.setObjectName(u"nameCrewTranslatorEditTitle")

        self.verticalLayout_16.addWidget(self.nameCrewTranslatorEditTitle)

        self.label_43 = QLabel(self.pageEditTitle)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_16.addWidget(self.label_43)

        self.translatorsEditTitle = QLineEdit(self.pageEditTitle)
        self.translatorsEditTitle.setObjectName(u"translatorsEditTitle")

        self.verticalLayout_16.addWidget(self.translatorsEditTitle)

        self.label_44 = QLabel(self.pageEditTitle)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_16.addWidget(self.label_44)

        self.dateReleaseEditTitle = QDateEdit(self.pageEditTitle)
        self.dateReleaseEditTitle.setObjectName(u"dateReleaseEditTitle")

        self.verticalLayout_16.addWidget(self.dateReleaseEditTitle)


        self.gridLayout_16.addLayout(self.verticalLayout_16, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(540, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(540, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_15, 1, 0, 1, 1)

        self.widget_7 = QWidget(self.pageEditTitle)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QSize(0, 40))
        self.widget_7.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(809, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.backEditTitleBtn = QPushButton(self.widget_7)
        self.backEditTitleBtn.setObjectName(u"backEditTitleBtn")
        self.backEditTitleBtn.setMinimumSize(QSize(140, 30))
        self.backEditTitleBtn.setMaximumSize(QSize(140, 30))
        self.backEditTitleBtn.setIcon(icon19)
        self.backEditTitleBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.backEditTitleBtn)

        self.applyEditBtn = QPushButton(self.widget_7)
        self.applyEditBtn.setObjectName(u"applyEditBtn")
        self.applyEditBtn.setMinimumSize(QSize(140, 30))
        self.applyEditBtn.setMaximumSize(QSize(140, 30))
        icon20 = QIcon()
        icon20.addFile(u":/icon/icon/free-icon-check-mark-8370918.png", QSize(), QIcon.Normal, QIcon.Off)
        self.applyEditBtn.setIcon(icon20)
        self.applyEditBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.applyEditBtn)


        self.gridLayout_16.addWidget(self.widget_7, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageEditTitle)
        self.pageSocialNetwork = QWidget()
        self.pageSocialNetwork.setObjectName(u"pageSocialNetwork")
        self.gridLayout_46 = QGridLayout(self.pageSocialNetwork)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.pageSocialNetwork)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.postEdit = QTextEdit(self.pageSocialNetwork)
        self.postEdit.setObjectName(u"postEdit")
        self.postEdit.setMinimumSize(QSize(0, 270))
        self.postEdit.setMaximumSize(QSize(16777215, 270))

        self.verticalLayout_10.addWidget(self.postEdit)

        self.label_85 = QLabel(self.pageSocialNetwork)
        self.label_85.setObjectName(u"label_85")

        self.verticalLayout_10.addWidget(self.label_85)

        self.imagePost = QTextEdit(self.pageSocialNetwork)
        self.imagePost.setObjectName(u"imagePost")
        self.imagePost.setMinimumSize(QSize(600, 250))
        self.imagePost.setMaximumSize(QSize(600, 250))

        self.verticalLayout_10.addWidget(self.imagePost)

        self.widget_28 = QWidget(self.pageSocialNetwork)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout_5 = QGridLayout(self.widget_28)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.vkBtn = QPushButton(self.widget_28)
        self.vkBtn.setObjectName(u"vkBtn")
        self.vkBtn.setMinimumSize(QSize(70, 60))
        self.vkBtn.setMaximumSize(QSize(70, 60))
        icon21 = QIcon()
        icon21.addFile(u":/icon/icon/icons8-vk-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vkBtn.setIcon(icon21)
        self.vkBtn.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.vkBtn, 0, 1, 1, 1)

        self.dsBtn = QPushButton(self.widget_28)
        self.dsBtn.setObjectName(u"dsBtn")
        self.dsBtn.setMinimumSize(QSize(70, 60))
        self.dsBtn.setMaximumSize(QSize(70, 60))
        icon22 = QIcon()
        icon22.addFile(u":/icon/icon/icons8-discord-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dsBtn.setIcon(icon22)
        self.dsBtn.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.dsBtn, 0, 2, 1, 1)

        self.tgBtn = QPushButton(self.widget_28)
        self.tgBtn.setObjectName(u"tgBtn")
        self.tgBtn.setMinimumSize(QSize(70, 60))
        self.tgBtn.setMaximumSize(QSize(70, 60))
        icon23 = QIcon()
        icon23.addFile(u":/icon/icon/icons8-\u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tgBtn.setIcon(icon23)
        self.tgBtn.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.tgBtn, 0, 0, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_46, 0, 3, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_28)


        self.gridLayout_46.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_45, 0, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 122, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_46.addItem(self.verticalSpacer_28, 1, 0, 1, 1)

        self.widget_29 = QWidget(self.pageSocialNetwork)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_45 = QGridLayout(self.widget_29)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_44 = QSpacerItem(995, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_45.addItem(self.horizontalSpacer_44, 0, 0, 1, 1)

        self.publishBtn = QPushButton(self.widget_29)
        self.publishBtn.setObjectName(u"publishBtn")
        self.publishBtn.setMinimumSize(QSize(140, 30))
        self.publishBtn.setMaximumSize(QSize(140, 30))
        self.publishBtn.setIcon(icon20)
        self.publishBtn.setIconSize(QSize(20, 20))

        self.gridLayout_45.addWidget(self.publishBtn, 0, 1, 1, 1)


        self.gridLayout_46.addWidget(self.widget_29, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageSocialNetwork)
        self.pageAddIncome = QWidget()
        self.pageAddIncome.setObjectName(u"pageAddIncome")
        self.gridLayout_18 = QGridLayout(self.pageAddIncome)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_45 = QLabel(self.pageAddIncome)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_17.addWidget(self.label_45)

        self.crewAddComboBox = QComboBox(self.pageAddIncome)
        self.crewAddComboBox.setObjectName(u"crewAddComboBox")

        self.verticalLayout_17.addWidget(self.crewAddComboBox)

        self.label_46 = QLabel(self.pageAddIncome)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_17.addWidget(self.label_46)

        self.titleAddComboBox = QComboBox(self.pageAddIncome)
        self.titleAddComboBox.setObjectName(u"titleAddComboBox")

        self.verticalLayout_17.addWidget(self.titleAddComboBox)

        self.label_47 = QLabel(self.pageAddIncome)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_17.addWidget(self.label_47)

        self.nameChapterAddIncome = QLineEdit(self.pageAddIncome)
        self.nameChapterAddIncome.setObjectName(u"nameChapterAddIncome")

        self.verticalLayout_17.addWidget(self.nameChapterAddIncome)

        self.label_48 = QLabel(self.pageAddIncome)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_17.addWidget(self.label_48)

        self.translatorAddIncome = QLineEdit(self.pageAddIncome)
        self.translatorAddIncome.setObjectName(u"translatorAddIncome")

        self.verticalLayout_17.addWidget(self.translatorAddIncome)

        self.label_49 = QLabel(self.pageAddIncome)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_17.addWidget(self.label_49)

        self.salaryAddIncome = QLineEdit(self.pageAddIncome)
        self.salaryAddIncome.setObjectName(u"salaryAddIncome")

        self.verticalLayout_17.addWidget(self.salaryAddIncome)


        self.gridLayout_18.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(563, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_20, 0, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(540, 505, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_16, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.pageAddIncome)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setMinimumSize(QSize(0, 40))
        self.widget_10.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(809, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)

        self.backAddIncome = QPushButton(self.widget_10)
        self.backAddIncome.setObjectName(u"backAddIncome")
        self.backAddIncome.setMinimumSize(QSize(140, 30))
        self.backAddIncome.setMaximumSize(QSize(140, 30))
        self.backAddIncome.setIcon(icon19)
        self.backAddIncome.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.backAddIncome)

        self.addIncomeBtn = QPushButton(self.widget_10)
        self.addIncomeBtn.setObjectName(u"addIncomeBtn")
        self.addIncomeBtn.setMinimumSize(QSize(140, 30))
        self.addIncomeBtn.setMaximumSize(QSize(140, 30))
        self.addIncomeBtn.setIcon(icon14)
        self.addIncomeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.addIncomeBtn)


        self.gridLayout_18.addWidget(self.widget_10, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageAddIncome)
        self.pageEditIncome = QWidget()
        self.pageEditIncome.setObjectName(u"pageEditIncome")
        self.gridLayout_19 = QGridLayout(self.pageEditIncome)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_50 = QLabel(self.pageEditIncome)
        self.label_50.setObjectName(u"label_50")

        self.verticalLayout_18.addWidget(self.label_50)

        self.crewEditComboBox = QComboBox(self.pageEditIncome)
        self.crewEditComboBox.setObjectName(u"crewEditComboBox")

        self.verticalLayout_18.addWidget(self.crewEditComboBox)

        self.label_51 = QLabel(self.pageEditIncome)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_18.addWidget(self.label_51)

        self.titleEditComboBox = QComboBox(self.pageEditIncome)
        self.titleEditComboBox.setObjectName(u"titleEditComboBox")

        self.verticalLayout_18.addWidget(self.titleEditComboBox)

        self.label_52 = QLabel(self.pageEditIncome)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_18.addWidget(self.label_52)

        self.nameChapterEditIncome = QLineEdit(self.pageEditIncome)
        self.nameChapterEditIncome.setObjectName(u"nameChapterEditIncome")

        self.verticalLayout_18.addWidget(self.nameChapterEditIncome)

        self.label_53 = QLabel(self.pageEditIncome)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_18.addWidget(self.label_53)

        self.translatorEditIncome = QLineEdit(self.pageEditIncome)
        self.translatorEditIncome.setObjectName(u"translatorEditIncome")

        self.verticalLayout_18.addWidget(self.translatorEditIncome)

        self.label_54 = QLabel(self.pageEditIncome)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_18.addWidget(self.label_54)

        self.salaryEditIncome = QLineEdit(self.pageEditIncome)
        self.salaryEditIncome.setObjectName(u"salaryEditIncome")

        self.verticalLayout_18.addWidget(self.salaryEditIncome)


        self.gridLayout_19.addLayout(self.verticalLayout_18, 0, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(563, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_22, 0, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(540, 505, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_17, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.pageEditIncome)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMinimumSize(QSize(0, 40))
        self.widget_11.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_21 = QSpacerItem(809, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_21)

        self.backEditIncome = QPushButton(self.widget_11)
        self.backEditIncome.setObjectName(u"backEditIncome")
        self.backEditIncome.setMinimumSize(QSize(140, 30))
        self.backEditIncome.setMaximumSize(QSize(140, 30))
        self.backEditIncome.setIcon(icon19)
        self.backEditIncome.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.backEditIncome)

        self.editIncomeBtn = QPushButton(self.widget_11)
        self.editIncomeBtn.setObjectName(u"editIncomeBtn")
        self.editIncomeBtn.setMinimumSize(QSize(140, 30))
        self.editIncomeBtn.setMaximumSize(QSize(140, 30))
        self.editIncomeBtn.setIcon(icon20)
        self.editIncomeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.editIncomeBtn)


        self.gridLayout_19.addWidget(self.widget_11, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageEditIncome)
        self.pageFileSharing = QWidget()
        self.pageFileSharing.setObjectName(u"pageFileSharing")
        self.gridLayout_50 = QGridLayout(self.pageFileSharing)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_89 = QLabel(self.pageFileSharing)
        self.label_89.setObjectName(u"label_89")
        sizePolicy7.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy7)

        self.verticalLayout_27.addWidget(self.label_89)

        self.fileAdd = QTextEdit(self.pageFileSharing)
        self.fileAdd.setObjectName(u"fileAdd")
        sizePolicy7.setHeightForWidth(self.fileAdd.sizePolicy().hasHeightForWidth())
        self.fileAdd.setSizePolicy(sizePolicy7)
        self.fileAdd.setMinimumSize(QSize(1000, 270))
        self.fileAdd.setMaximumSize(QSize(16777215, 270))

        self.verticalLayout_27.addWidget(self.fileAdd)

        self.label_90 = QLabel(self.pageFileSharing)
        self.label_90.setObjectName(u"label_90")
        sizePolicy7.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy7)

        self.verticalLayout_27.addWidget(self.label_90)

        self.recipientFile = QComboBox(self.pageFileSharing)
        self.recipientFile.setObjectName(u"recipientFile")
        sizePolicy7.setHeightForWidth(self.recipientFile.sizePolicy().hasHeightForWidth())
        self.recipientFile.setSizePolicy(sizePolicy7)
        self.recipientFile.setMinimumSize(QSize(540, 0))
        self.recipientFile.setMaximumSize(QSize(540, 16777215))

        self.verticalLayout_27.addWidget(self.recipientFile)


        self.gridLayout_50.addLayout(self.verticalLayout_27, 0, 0, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_29, 1, 0, 1, 1)

        self.widget_30 = QWidget(self.pageFileSharing)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy)
        self.widget_30.setMinimumSize(QSize(0, 40))
        self.widget_30.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_48 = QGridLayout(self.widget_30)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_48 = QSpacerItem(995, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_48, 0, 0, 1, 1)

        self.sendFile = QPushButton(self.widget_30)
        self.sendFile.setObjectName(u"sendFile")
        self.sendFile.setMinimumSize(QSize(140, 30))
        self.sendFile.setMaximumSize(QSize(140, 30))
        icon24 = QIcon()
        icon24.addFile(u":/icon/icon/free-icon-send-9351602.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendFile.setIcon(icon24)
        self.sendFile.setIconSize(QSize(20, 20))

        self.gridLayout_48.addWidget(self.sendFile, 0, 1, 1, 1)


        self.gridLayout_50.addWidget(self.widget_30, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageFileSharing)
        self.pageAccount = QWidget()
        self.pageAccount.setObjectName(u"pageAccount")
        self.gridLayout_52 = QGridLayout(self.pageAccount)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.widget_34 = QWidget(self.pageAccount)
        self.widget_34.setObjectName(u"widget_34")
        self.gridLayout_51 = QGridLayout(self.widget_34)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.widget_35 = QWidget(self.widget_34)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.widget_35)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_26.addWidget(self.label_93)

        self.horizontalSpacer_52 = QSpacerItem(700, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_52)

        self.addTitleTeamBtn = QPushButton(self.widget_35)
        self.addTitleTeamBtn.setObjectName(u"addTitleTeamBtn")
        self.addTitleTeamBtn.setMinimumSize(QSize(140, 30))
        self.addTitleTeamBtn.setMaximumSize(QSize(140, 30))
        self.addTitleTeamBtn.setIcon(icon14)
        self.addTitleTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_26.addWidget(self.addTitleTeamBtn)

        self.deleteTitleTeamBtn = QPushButton(self.widget_35)
        self.deleteTitleTeamBtn.setObjectName(u"deleteTitleTeamBtn")
        self.deleteTitleTeamBtn.setMinimumSize(QSize(140, 30))
        self.deleteTitleTeamBtn.setMaximumSize(QSize(140, 30))
        self.deleteTitleTeamBtn.setIcon(icon16)
        self.deleteTitleTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_26.addWidget(self.deleteTitleTeamBtn)

        self.saveTitleTeamBtn = QPushButton(self.widget_35)
        self.saveTitleTeamBtn.setObjectName(u"saveTitleTeamBtn")
        self.saveTitleTeamBtn.setMinimumSize(QSize(140, 30))
        self.saveTitleTeamBtn.setMaximumSize(QSize(140, 30))
        self.saveTitleTeamBtn.setIcon(icon20)
        self.saveTitleTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_26.addWidget(self.saveTitleTeamBtn)


        self.gridLayout_51.addWidget(self.widget_35, 0, 0, 1, 1)

        self.tableTitleAcc = QTableView(self.widget_34)
        self.tableTitleAcc.setObjectName(u"tableTitleAcc")

        self.gridLayout_51.addWidget(self.tableTitleAcc, 1, 0, 1, 1)


        self.gridLayout_52.addWidget(self.widget_34, 9, 0, 1, 2)

        self.nameCrewAcc = QLineEdit(self.pageAccount)
        self.nameCrewAcc.setObjectName(u"nameCrewAcc")
        self.nameCrewAcc.setMinimumSize(QSize(540, 0))
        self.nameCrewAcc.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_52.addWidget(self.nameCrewAcc, 2, 0, 1, 2)

        self.label_91 = QLabel(self.pageAccount)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_52.addWidget(self.label_91, 1, 0, 1, 1)

        self.imageCrewAcc = QTextEdit(self.pageAccount)
        self.imageCrewAcc.setObjectName(u"imageCrewAcc")
        self.imageCrewAcc.setMinimumSize(QSize(540, 0))
        self.imageCrewAcc.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_52.addWidget(self.imageCrewAcc, 4, 0, 1, 2)

        self.label_92 = QLabel(self.pageAccount)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_52.addWidget(self.label_92, 3, 0, 1, 1)

        self.userNameAcc = QLabel(self.pageAccount)
        self.userNameAcc.setObjectName(u"userNameAcc")

        self.gridLayout_52.addWidget(self.userNameAcc, 0, 0, 1, 2)

        self.widget_32 = QWidget(self.pageAccount)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_7 = QGridLayout(self.widget_32)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_33)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_25.addWidget(self.label_8)

        self.horizontalSpacer_51 = QSpacerItem(691, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_51)

        self.addTeamBtn = QPushButton(self.widget_33)
        self.addTeamBtn.setObjectName(u"addTeamBtn")
        self.addTeamBtn.setMinimumSize(QSize(140, 30))
        self.addTeamBtn.setMaximumSize(QSize(140, 30))
        self.addTeamBtn.setIcon(icon14)
        self.addTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.addTeamBtn)

        self.deleteTeamBtn = QPushButton(self.widget_33)
        self.deleteTeamBtn.setObjectName(u"deleteTeamBtn")
        self.deleteTeamBtn.setMinimumSize(QSize(140, 30))
        self.deleteTeamBtn.setMaximumSize(QSize(140, 30))
        self.deleteTeamBtn.setIcon(icon16)
        self.deleteTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.deleteTeamBtn)

        self.saveTeamBtn = QPushButton(self.widget_33)
        self.saveTeamBtn.setObjectName(u"saveTeamBtn")
        self.saveTeamBtn.setMinimumSize(QSize(140, 30))
        self.saveTeamBtn.setMaximumSize(QSize(140, 30))
        self.saveTeamBtn.setIcon(icon20)
        self.saveTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.saveTeamBtn)


        self.gridLayout_7.addWidget(self.widget_33, 1, 0, 1, 1)

        self.tableTeamAcc = QTableView(self.widget_32)
        self.tableTeamAcc.setObjectName(u"tableTeamAcc")

        self.gridLayout_7.addWidget(self.tableTeamAcc, 2, 0, 1, 1)


        self.gridLayout_52.addWidget(self.widget_32, 6, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageAccount)
        self.pageAddTask = QWidget()
        self.pageAddTask.setObjectName(u"pageAddTask")
        self.gridLayout_23 = QGridLayout(self.pageAddTask)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_55 = QLabel(self.pageAddTask)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_19.addWidget(self.label_55)

        self.dateLineAddTask = QLineEdit(self.pageAddTask)
        self.dateLineAddTask.setObjectName(u"dateLineAddTask")

        self.verticalLayout_19.addWidget(self.dateLineAddTask)

        self.label_56 = QLabel(self.pageAddTask)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_19.addWidget(self.label_56)

        self.employeeAddTask = QComboBox(self.pageAddTask)
        self.employeeAddTask.setObjectName(u"employeeAddTask")

        self.verticalLayout_19.addWidget(self.employeeAddTask)

        self.label_57 = QLabel(self.pageAddTask)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_19.addWidget(self.label_57)

        self.taskEditAdd = QTextEdit(self.pageAddTask)
        self.taskEditAdd.setObjectName(u"taskEditAdd")

        self.verticalLayout_19.addWidget(self.taskEditAdd)


        self.gridLayout_23.addLayout(self.verticalLayout_19, 0, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(563, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_23, 0, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(540, 422, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_18, 1, 0, 1, 1)

        self.widget_12 = QWidget(self.pageAddTask)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setMinimumSize(QSize(0, 40))
        self.widget_12.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_25 = QSpacerItem(809, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.taskAddBtn = QPushButton(self.widget_12)
        self.taskAddBtn.setObjectName(u"taskAddBtn")
        self.taskAddBtn.setMinimumSize(QSize(140, 30))
        self.taskAddBtn.setMaximumSize(QSize(140, 30))
        self.taskAddBtn.setIcon(icon14)
        self.taskAddBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.taskAddBtn)

        self.backTaskBtn = QPushButton(self.widget_12)
        self.backTaskBtn.setObjectName(u"backTaskBtn")
        self.backTaskBtn.setMinimumSize(QSize(140, 30))
        self.backTaskBtn.setMaximumSize(QSize(140, 30))
        self.backTaskBtn.setIcon(icon19)
        self.backTaskBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.backTaskBtn)


        self.gridLayout_23.addWidget(self.widget_12, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageAddTask)
        self.pageUserPr = QWidget()
        self.pageUserPr.setObjectName(u"pageUserPr")
        self.gridLayout_42 = QGridLayout(self.pageUserPr)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_84 = QLabel(self.pageUserPr)
        self.label_84.setObjectName(u"label_84")

        self.verticalLayout_25.addWidget(self.label_84)

        self.dateLinePrTask = QLineEdit(self.pageUserPr)
        self.dateLinePrTask.setObjectName(u"dateLinePrTask")

        self.verticalLayout_25.addWidget(self.dateLinePrTask)

        self.label_86 = QLabel(self.pageUserPr)
        self.label_86.setObjectName(u"label_86")

        self.verticalLayout_25.addWidget(self.label_86)

        self.taskEditPr = QTextEdit(self.pageUserPr)
        self.taskEditPr.setObjectName(u"taskEditPr")

        self.verticalLayout_25.addWidget(self.taskEditPr)


        self.gridLayout_42.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(563, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_41, 0, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(540, 422, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_42.addItem(self.verticalSpacer_27, 1, 0, 1, 1)

        self.widget_26 = QWidget(self.pageUserPr)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy)
        self.widget_26.setMinimumSize(QSize(0, 40))
        self.widget_26.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_42 = QSpacerItem(809, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_42)

        self.backTaskPrBtn = QPushButton(self.widget_26)
        self.backTaskPrBtn.setObjectName(u"backTaskPrBtn")
        self.backTaskPrBtn.setMinimumSize(QSize(140, 30))
        self.backTaskPrBtn.setMaximumSize(QSize(140, 30))
        self.backTaskPrBtn.setIcon(icon19)
        self.backTaskPrBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.backTaskPrBtn)


        self.gridLayout_42.addWidget(self.widget_26, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageUserPr)
        self.pageAboutUs = QWidget()
        self.pageAboutUs.setObjectName(u"pageAboutUs")
        self.gridLayout_8 = QGridLayout(self.pageAboutUs)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_54, 1, 2, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_30, 0, 1, 1, 1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_53, 1, 0, 1, 1)

        self.widget_37 = QWidget(self.pageAboutUs)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMinimumSize(QSize(0, 40))
        self.gridLayout_54 = QGridLayout(self.widget_37)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setVerticalSpacing(20)
        self.infoLabel = QLabel(self.widget_37)
        self.infoLabel.setObjectName(u"infoLabel")

        self.gridLayout_54.addWidget(self.infoLabel, 0, 0, 1, 1, Qt.AlignHCenter)

        self.plugLabel = QLabel(self.widget_37)
        self.plugLabel.setObjectName(u"plugLabel")

        self.gridLayout_54.addWidget(self.plugLabel, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.widget_37, 1, 1, 1, 1)

        self.widget_36 = QWidget(self.pageAboutUs)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy7.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy7)
        self.gridLayout_53 = QGridLayout(self.widget_36)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.verLabel = QLabel(self.widget_36)
        self.verLabel.setObjectName(u"verLabel")

        self.gridLayout_53.addWidget(self.verLabel, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.widget_36, 3, 1, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_31, 2, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.pageAboutUs)
        self.pageReceiveFile = QWidget()
        self.pageReceiveFile.setObjectName(u"pageReceiveFile")
        self.gridLayout_49 = QGridLayout(self.pageReceiveFile)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_7 = QLabel(self.pageReceiveFile)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_49.addWidget(self.label_7, 0, 0, 1, 1)

        self.tableFiles = QTableView(self.pageReceiveFile)
        self.tableFiles.setObjectName(u"tableFiles")

        self.gridLayout_49.addWidget(self.tableFiles, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageReceiveFile)
        self.pageListTask = QWidget()
        self.pageListTask.setObjectName(u"pageListTask")
        self.gridLayout_44 = QGridLayout(self.pageListTask)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.widget_27 = QWidget(self.pageListTask)
        self.widget_27.setObjectName(u"widget_27")
        self.gridLayout_43 = QGridLayout(self.widget_27)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.deleteListTask = QPushButton(self.widget_27)
        self.deleteListTask.setObjectName(u"deleteListTask")
        self.deleteListTask.setMinimumSize(QSize(140, 30))
        self.deleteListTask.setMaximumSize(QSize(140, 30))
        self.deleteListTask.setIcon(icon16)
        self.deleteListTask.setIconSize(QSize(20, 20))

        self.gridLayout_43.addWidget(self.deleteListTask, 0, 1, 1, 1)

        self.addListTask = QPushButton(self.widget_27)
        self.addListTask.setObjectName(u"addListTask")
        self.addListTask.setMinimumSize(QSize(140, 30))
        self.addListTask.setMaximumSize(QSize(140, 30))
        self.addListTask.setIcon(icon14)
        self.addListTask.setIconSize(QSize(20, 20))

        self.gridLayout_43.addWidget(self.addListTask, 0, 2, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(855, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_43.addItem(self.horizontalSpacer_43, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.widget_27, 0, 0, 1, 1)

        self.tableListTask = QTableView(self.pageListTask)
        self.tableListTask.setObjectName(u"tableListTask")

        self.gridLayout_44.addWidget(self.tableListTask, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageListTask)

        self.gridLayout_10.addWidget(self.stackedWidget_2, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.pageMain)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.openMenuBtn.toggled.connect(self.icon.setVisible)
        self.openMenuBtn.toggled.connect(self.fullMenu.setHidden)
        self.titleBtn_1.toggled.connect(self.titleBtn_2.setChecked)
        self.incomeBtn_1.toggled.connect(self.incomeBtn_2.setChecked)
        self.scheduleBtn_1.toggled.connect(self.scheduleBtn_2.setChecked)
        self.socialNetworksBtn_1.toggled.connect(self.socialNetworksBtn_2.setChecked)
        self.fileSharingBtn_1.toggled.connect(self.fileSharingBtn_2.setChecked)
        self.acceptFileBtn_1.toggled.connect(self.acceptFileBtn_2.setChecked)
        self.accountBtn_1.toggled.connect(self.accountBtn_2.setChecked)
        self.translateBtn_1.toggled.connect(self.translateBtn_2.setChecked)
        self.aboutUs_1.toggled.connect(self.aboutUs_2.setChecked)
        self.aboutUs_2.toggled.connect(self.aboutUs_1.setChecked)
        self.translateBtn_2.toggled.connect(self.translateBtn_1.setChecked)
        self.accountBtn_2.toggled.connect(self.accountBtn_1.setChecked)
        self.acceptFileBtn_2.toggled.connect(self.acceptFileBtn_1.setChecked)
        self.fileSharingBtn_2.toggled.connect(self.fileSharingBtn_1.setChecked)
        self.socialNetworksBtn_2.toggled.connect(self.socialNetworksBtn_1.setChecked)
        self.scheduleBtn_2.toggled.connect(self.scheduleBtn_1.setChecked)
        self.incomeBtn_2.toggled.connect(self.incomeBtn_1.setChecked)
        self.titleBtn_2.toggled.connect(self.titleBtn_1.setChecked)
        self.pushButton.toggled.connect(self.widget_4.setHidden)
        self.pushButton.toggled.connect(self.widget_4.setVisible)

        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimazeBtn.setText("")
        self.expandBtn.setText("")
        self.closeBtn.setText("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.inLogBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.inLogBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.notRegLabel.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0449\u0451 \u043d\u0435 \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u044b?", None))
        self.forgotPasLabel.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.changePasBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.changePasBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.backChangePasBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email", None))
#if QT_CONFIG(tooltip)
        self.nextResBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.nextResBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.backResBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.regBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.regBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.backBtnReg.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.openMenuBtn.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DADA GROUP", None))
        self.titleBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0442\u043b\u044b", None))
        self.incomeBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.scheduleBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.socialNetworksBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0446. \u0441\u0435\u0442\u0438", None))
        self.fileSharingBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043c\u0435\u043d \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.acceptFileBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.accountBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.translateBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
        self.aboutUs_2.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441", None))
        self.label.setText("")
        self.titleBtn_1.setText("")
        self.incomeBtn_1.setText("")
        self.scheduleBtn_1.setText("")
        self.socialNetworksBtn_1.setText("")
        self.fileSharingBtn_1.setText("")
        self.acceptFileBtn_1.setText("")
        self.accountBtn_1.setText("")
        self.translateBtn_1.setText("")
        self.aboutUs_1.setText("")
        self.pushOpenAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushOpenEdit.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushOpenDel.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.SearchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.SearchBtn.setText("")
        self.pushButton.setText("")
        self.label_94.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0435\u0439\u0441\u043a\u0438\u0439", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u042f\u043f\u043e\u043d\u0441\u043a\u0438\u0439", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0435\u0439\u0441\u043a\u0438\u0439", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u042f\u043f\u043e\u043d\u0441\u043a\u0438\u0439", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u0443", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u0434\u043e\u0445\u043e\u0434\u0430", None))
        self.incomeDeleteBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.incomeAddBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.photoDesc.setText("")
        self.textEditDesc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u0430\u0439\u0442\u043b\u0430", None))
        self.backBtnDesc.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0441\u044f\u0446", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0433\u043e\u0434", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.imageArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a\u043e\u0432", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a\u0438", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0445\u043e\u0434\u0430", None))
        self.backAddTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.addTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.imageAreaEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a\u043e\u0432", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a\u0438", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0445\u043e\u0434\u0430", None))
        self.backEditTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.applyEditBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.postEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.imagePost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.vkBtn.setText("")
        self.dsBtn.setText("")
        self.tgBtn.setText("")
        self.publishBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0439\u0442\u043b\u0430", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u043b\u0430\u0432\u044b", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.backAddIncome.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.addIncomeBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0439\u0442\u043b\u0430", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u043b\u0430\u0432\u044b", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.backEditIncome.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.editIncomeBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \".rar\", \".docx\"", None))
        self.fileAdd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \".rar\" \u043d\u0435 \u0434\u043e\u043b\u0436\u0435\u043d \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0442\u044c 4\u0433\u0431, \".docx\" \u043d\u0435 \u0434\u043e\u043b\u0436\u0435\u043d \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0442\u044c 100\u043c\u0431", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f", None))
        self.sendFile.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.addTitleTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteTitleTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.saveTitleTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0430\u0448\u0435\u0439 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.userNameAcc.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u0430\u0432 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.addTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.saveTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0435", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.taskAddBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.backTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.backTaskPrBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u0430 \u043f\u0440\u0438 \u0443\u0447\u0430\u0441\u0442\u0438\u0438 DADA GROUP", None))
        self.plugLabel.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043b\u0443\u0448\u043a\u0430", None))
        self.verLabel.setText(QCoreApplication.translate("MainWindow", u"ver 0.0.1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None))
        self.deleteListTask.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.addListTask.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

