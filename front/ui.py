# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1156, 768))
        MainWindow.setMaximumSize(QSize(3840, 2160))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(10000000, 10000000))
        self.pageLog = QWidget()
        self.pageLog.setObjectName(u"pageLog")
        self.gridLayout_11 = QGridLayout(self.pageLog)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_2)

        self.errorLabel = QLabel(self.pageLog)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.errorLabel)

        self.inLogBtn = QPushButton(self.pageLog)
        self.inLogBtn.setObjectName(u"inLogBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
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
        self.forgotPasLabel.setMinimumSize(QSize(256, 256))
        self.forgotPasLabel.setMaximumSize(QSize(30, 16777215))
        self.forgotPasLabel.setPixmap(QPixmap(u":/icon/icon/YQR.png"))
        self.forgotPasLabel.setScaledContents(False)

        self.verticalLayout_6.addWidget(self.forgotPasLabel, 0, Qt.AlignHCenter)


        self.gridLayout_11.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageLog)
        self.pageChangePas = QWidget()
        self.pageChangePas.setObjectName(u"pageChangePas")
        self.gridLayout_12 = QGridLayout(self.pageChangePas)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalSpacer_10 = QSpacerItem(20, 242, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(433, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.horizontalSpacer_11 = QSpacerItem(433, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 242, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageChangePas)
        self.pageResPas = QWidget()
        self.pageResPas.setObjectName(u"pageResPas")
        self.gridLayout_9 = QGridLayout(self.pageResPas)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_8 = QSpacerItem(20, 262, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(433, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.horizontalSpacer_8 = QSpacerItem(433, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 261, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageResPas)
        self.pageReg = QWidget()
        self.pageReg.setObjectName(u"pageReg")
        self.gridLayout = QGridLayout(self.pageReg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.pageReg)
        self.pageMain = QWidget()
        self.pageMain.setObjectName(u"pageMain")
        self.pageMain.setEnabled(True)
        self.gridLayout_10 = QGridLayout(self.pageMain)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleBtn_2 = QPushButton(self.fullMenu)
        self.titleBtn_2.setObjectName(u"titleBtn_2")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/free-icon-book-9193009.png", QSize(), QIcon.Normal, QIcon.Off)
        self.titleBtn_2.setIcon(icon4)
        self.titleBtn_2.setIconSize(QSize(20, 20))
        self.titleBtn_2.setCheckable(True)
        self.titleBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.titleBtn_2)

        self.incomeBtn_2 = QPushButton(self.fullMenu)
        self.incomeBtn_2.setObjectName(u"incomeBtn_2")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/free-icon-coin-550650.png", QSize(), QIcon.Normal, QIcon.Off)
        self.incomeBtn_2.setIcon(icon5)
        self.incomeBtn_2.setIconSize(QSize(20, 20))
        self.incomeBtn_2.setCheckable(True)
        self.incomeBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.incomeBtn_2)

        self.scheduleBtn_2 = QPushButton(self.fullMenu)
        self.scheduleBtn_2.setObjectName(u"scheduleBtn_2")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/free-icon-clock-2902894.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scheduleBtn_2.setIcon(icon6)
        self.scheduleBtn_2.setIconSize(QSize(20, 20))
        self.scheduleBtn_2.setCheckable(True)
        self.scheduleBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.scheduleBtn_2)

        self.socialNetworksBtn_2 = QPushButton(self.fullMenu)
        self.socialNetworksBtn_2.setObjectName(u"socialNetworksBtn_2")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/free-icon-social-media-9351311.png", QSize(), QIcon.Normal, QIcon.Off)
        self.socialNetworksBtn_2.setIcon(icon7)
        self.socialNetworksBtn_2.setIconSize(QSize(20, 20))
        self.socialNetworksBtn_2.setCheckable(True)
        self.socialNetworksBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.socialNetworksBtn_2)

        self.fileSharingBtn_2 = QPushButton(self.fullMenu)
        self.fileSharingBtn_2.setObjectName(u"fileSharingBtn_2")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/free-icon-file-sharing-10004135.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileSharingBtn_2.setIcon(icon8)
        self.fileSharingBtn_2.setIconSize(QSize(20, 20))
        self.fileSharingBtn_2.setCheckable(True)
        self.fileSharingBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fileSharingBtn_2)

        self.accountBtn_2 = QPushButton(self.fullMenu)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn_2.setIcon(icon9)
        self.accountBtn_2.setIconSize(QSize(20, 20))
        self.accountBtn_2.setCheckable(True)
        self.accountBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.accountBtn_2)

        self.translateBtn_2 = QPushButton(self.fullMenu)
        self.translateBtn_2.setObjectName(u"translateBtn_2")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/education.png", QSize(), QIcon.Normal, QIcon.Off)
        self.translateBtn_2.setIcon(icon10)
        self.translateBtn_2.setIconSize(QSize(20, 20))
        self.translateBtn_2.setCheckable(True)
        self.translateBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.translateBtn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 382, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitAppBtn_2 = QPushButton(self.fullMenu)
        self.exitAppBtn_2.setObjectName(u"exitAppBtn_2")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitAppBtn_2.setIcon(icon11)
        self.exitAppBtn_2.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.exitAppBtn_2)


        self.gridLayout_10.addWidget(self.fullMenu, 0, 1, 3, 1)

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
        icon12 = QIcon()
        icon12.addFile(u":/icon/icon/free-icon-chevron-248744.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icon/icon/rev.png", QSize(), QIcon.Active, QIcon.On)
        icon12.addFile(u":/icon/icon/free-icon-chevron-248744.png", QSize(), QIcon.Selected, QIcon.On)
        self.openMenuBtn.setIcon(icon12)
        self.openMenuBtn.setIconSize(QSize(20, 20))
        self.openMenuBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.openMenuBtn)

        self.horizontalSpacer_3 = QSpacerItem(742, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout_10.addWidget(self.widget, 0, 2, 1, 1)

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
        self.titleBtn_1.setIcon(icon4)
        self.titleBtn_1.setIconSize(QSize(20, 20))
        self.titleBtn_1.setCheckable(True)
        self.titleBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.titleBtn_1)

        self.incomeBtn_1 = QPushButton(self.icon)
        self.incomeBtn_1.setObjectName(u"incomeBtn_1")
        self.incomeBtn_1.setIcon(icon5)
        self.incomeBtn_1.setIconSize(QSize(20, 20))
        self.incomeBtn_1.setCheckable(True)
        self.incomeBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.incomeBtn_1)

        self.scheduleBtn_1 = QPushButton(self.icon)
        self.scheduleBtn_1.setObjectName(u"scheduleBtn_1")
        self.scheduleBtn_1.setIcon(icon6)
        self.scheduleBtn_1.setIconSize(QSize(20, 20))
        self.scheduleBtn_1.setCheckable(True)
        self.scheduleBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.scheduleBtn_1)

        self.socialNetworksBtn_1 = QPushButton(self.icon)
        self.socialNetworksBtn_1.setObjectName(u"socialNetworksBtn_1")
        self.socialNetworksBtn_1.setIcon(icon7)
        self.socialNetworksBtn_1.setIconSize(QSize(20, 20))
        self.socialNetworksBtn_1.setCheckable(True)
        self.socialNetworksBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.socialNetworksBtn_1)

        self.fileSharingBtn_1 = QPushButton(self.icon)
        self.fileSharingBtn_1.setObjectName(u"fileSharingBtn_1")
        self.fileSharingBtn_1.setIcon(icon8)
        self.fileSharingBtn_1.setIconSize(QSize(20, 20))
        self.fileSharingBtn_1.setCheckable(True)
        self.fileSharingBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.fileSharingBtn_1)

        self.accountBtn_1 = QPushButton(self.icon)
        self.accountBtn_1.setObjectName(u"accountBtn_1")
        self.accountBtn_1.setIcon(icon9)
        self.accountBtn_1.setIconSize(QSize(20, 20))
        self.accountBtn_1.setCheckable(True)
        self.accountBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.accountBtn_1)

        self.translateBtn_1 = QPushButton(self.icon)
        self.translateBtn_1.setObjectName(u"translateBtn_1")
        self.translateBtn_1.setIcon(icon10)
        self.translateBtn_1.setIconSize(QSize(20, 20))
        self.translateBtn_1.setCheckable(True)
        self.translateBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.translateBtn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 382, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exitAppBtn = QPushButton(self.icon)
        self.exitAppBtn.setObjectName(u"exitAppBtn")
        self.exitAppBtn.setIcon(icon11)
        self.exitAppBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.exitAppBtn)


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
        self.titleWidget = QWidget(self.pageTitle)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
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
        self.SearchEdit = QLineEdit(self.pageTitle)
        self.SearchEdit.setObjectName(u"SearchEdit")

        self.horizontalLayout_3.addWidget(self.SearchEdit)

        self.SearchBtn = QPushButton(self.pageTitle)
        self.SearchBtn.setObjectName(u"SearchBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icon/icon/free-icon-loupe-216463.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SearchBtn.setIcon(icon13)
        self.SearchBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.SearchBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboboxTitle = QComboBox(self.pageTitle)
        self.comboboxTitle.setObjectName(u"comboboxTitle")
        self.comboboxTitle.setMaximumSize(QSize(540, 16777215))

        self.horizontalLayout_3.addWidget(self.comboboxTitle)

        self.pushOpenAdd = QPushButton(self.pageTitle)
        self.pushOpenAdd.setObjectName(u"pushOpenAdd")
        self.pushOpenAdd.setLayoutDirection(Qt.LeftToRight)
        icon14 = QIcon()
        icon14.addFile(u":/icon/icon/free-icon-add-7222864.png", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/icon/icon/free-icon-add-7222864.png", QSize(), QIcon.Active, QIcon.On)
        self.pushOpenAdd.setIcon(icon14)
        self.pushOpenAdd.setIconSize(QSize(20, 20))
        self.pushOpenAdd.setCheckable(True)
        self.pushOpenAdd.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.pushOpenAdd)


        self.gridLayout_13.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageTitle)
        self.pageEditTask = QWidget()
        self.pageEditTask.setObjectName(u"pageEditTask")
        self.gridLayout_2 = QGridLayout(self.pageEditTask)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_61 = QLabel(self.pageEditTask)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_21.addWidget(self.label_61)

        self.dateEditEditTask = QDateEdit(self.pageEditTask)
        self.dateEditEditTask.setObjectName(u"dateEditEditTask")

        self.verticalLayout_21.addWidget(self.dateEditEditTask)

        self.label_62 = QLabel(self.pageEditTask)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_21.addWidget(self.label_62)

        self.employeeEditTask = QComboBox(self.pageEditTask)
        self.employeeEditTask.setObjectName(u"employeeEditTask")

        self.verticalLayout_21.addWidget(self.employeeEditTask)

        self.label_63 = QLabel(self.pageEditTask)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_21.addWidget(self.label_63)

        self.taskEditChange = QTextEdit(self.pageEditTask)
        self.taskEditChange.setObjectName(u"taskEditChange")

        self.verticalLayout_21.addWidget(self.taskEditChange)


        self.gridLayout_2.addLayout(self.verticalLayout_21, 0, 0, 1, 2)

        self.horizontalSpacer_29 = QSpacerItem(417, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_29, 0, 2, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(540, 422, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_19, 1, 0, 1, 1)

        self.widget_13 = QWidget(self.pageEditTask)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.widget_13.setMinimumSize(QSize(0, 40))
        self.widget_13.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_28 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_28)

        self.taskApplyBtn = QPushButton(self.widget_13)
        self.taskApplyBtn.setObjectName(u"taskApplyBtn")
        self.taskApplyBtn.setMinimumSize(QSize(140, 30))
        self.taskApplyBtn.setMaximumSize(QSize(140, 30))
        icon15 = QIcon()
        icon15.addFile(u":/icon/icon/free-icon-check-mark-8370918.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskApplyBtn.setIcon(icon15)
        self.taskApplyBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_17.addWidget(self.taskApplyBtn)

        self.backApplyTaskBtn = QPushButton(self.widget_13)
        self.backApplyTaskBtn.setObjectName(u"backApplyTaskBtn")
        self.backApplyTaskBtn.setMinimumSize(QSize(140, 30))
        self.backApplyTaskBtn.setMaximumSize(QSize(140, 30))
        icon16 = QIcon()
        icon16.addFile(u":/icon/icon/free-icon-back-2644908.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backApplyTaskBtn.setIcon(icon16)
        self.backApplyTaskBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_17.addWidget(self.backApplyTaskBtn)


        self.gridLayout_2.addWidget(self.widget_13, 3, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.pageEditTask)
        self.pageTranslator = QWidget()
        self.pageTranslator.setObjectName(u"pageTranslator")
        self.gridLayout_56 = QGridLayout(self.pageTranslator)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_55, 1, 2, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 379, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.textEdit_2.setReadOnly(True)

        self.gridLayout_55.addWidget(self.textEdit_2, 2, 1, 1, 1)


        self.gridLayout_56.addLayout(self.gridLayout_55, 1, 1, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_56, 1, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(40, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_56.addItem(self.verticalSpacer_33, 0, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.pageTranslator)
        self.pageIncome = QWidget()
        self.pageIncome.setObjectName(u"pageIncome")
        self.gridLayout_17 = QGridLayout(self.pageIncome)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tableIncome = QTableView(self.pageIncome)
        self.tableIncome.setObjectName(u"tableIncome")
        self.tableIncome.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableIncome.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_17.addWidget(self.tableIncome, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.pageIncome)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_8)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMargin(5)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMargin(5)

        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)

        self.totalIncomeEdit = QLineEdit(self.widget_8)
        self.totalIncomeEdit.setObjectName(u"totalIncomeEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.totalIncomeEdit.sizePolicy().hasHeightForWidth())
        self.totalIncomeEdit.setSizePolicy(sizePolicy5)
        self.totalIncomeEdit.setMinimumSize(QSize(0, 0))
        self.totalIncomeEdit.setMaximumSize(QSize(540, 16777215))
        self.totalIncomeEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.totalIncomeEdit, 2, 2, 1, 1)

        self.crewComboBox = QComboBox(self.widget_8)
        self.crewComboBox.setObjectName(u"crewComboBox")
        sizePolicy5.setHeightForWidth(self.crewComboBox.sizePolicy().hasHeightForWidth())
        self.crewComboBox.setSizePolicy(sizePolicy5)
        self.crewComboBox.setMinimumSize(QSize(0, 0))
        self.crewComboBox.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_3.addWidget(self.crewComboBox, 2, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 2, 1, 1, 1)


        self.gridLayout_17.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.pageIncome)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(855, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)

        self.incomeEditBtn = QPushButton(self.widget_9)
        self.incomeEditBtn.setObjectName(u"incomeEditBtn")
        self.incomeEditBtn.setMinimumSize(QSize(140, 30))
        self.incomeEditBtn.setMaximumSize(QSize(140, 30))
        icon17 = QIcon()
        icon17.addFile(u":/icon/icon/free-icon-pencil-7266923.png", QSize(), QIcon.Normal, QIcon.Off)
        self.incomeEditBtn.setIcon(icon17)

        self.horizontalLayout_10.addWidget(self.incomeEditBtn)

        self.incomeDeleteBtn = QPushButton(self.widget_9)
        self.incomeDeleteBtn.setObjectName(u"incomeDeleteBtn")
        self.incomeDeleteBtn.setMinimumSize(QSize(140, 30))
        self.incomeDeleteBtn.setMaximumSize(QSize(140, 30))
        icon18 = QIcon()
        icon18.addFile(u":/icon/icon/free-icon-minus-button-4315581 \u043a\u043e\u043f\u0438\u044f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.incomeDeleteBtn.setIcon(icon18)
        self.incomeDeleteBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.incomeDeleteBtn)

        self.incomeAddBtn = QPushButton(self.widget_9)
        self.incomeAddBtn.setObjectName(u"incomeAddBtn")
        self.incomeAddBtn.setMinimumSize(QSize(140, 30))
        self.incomeAddBtn.setMaximumSize(QSize(140, 30))
        icon19 = QIcon()
        icon19.addFile(u":/icon/icon/free-icon-add-7222864.png", QSize(), QIcon.Normal, QIcon.Off)
        self.incomeAddBtn.setIcon(icon19)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.photoDesc.sizePolicy().hasHeightForWidth())
        self.photoDesc.setSizePolicy(sizePolicy6)
        self.photoDesc.setMinimumSize(QSize(250, 380))
        self.photoDesc.setMaximumSize(QSize(250, 380))
        self.photoDesc.setAcceptDrops(False)
        self.photoDesc.setLayoutDirection(Qt.LeftToRight)
        self.photoDesc.setPixmap(QPixmap(u":/Photo/Photo/EyX_7safWuU.jpg"))
        self.photoDesc.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.photoDesc, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.textEditDesc = QTextEdit(self.pageDesc)
        self.textEditDesc.setObjectName(u"textEditDesc")
        self.textEditDesc.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.textEditDesc)


        self.gridLayout_14.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_13, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.pageDesc)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy7)
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(949, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.editTitleBtn = QPushButton(self.widget_5)
        self.editTitleBtn.setObjectName(u"editTitleBtn")
        self.editTitleBtn.setMinimumSize(QSize(140, 26))
        self.editTitleBtn.setMaximumSize(QSize(140, 30))
        self.editTitleBtn.setIcon(icon17)

        self.horizontalLayout_8.addWidget(self.editTitleBtn)

        self.deleteTitleBtn = QPushButton(self.widget_5)
        self.deleteTitleBtn.setObjectName(u"deleteTitleBtn")
        self.deleteTitleBtn.setMinimumSize(QSize(140, 30))
        self.deleteTitleBtn.setMaximumSize(QSize(140, 30))
        self.deleteTitleBtn.setIcon(icon18)

        self.horizontalLayout_8.addWidget(self.deleteTitleBtn)

        self.backBtnDesc = QPushButton(self.widget_5)
        self.backBtnDesc.setObjectName(u"backBtnDesc")
        self.backBtnDesc.setMinimumSize(QSize(140, 30))
        self.backBtnDesc.setMaximumSize(QSize(140, 30))
        self.backBtnDesc.setIcon(icon16)
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
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.gridLayout_21 = QGridLayout(self.widget_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_18 = QLabel(self.widget_15)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

        self.gridLayout_21.addWidget(self.label_18, 0, 0, 1, 1)

        self.comboBoxMonth = QComboBox(self.widget_15)
        self.comboBoxMonth.setObjectName(u"comboBoxMonth")
        sizePolicy5.setHeightForWidth(self.comboBoxMonth.sizePolicy().hasHeightForWidth())
        self.comboBoxMonth.setSizePolicy(sizePolicy5)
        self.comboBoxMonth.setMinimumSize(QSize(0, 0))
        self.comboBoxMonth.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_21.addWidget(self.comboBoxMonth, 1, 0, 1, 1)

        self.comboBoxYear = QComboBox(self.widget_15)
        self.comboBoxYear.setObjectName(u"comboBoxYear")
        sizePolicy5.setHeightForWidth(self.comboBoxYear.sizePolicy().hasHeightForWidth())
        self.comboBoxYear.setSizePolicy(sizePolicy5)
        self.comboBoxYear.setMinimumSize(QSize(0, 0))
        self.comboBoxYear.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_21.addWidget(self.comboBoxYear, 1, 2, 1, 1)

        self.label_21 = QLabel(self.widget_15)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)

        self.gridLayout_21.addWidget(self.label_21, 0, 2, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_24, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_15, 0, 0, 1, 2)

        self.widgetCalender = QWidget(self.widget_14)
        self.widgetCalender.setObjectName(u"widgetCalender")
        sizePolicy5.setHeightForWidth(self.widgetCalender.sizePolicy().hasHeightForWidth())
        self.widgetCalender.setSizePolicy(sizePolicy5)
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
        self.verticalSpacer_14 = QSpacerItem(540, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_14, 1, 0, 1, 1)

        self.widget_6 = QWidget(self.pageAddTitle)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(0, 40))
        self.widget_6.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.backAddTitleBtn = QPushButton(self.widget_6)
        self.backAddTitleBtn.setObjectName(u"backAddTitleBtn")
        self.backAddTitleBtn.setMinimumSize(QSize(140, 30))
        self.backAddTitleBtn.setMaximumSize(QSize(140, 30))
        self.backAddTitleBtn.setIcon(icon16)
        self.backAddTitleBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.backAddTitleBtn)

        self.addTitleBtn = QPushButton(self.widget_6)
        self.addTitleBtn.setObjectName(u"addTitleBtn")
        self.addTitleBtn.setMinimumSize(QSize(140, 30))
        self.addTitleBtn.setMaximumSize(QSize(140, 30))
        self.addTitleBtn.setIcon(icon19)
        self.addTitleBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.addTitleBtn)


        self.gridLayout_15.addWidget(self.widget_6, 2, 0, 1, 2)

        self.horizontalSpacer_13 = QSpacerItem(540, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_30 = QLabel(self.pageAddTitle)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_28.addWidget(self.label_30, 0, 0, 1, 1)

        self.imageArea = QTextEdit(self.pageAddTitle)
        self.imageArea.setObjectName(u"imageArea")
        self.imageArea.setReadOnly(True)

        self.gridLayout_28.addWidget(self.imageArea, 1, 0, 1, 1)

        self.label_31 = QLabel(self.pageAddTitle)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_28.addWidget(self.label_31, 2, 0, 1, 1)

        self.nameAddTitle = QLineEdit(self.pageAddTitle)
        self.nameAddTitle.setObjectName(u"nameAddTitle")

        self.gridLayout_28.addWidget(self.nameAddTitle, 3, 0, 1, 1)

        self.label_32 = QLabel(self.pageAddTitle)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_28.addWidget(self.label_32, 4, 0, 1, 1)

        self.nameCrewTranslatorAddTitle = QComboBox(self.pageAddTitle)
        self.nameCrewTranslatorAddTitle.setObjectName(u"nameCrewTranslatorAddTitle")

        self.gridLayout_28.addWidget(self.nameCrewTranslatorAddTitle, 5, 0, 1, 1)

        self.label_33 = QLabel(self.pageAddTitle)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_28.addWidget(self.label_33, 6, 0, 1, 1)

        self.descriptionEdit = QTextEdit(self.pageAddTitle)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.gridLayout_28.addWidget(self.descriptionEdit, 7, 0, 1, 1)

        self.label_34 = QLabel(self.pageAddTitle)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_28.addWidget(self.label_34, 8, 0, 1, 1)

        self.dateReleaseAddTitle = QDateEdit(self.pageAddTitle)
        self.dateReleaseAddTitle.setObjectName(u"dateReleaseAddTitle")
        self.dateReleaseAddTitle.setCalendarPopup(False)
        self.dateReleaseAddTitle.setDate(QDate(2000, 1, 2))

        self.gridLayout_28.addWidget(self.dateReleaseAddTitle, 9, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_28, 0, 0, 1, 1)

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
        self.imageAreaEdit.setReadOnly(True)

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

        self.descriptionEdit_2 = QTextEdit(self.pageEditTitle)
        self.descriptionEdit_2.setObjectName(u"descriptionEdit_2")

        self.verticalLayout_16.addWidget(self.descriptionEdit_2)

        self.label_44 = QLabel(self.pageEditTitle)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_16.addWidget(self.label_44)

        self.dateReleaseEditTitle = QDateEdit(self.pageEditTitle)
        self.dateReleaseEditTitle.setObjectName(u"dateReleaseEditTitle")

        self.verticalLayout_16.addWidget(self.dateReleaseEditTitle)


        self.gridLayout_16.addLayout(self.verticalLayout_16, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(540, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(540, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_15, 1, 0, 1, 1)

        self.widget_7 = QWidget(self.pageEditTitle)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.widget_7.setMinimumSize(QSize(0, 40))
        self.widget_7.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.backEditTitleBtn = QPushButton(self.widget_7)
        self.backEditTitleBtn.setObjectName(u"backEditTitleBtn")
        self.backEditTitleBtn.setMinimumSize(QSize(140, 30))
        self.backEditTitleBtn.setMaximumSize(QSize(140, 30))
        self.backEditTitleBtn.setIcon(icon16)
        self.backEditTitleBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.backEditTitleBtn)

        self.applyEditBtn = QPushButton(self.widget_7)
        self.applyEditBtn.setObjectName(u"applyEditBtn")
        self.applyEditBtn.setMinimumSize(QSize(140, 30))
        self.applyEditBtn.setMaximumSize(QSize(140, 30))
        self.applyEditBtn.setIcon(icon15)
        self.applyEditBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.applyEditBtn)


        self.gridLayout_16.addWidget(self.widget_7, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageEditTitle)
        self.pageSocialNetwork = QWidget()
        self.pageSocialNetwork.setObjectName(u"pageSocialNetwork")
        self.gridLayout_46 = QGridLayout(self.pageSocialNetwork)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.pageSocialNetwork)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.postEdit = QTextEdit(self.pageSocialNetwork)
        self.postEdit.setObjectName(u"postEdit")
        sizePolicy2.setHeightForWidth(self.postEdit.sizePolicy().hasHeightForWidth())
        self.postEdit.setSizePolicy(sizePolicy2)
        self.postEdit.setMinimumSize(QSize(0, 270))
        self.postEdit.setMaximumSize(QSize(16777215, 270))

        self.verticalLayout_10.addWidget(self.postEdit)

        self.label_85 = QLabel(self.pageSocialNetwork)
        self.label_85.setObjectName(u"label_85")
        sizePolicy5.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.label_85)

        self.imagePost = QTextEdit(self.pageSocialNetwork)
        self.imagePost.setObjectName(u"imagePost")
        sizePolicy2.setHeightForWidth(self.imagePost.sizePolicy().hasHeightForWidth())
        self.imagePost.setSizePolicy(sizePolicy2)
        self.imagePost.setMinimumSize(QSize(600, 250))
        self.imagePost.setMaximumSize(QSize(600, 250))
        self.imagePost.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.imagePost)


        self.gridLayout_46.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_45, 0, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 122, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_46.addItem(self.verticalSpacer_28, 1, 0, 1, 1)

        self.widget_29 = QWidget(self.pageSocialNetwork)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_45 = QGridLayout(self.widget_29)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_44 = QSpacerItem(995, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_45.addItem(self.horizontalSpacer_44, 0, 0, 1, 1)

        self.publishBtn = QPushButton(self.widget_29)
        self.publishBtn.setObjectName(u"publishBtn")
        self.publishBtn.setMinimumSize(QSize(150, 30))
        self.publishBtn.setMaximumSize(QSize(150, 30))
        self.publishBtn.setIcon(icon15)
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

        self.userAddComboBox = QComboBox(self.pageAddIncome)
        self.userAddComboBox.setObjectName(u"userAddComboBox")

        self.verticalLayout_17.addWidget(self.userAddComboBox)

        self.label_15 = QLabel(self.pageAddIncome)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_17.addWidget(self.label_15)

        self.titleAddComboBox = QComboBox(self.pageAddIncome)
        self.titleAddComboBox.setObjectName(u"titleAddComboBox")

        self.verticalLayout_17.addWidget(self.titleAddComboBox)

        self.label_47 = QLabel(self.pageAddIncome)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_17.addWidget(self.label_47)

        self.nameChapterAddIncome = QLineEdit(self.pageAddIncome)
        self.nameChapterAddIncome.setObjectName(u"nameChapterAddIncome")

        self.verticalLayout_17.addWidget(self.nameChapterAddIncome)

        self.label_49 = QLabel(self.pageAddIncome)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_17.addWidget(self.label_49)

        self.salaryAddIncome = QLineEdit(self.pageAddIncome)
        self.salaryAddIncome.setObjectName(u"salaryAddIncome")
        self.salaryAddIncome.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_17.addWidget(self.salaryAddIncome)


        self.gridLayout_18.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(563, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_20, 0, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(540, 505, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_16, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.pageAddIncome)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.widget_10.setMinimumSize(QSize(0, 40))
        self.widget_10.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)

        self.backAddIncome = QPushButton(self.widget_10)
        self.backAddIncome.setObjectName(u"backAddIncome")
        self.backAddIncome.setMinimumSize(QSize(140, 30))
        self.backAddIncome.setMaximumSize(QSize(140, 30))
        self.backAddIncome.setIcon(icon16)
        self.backAddIncome.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.backAddIncome)

        self.addIncomeBtn = QPushButton(self.widget_10)
        self.addIncomeBtn.setObjectName(u"addIncomeBtn")
        self.addIncomeBtn.setMinimumSize(QSize(140, 30))
        self.addIncomeBtn.setMaximumSize(QSize(140, 30))
        self.addIncomeBtn.setIcon(icon19)
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

        self.userEditComboBox = QComboBox(self.pageEditIncome)
        self.userEditComboBox.setObjectName(u"userEditComboBox")

        self.verticalLayout_18.addWidget(self.userEditComboBox)

        self.label_5 = QLabel(self.pageEditIncome)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_18.addWidget(self.label_5)

        self.titleEditcomboBox = QComboBox(self.pageEditIncome)
        self.titleEditcomboBox.setObjectName(u"titleEditcomboBox")

        self.verticalLayout_18.addWidget(self.titleEditcomboBox)

        self.label_52 = QLabel(self.pageEditIncome)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_18.addWidget(self.label_52)

        self.nameChapterEditIncome = QLineEdit(self.pageEditIncome)
        self.nameChapterEditIncome.setObjectName(u"nameChapterEditIncome")

        self.verticalLayout_18.addWidget(self.nameChapterEditIncome)

        self.label_54 = QLabel(self.pageEditIncome)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_18.addWidget(self.label_54)

        self.salaryEditIncome = QLineEdit(self.pageEditIncome)
        self.salaryEditIncome.setObjectName(u"salaryEditIncome")
        self.salaryEditIncome.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)

        self.verticalLayout_18.addWidget(self.salaryEditIncome)


        self.gridLayout_19.addLayout(self.verticalLayout_18, 0, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(563, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_22, 0, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(540, 505, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_17, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.pageEditIncome)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.widget_11.setMinimumSize(QSize(0, 40))
        self.widget_11.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_21 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_21)

        self.backEditIncome = QPushButton(self.widget_11)
        self.backEditIncome.setObjectName(u"backEditIncome")
        self.backEditIncome.setMinimumSize(QSize(140, 30))
        self.backEditIncome.setMaximumSize(QSize(140, 30))
        self.backEditIncome.setIcon(icon16)
        self.backEditIncome.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.backEditIncome)

        self.editIncomeBtn = QPushButton(self.widget_11)
        self.editIncomeBtn.setObjectName(u"editIncomeBtn")
        self.editIncomeBtn.setMinimumSize(QSize(140, 30))
        self.editIncomeBtn.setMaximumSize(QSize(140, 30))
        self.editIncomeBtn.setIcon(icon15)
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
        sizePolicy5.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy5)

        self.verticalLayout_27.addWidget(self.label_89)

        self.fileAdd = QTextEdit(self.pageFileSharing)
        self.fileAdd.setObjectName(u"fileAdd")
        sizePolicy6.setHeightForWidth(self.fileAdd.sizePolicy().hasHeightForWidth())
        self.fileAdd.setSizePolicy(sizePolicy6)
        self.fileAdd.setMinimumSize(QSize(900, 270))
        self.fileAdd.setMaximumSize(QSize(16777215, 270))
        self.fileAdd.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.fileAdd)

        self.label_90 = QLabel(self.pageFileSharing)
        self.label_90.setObjectName(u"label_90")
        sizePolicy5.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy5)

        self.verticalLayout_27.addWidget(self.label_90)

        self.recipientFile = QComboBox(self.pageFileSharing)
        self.recipientFile.setObjectName(u"recipientFile")
        sizePolicy5.setHeightForWidth(self.recipientFile.sizePolicy().hasHeightForWidth())
        self.recipientFile.setSizePolicy(sizePolicy5)
        self.recipientFile.setMinimumSize(QSize(540, 0))
        self.recipientFile.setMaximumSize(QSize(540, 25))

        self.verticalLayout_27.addWidget(self.recipientFile)

        self.rar_error = QLabel(self.pageFileSharing)
        self.rar_error.setObjectName(u"rar_error")

        self.verticalLayout_27.addWidget(self.rar_error)


        self.gridLayout_50.addLayout(self.verticalLayout_27, 0, 0, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_29, 1, 0, 1, 1)

        self.widget_30 = QWidget(self.pageFileSharing)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy1.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy1)
        self.widget_30.setMinimumSize(QSize(0, 40))
        self.widget_30.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_48 = QGridLayout(self.widget_30)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_48 = QSpacerItem(995, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_48, 0, 0, 1, 1)

        self.sendFile = QPushButton(self.widget_30)
        self.sendFile.setObjectName(u"sendFile")
        self.sendFile.setMinimumSize(QSize(140, 30))
        self.sendFile.setMaximumSize(QSize(140, 30))
        icon20 = QIcon()
        icon20.addFile(u":/icon/icon/free-icon-send-9351602.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendFile.setIcon(icon20)
        self.sendFile.setIconSize(QSize(20, 20))

        self.gridLayout_48.addWidget(self.sendFile, 0, 1, 1, 1)


        self.gridLayout_50.addWidget(self.widget_30, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageFileSharing)
        self.pageAccount = QWidget()
        self.pageAccount.setObjectName(u"pageAccount")
        self.gridLayout_52 = QGridLayout(self.pageAccount)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.widget_17 = QWidget(self.pageAccount)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_6 = QGridLayout(self.widget_17)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_26 = QGridLayout(self.widget_19)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.editLogo = QPushButton(self.widget_19)
        self.editLogo.setObjectName(u"editLogo")
        sizePolicy.setHeightForWidth(self.editLogo.sizePolicy().hasHeightForWidth())
        self.editLogo.setSizePolicy(sizePolicy)
        self.editLogo.setMinimumSize(QSize(140, 30))
        self.editLogo.setIcon(icon18)
        self.editLogo.setAutoDefault(False)
        self.editLogo.setFlat(False)

        self.gridLayout_26.addWidget(self.editLogo, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.addLogo = QPushButton(self.widget_19)
        self.addLogo.setObjectName(u"addLogo")
        sizePolicy.setHeightForWidth(self.addLogo.sizePolicy().hasHeightForWidth())
        self.addLogo.setSizePolicy(sizePolicy)
        self.addLogo.setMinimumSize(QSize(140, 30))
        self.addLogo.setIcon(icon19)
        self.addLogo.setCheckable(False)

        self.gridLayout_26.addWidget(self.addLogo, 0, 0, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_32, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.widget_19, 1, 1, 1, 1)

        self.label_37 = QLabel(self.widget_17)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(280, 370))
        self.label_37.setMaximumSize(QSize(280, 370))
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_37, 0, 0, 2, 1)

        self.widget_20 = QWidget(self.widget_17)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_27 = QGridLayout(self.widget_20)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_92 = QLabel(self.widget_20)
        self.label_92.setObjectName(u"label_92")
        sizePolicy.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy)

        self.gridLayout_27.addWidget(self.label_92, 5, 0, 1, 1)

        self.label_91 = QLabel(self.widget_20)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_27.addWidget(self.label_91, 1, 0, 1, 1)

        self.nameCrewAccComboBox = QComboBox(self.widget_20)
        self.nameCrewAccComboBox.setObjectName(u"nameCrewAccComboBox")
        sizePolicy2.setHeightForWidth(self.nameCrewAccComboBox.sizePolicy().hasHeightForWidth())
        self.nameCrewAccComboBox.setSizePolicy(sizePolicy2)
        self.nameCrewAccComboBox.setMinimumSize(QSize(340, 0))
        self.nameCrewAccComboBox.setMaximumSize(QSize(540, 16777215))

        self.gridLayout_27.addWidget(self.nameCrewAccComboBox, 2, 0, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_31, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_20, 0, 1, 1, 1)


        self.gridLayout_52.addWidget(self.widget_17, 0, 0, 2, 1)

        self.widget_16 = QWidget(self.pageAccount)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 0))
        self.widget_16.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_52.addWidget(self.widget_16, 3, 0, 1, 1)

        self.widget_32 = QWidget(self.pageAccount)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_7 = QGridLayout(self.widget_32)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 5)
        self.label_8 = QLabel(self.widget_33)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_25.addWidget(self.label_8)

        self.horizontalSpacer_51 = QSpacerItem(691, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_51)

        self.addTeamBtn = QPushButton(self.widget_33)
        self.addTeamBtn.setObjectName(u"addTeamBtn")
        self.addTeamBtn.setMinimumSize(QSize(140, 30))
        self.addTeamBtn.setMaximumSize(QSize(140, 30))
        self.addTeamBtn.setIcon(icon19)
        self.addTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.addTeamBtn)

        self.deleteTeamBtn = QPushButton(self.widget_33)
        self.deleteTeamBtn.setObjectName(u"deleteTeamBtn")
        self.deleteTeamBtn.setMinimumSize(QSize(140, 30))
        self.deleteTeamBtn.setMaximumSize(QSize(140, 30))
        self.deleteTeamBtn.setIcon(icon18)
        self.deleteTeamBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.deleteTeamBtn)


        self.gridLayout_7.addWidget(self.widget_33, 1, 0, 1, 1)

        self.tableTeamAcc = QTableView(self.widget_32)
        self.tableTeamAcc.setObjectName(u"tableTeamAcc")

        self.gridLayout_7.addWidget(self.tableTeamAcc, 2, 0, 1, 1)


        self.gridLayout_52.addWidget(self.widget_32, 2, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageAccount)
        self.pageAddTeams = QWidget()
        self.pageAddTeams.setObjectName(u"pageAddTeams")
        self.gridLayout_5 = QGridLayout(self.pageAddTeams)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_35 = QLabel(self.pageAddTeams)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_13.addWidget(self.label_35)

        self.teamsComboBoxTeam = QComboBox(self.pageAddTeams)
        self.teamsComboBoxTeam.setObjectName(u"teamsComboBoxTeam")
        self.teamsComboBoxTeam.setMinimumSize(QSize(540, 0))

        self.verticalLayout_13.addWidget(self.teamsComboBoxTeam)

        self.label_36 = QLabel(self.pageAddTeams)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_13.addWidget(self.label_36)

        self.usersComboBoxTeam = QComboBox(self.pageAddTeams)
        self.usersComboBoxTeam.setObjectName(u"usersComboBoxTeam")

        self.verticalLayout_13.addWidget(self.usersComboBoxTeam)


        self.gridLayout_5.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 557, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 1, 0, 1, 1)

        self.widget_18 = QWidget(self.pageAddTeams)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_30 = QSpacerItem(678, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_30)

        self.backTeamsBtn = QPushButton(self.widget_18)
        self.backTeamsBtn.setObjectName(u"backTeamsBtn")
        self.backTeamsBtn.setMinimumSize(QSize(140, 30))
        self.backTeamsBtn.setMaximumSize(QSize(140, 30))
        self.backTeamsBtn.setIcon(icon16)
        self.backTeamsBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.backTeamsBtn)

        self.saveTeams = QPushButton(self.widget_18)
        self.saveTeams.setObjectName(u"saveTeams")
        self.saveTeams.setMinimumSize(QSize(140, 30))
        self.saveTeams.setMaximumSize(QSize(140, 30))
        self.saveTeams.setIcon(icon15)
        self.saveTeams.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.saveTeams)


        self.gridLayout_5.addWidget(self.widget_18, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageAddTeams)
        self.pageAddTask = QWidget()
        self.pageAddTask.setObjectName(u"pageAddTask")
        self.gridLayout_23 = QGridLayout(self.pageAddTask)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.widget_12 = QWidget(self.pageAddTask)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.widget_12.setMinimumSize(QSize(0, 40))
        self.widget_12.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_25 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.taskAddBtn = QPushButton(self.widget_12)
        self.taskAddBtn.setObjectName(u"taskAddBtn")
        self.taskAddBtn.setMinimumSize(QSize(140, 30))
        self.taskAddBtn.setMaximumSize(QSize(140, 30))
        self.taskAddBtn.setIcon(icon19)
        self.taskAddBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.taskAddBtn)

        self.backTaskBtn = QPushButton(self.widget_12)
        self.backTaskBtn.setObjectName(u"backTaskBtn")
        self.backTaskBtn.setMinimumSize(QSize(140, 30))
        self.backTaskBtn.setMaximumSize(QSize(140, 30))
        self.backTaskBtn.setIcon(icon16)
        self.backTaskBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.backTaskBtn)


        self.gridLayout_23.addWidget(self.widget_12, 2, 0, 1, 2)

        self.verticalSpacer_18 = QSpacerItem(540, 422, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_18, 1, 0, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_55 = QLabel(self.pageAddTask)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_19.addWidget(self.label_55)

        self.dateEdit = QDateEdit(self.pageAddTask)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_19.addWidget(self.dateEdit)

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

        self.horizontalSpacer_23 = QSpacerItem(417, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_23, 0, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.pageAddTask)
        self.pageUserView = QWidget()
        self.pageUserView.setObjectName(u"pageUserView")
        self.gridLayout_42 = QGridLayout(self.pageUserView)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_84 = QLabel(self.pageUserView)
        self.label_84.setObjectName(u"label_84")

        self.verticalLayout_25.addWidget(self.label_84)

        self.dateEditView = QDateEdit(self.pageUserView)
        self.dateEditView.setObjectName(u"dateEditView")
        sizePolicy.setHeightForWidth(self.dateEditView.sizePolicy().hasHeightForWidth())
        self.dateEditView.setSizePolicy(sizePolicy)
        self.dateEditView.setMinimumSize(QSize(450, 0))
        self.dateEditView.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.dateEditView)

        self.label_86 = QLabel(self.pageUserView)
        self.label_86.setObjectName(u"label_86")

        self.verticalLayout_25.addWidget(self.label_86)

        self.taskEditView = QTextEdit(self.pageUserView)
        self.taskEditView.setObjectName(u"taskEditView")
        self.taskEditView.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.taskEditView)


        self.gridLayout_42.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(540, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_42.addItem(self.verticalSpacer_27, 1, 0, 1, 1)

        self.widget_26 = QWidget(self.pageUserView)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy1.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy1)
        self.widget_26.setMinimumSize(QSize(0, 40))
        self.widget_26.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_42 = QSpacerItem(809, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_42)

        self.backTaskViewBtn = QPushButton(self.widget_26)
        self.backTaskViewBtn.setObjectName(u"backTaskViewBtn")
        self.backTaskViewBtn.setMinimumSize(QSize(140, 30))
        self.backTaskViewBtn.setMaximumSize(QSize(140, 30))
        self.backTaskViewBtn.setIcon(icon16)
        self.backTaskViewBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.backTaskViewBtn)


        self.gridLayout_42.addWidget(self.widget_26, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.pageUserView)
        self.pageAboutUs = QWidget()
        self.pageAboutUs.setObjectName(u"pageAboutUs")
        self.gridLayout_8 = QGridLayout(self.pageAboutUs)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_54, 1, 2, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_30, 0, 1, 1, 1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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


        self.gridLayout_8.addWidget(self.widget_37, 1, 1, 1, 1)

        self.widget_36 = QWidget(self.pageAboutUs)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy5.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy5)
        self.gridLayout_53 = QGridLayout(self.widget_36)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.verLabel = QLabel(self.widget_36)
        self.verLabel.setObjectName(u"verLabel")

        self.gridLayout_53.addWidget(self.verLabel, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.widget_36, 3, 1, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.tableListTask = QTableView(self.pageListTask)
        self.tableListTask.setObjectName(u"tableListTask")
        self.tableListTask.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableListTask.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableListTask.setGridStyle(Qt.NoPen)
        self.tableListTask.setSortingEnabled(True)
        self.tableListTask.setCornerButtonEnabled(True)

        self.gridLayout_44.addWidget(self.tableListTask, 1, 0, 1, 1)

        self.widget_27 = QWidget(self.pageListTask)
        self.widget_27.setObjectName(u"widget_27")
        self.gridLayout_43 = QGridLayout(self.widget_27)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.addListTask = QPushButton(self.widget_27)
        self.addListTask.setObjectName(u"addListTask")
        self.addListTask.setMinimumSize(QSize(140, 30))
        self.addListTask.setMaximumSize(QSize(140, 30))
        self.addListTask.setIcon(icon19)
        self.addListTask.setIconSize(QSize(20, 20))

        self.gridLayout_43.addWidget(self.addListTask, 0, 3, 1, 1)

        self.deleteListTask = QPushButton(self.widget_27)
        self.deleteListTask.setObjectName(u"deleteListTask")
        self.deleteListTask.setMinimumSize(QSize(140, 30))
        self.deleteListTask.setMaximumSize(QSize(140, 30))
        self.deleteListTask.setIcon(icon18)
        self.deleteListTask.setIconSize(QSize(20, 20))

        self.gridLayout_43.addWidget(self.deleteListTask, 0, 2, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(855, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_43.addItem(self.horizontalSpacer_43, 0, 0, 1, 1)

        self.editListTask = QPushButton(self.widget_27)
        self.editListTask.setObjectName(u"editListTask")
        self.editListTask.setMinimumSize(QSize(140, 30))
        self.editListTask.setMaximumSize(QSize(140, 30))
        self.editListTask.setIcon(icon17)

        self.gridLayout_43.addWidget(self.editListTask, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_27, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.pageListTask)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_26 = QSpacerItem(829, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_26)

        self.cancelPageList = QPushButton(self.widget_4)
        self.cancelPageList.setObjectName(u"cancelPageList")
        self.cancelPageList.setMinimumSize(QSize(140, 30))
        self.cancelPageList.setMaximumSize(QSize(140, 30))
        self.cancelPageList.setIcon(icon16)

        self.horizontalLayout_15.addWidget(self.cancelPageList)


        self.gridLayout_44.addWidget(self.widget_4, 2, 0, 1, 1)

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
        self.accountBtn_1.toggled.connect(self.accountBtn_2.setChecked)
        self.translateBtn_1.toggled.connect(self.translateBtn_2.setChecked)
        self.translateBtn_2.toggled.connect(self.translateBtn_1.setChecked)
        self.accountBtn_2.toggled.connect(self.accountBtn_1.setChecked)
        self.fileSharingBtn_2.toggled.connect(self.fileSharingBtn_1.setChecked)
        self.socialNetworksBtn_2.toggled.connect(self.socialNetworksBtn_1.setChecked)
        self.scheduleBtn_2.toggled.connect(self.scheduleBtn_1.setChecked)
        self.incomeBtn_2.toggled.connect(self.incomeBtn_1.setChecked)
        self.titleBtn_2.toggled.connect(self.titleBtn_1.setChecked)

        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(12)
        self.editLogo.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimazeBtn.setText("")
        self.expandBtn.setText("")
        self.closeBtn.setText("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430/\u043b\u043e\u0433\u0438\u043d", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.errorLabel.setText("")
#if QT_CONFIG(tooltip)
        self.inLogBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.inLogBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.notRegLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0438\u043b\u0438 \u0441\u043c\u0435\u043d\u044b \u043f\u0430\u0440\u043e\u043b\u044f \u0432 \u043d\u0430\u0448\u0435\u043c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438, \u043f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435 \u0432 \u043d\u0430\u0448 \u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c \u0431\u043e\u0442 \u043f\u043e QR-\u043a\u043e\u0434\u0443 \u043d\u0438\u0436\u0435", None))
        self.forgotPasLabel.setText("")
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
        self.label_2.setText("")
        self.titleBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0442\u043b\u044b", None))
        self.incomeBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.scheduleBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.socialNetworksBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0446. \u0441\u0435\u0442\u0438", None))
        self.fileSharingBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043c\u0435\u043d \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.accountBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.translateBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
        self.exitAppBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.openMenuBtn.setText("")
        self.label.setText("")
        self.titleBtn_1.setText("")
        self.incomeBtn_1.setText("")
        self.scheduleBtn_1.setText("")
        self.socialNetworksBtn_1.setText("")
        self.fileSharingBtn_1.setText("")
        self.accountBtn_1.setText("")
        self.translateBtn_1.setText("")
        self.exitAppBtn.setText("")
        self.SearchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.SearchBtn.setText("")
        self.pushOpenAdd.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0435", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.taskApplyBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.backApplyTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
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
        self.incomeEditBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.incomeDeleteBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.incomeAddBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.photoDesc.setText("")
        self.textEditDesc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u0430\u0439\u0442\u043b\u0430", None))
        self.editTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.deleteTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.backBtnDesc.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0441\u044f\u0446", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0433\u043e\u0434", None))
        self.backAddTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.addTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.imageArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a\u043e\u0432", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u0430\u0439\u0442\u043b\u0430", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0445\u043e\u0434\u0430", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.imageAreaEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a\u043e\u0432", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u0430\u0439\u0442\u043b\u0430", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0445\u043e\u0434\u0430", None))
        self.backEditTitleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.applyEditBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.postEdit.setPlaceholderText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.imagePost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.publishBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0442\u043b", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u043b\u0430\u0432\u044b", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.backAddIncome.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.addIncomeBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0442\u043b", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u043b\u0430\u0432\u044b", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.backEditIncome.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.editIncomeBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \".rar\", \".docx\"", None))
        self.fileAdd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \".rar\" \u043d\u0435 \u0434\u043e\u043b\u0436\u0435\u043d \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0442\u044c 100\u043c\u0431, \".docx\" \u043d\u0435 \u0434\u043e\u043b\u0436\u0435\u043d \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0442\u044c 50\u043c\u0431", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u043f\u0430\u043f\u043a\u0430", None))
        self.rar_error.setText("")
        self.sendFile.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.editLogo.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.addLogo.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u0430\u0441\u0442\u044c \u0434\u043b\u044f \u043b\u043e\u0433\u043e\u0442\u0438\u043f\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0430\u0448\u0435\u0439 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u0430\u0432 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.addTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.backTeamsBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.saveTeams.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.taskAddBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.backTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0435", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.backTaskViewBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u0430 \u043f\u0440\u0438 \u0443\u0447\u0430\u0441\u0442\u0438\u0438 DADA GROUP", None))
        self.verLabel.setText(QCoreApplication.translate("MainWindow", u"ver 1.12", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None))
        self.addListTask.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteListTask.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editListTask.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.cancelPageList.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
    # retranslateUi

