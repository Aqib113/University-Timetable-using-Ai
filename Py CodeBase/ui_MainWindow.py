# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowyhhJsR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1189, 671)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"*{\n"
"color: rgb(33, 47, 61);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#centralwidget{\n"
"background-color: rgb(222, 228, 234);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QWidget(self.centralwidget)
        self.Header.setObjectName(u"Header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        self.Header.setFont(font)
        self.Header.setStyleSheet(u"*{\n"
"background-color: rgb(222, 228, 234);\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.Header)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.Header)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(222, 228, 234);\n"
"border-right: 1px solid rgb(0, 0, 0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"border-bottom-right-radius: 45px;\n"
"padding-right: 10px;\n"
"padding-bottom: 10px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"\n"
" }")
        self.logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.logo)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.LogoButton = QPushButton(self.logo)
        self.LogoButton.setObjectName(u"LogoButton")
        self.LogoButton.setMinimumSize(QSize(120, 0))
        icon = QIcon()
        icon.addFile(u":/final logo2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LogoButton.setIcon(icon)
        self.LogoButton.setIconSize(QSize(80, 100))

        self.gridLayout_5.addWidget(self.LogoButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_6.addWidget(self.logo, 0, 0, 1, 1)

        self.content = QFrame(self.Header)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"#Project_Label{\n"
"border:none;\n"
"background-color:none;\n"
"\n"
"}\n"
"\n"
"#CloseProject_Button{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.content.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.content)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.headercontent = QFrame(self.content)
        self.headercontent.setObjectName(u"headercontent")
        self.headercontent.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"background-color:  rgb(33, 47, 61);\n"
"}")
        self.headercontent.setFrameShape(QFrame.Shape.StyledPanel)
        self.headercontent.setFrameShadow(QFrame.Shadow.Raised)
        self.headercontent.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.headercontent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.HeaderMiddleLabel_2 = QLabel(self.headercontent)
        self.HeaderMiddleLabel_2.setObjectName(u"HeaderMiddleLabel_2")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.HeaderMiddleLabel_2.setFont(font1)
        self.HeaderMiddleLabel_2.setStyleSheet(u"* {\n"
"	padding: 5px, 0px,5px,0px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.HeaderMiddleLabel_2)

        self.HeaderSpacer1_4 = QSpacerItem(352, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.HeaderSpacer1_4)

        self.HeaderSpacer1_3 = QSpacerItem(352, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.HeaderSpacer1_3)

        self.BarButtons_2 = QFrame(self.headercontent)
        self.BarButtons_2.setObjectName(u"BarButtons_2")
        self.BarButtons_2.setEnabled(True)
        self.BarButtons_2.setToolTipDuration(-1)
        self.BarButtons_2.setStyleSheet(u"QPushButton:hover {\n"
"border:2px solid  rgb(240, 255, 253);\n"
"border-radius: 3px;\n"
"\n"
" }\n"
"\n"
"#Close_window_Button:hover {\n"
"	background-color:rgb(255, 0, 0);\n"
" }")
        self.BarButtons_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.BarButtons_2.setFrameShadow(QFrame.Shadow.Raised)
        self.BarButtons_2.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.BarButtons_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Minimize_Button = QPushButton(self.BarButtons_2)
        self.Minimize_Button.setObjectName(u"Minimize_Button")
        self.Minimize_Button.setMinimumSize(QSize(37, 34))
        self.Minimize_Button.setMaximumSize(QSize(37, 34))
        icon1 = QIcon()
        icon1.addFile(u":/minimize_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Minimize_Button.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.Minimize_Button)

        self.Fullscreen_Button = QPushButton(self.BarButtons_2)
        self.Fullscreen_Button.setObjectName(u"Fullscreen_Button")
        self.Fullscreen_Button.setMinimumSize(QSize(37, 34))
        self.Fullscreen_Button.setMaximumSize(QSize(37, 34))
        icon2 = QIcon()
        icon2.addFile(u":/fullScreen_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Fullscreen_Button.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.Fullscreen_Button)

        self.Close_window_Button = QPushButton(self.BarButtons_2)
        self.Close_window_Button.setObjectName(u"Close_window_Button")
        self.Close_window_Button.setMinimumSize(QSize(37, 34))
        self.Close_window_Button.setMaximumSize(QSize(37, 34))
        self.Close_window_Button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Cut_Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Close_window_Button.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.Close_window_Button)


        self.horizontalLayout_8.addWidget(self.BarButtons_2)


        self.verticalLayout_18.addWidget(self.headercontent, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_12)

        self.ProjectButtonFrame = QFrame(self.content)
        self.ProjectButtonFrame.setObjectName(u"ProjectButtonFrame")
        self.ProjectButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ProjectButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.ProjectButtonFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Project_Label = QLabel(self.ProjectButtonFrame)
        self.Project_Label.setObjectName(u"Project_Label")
        self.Project_Label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.Project_Label)

        self.CloseProject_Button = QPushButton(self.ProjectButtonFrame)
        self.CloseProject_Button.setObjectName(u"CloseProject_Button")
        self.CloseProject_Button.setMinimumSize(QSize(35, 30))
        self.CloseProject_Button.setFont(font1)
        self.CloseProject_Button.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.CloseProject_Button)


        self.verticalLayout_18.addWidget(self.ProjectButtonFrame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_6.addWidget(self.content, 0, 1, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.Header)

        self.Middle = QWidget(self.centralwidget)
        self.Middle.setObjectName(u"Middle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Middle.sizePolicy().hasHeightForWidth())
        self.Middle.setSizePolicy(sizePolicy1)
        self.Middle.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.Middle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenu = QFrame(self.Middle)
        self.LeftMenu.setObjectName(u"LeftMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LeftMenu.sizePolicy().hasHeightForWidth())
        self.LeftMenu.setSizePolicy(sizePolicy2)
        self.LeftMenu.setMinimumSize(QSize(0, 0))
        self.LeftMenu.setStyleSheet(u"* {\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"QPushButton{\n"
"font-size:12pt;\n"
"font-family: Segoe UI;\n"
"text-align:left;\n"
"padding:5px;\n"
"padding-left:10px;\n"
"\n"
"\n"
"}\n"
"\n"
"#ExpandMenuButton{\n"
"padding:0px;}\n"
"#ExpandMenuButton:hover{\n"
"border:2px solid rgb(222, 228, 234);\n"
"padding:0px;}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(225, 255, 253);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.LeftMenu.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.LeftMenu)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.middlebuttons = QFrame(self.LeftMenu)
        self.middlebuttons.setObjectName(u"middlebuttons")
        sizePolicy1.setHeightForWidth(self.middlebuttons.sizePolicy().hasHeightForWidth())
        self.middlebuttons.setSizePolicy(sizePolicy1)
        self.middlebuttons.setStyleSheet(u"#middlebuttons{\n"
"background-color: rgb(33, 47, 61);\n"
"border-right: 1px solid rgb(0,0,0);\n"
"border-top:1px solid rgb(0,0,0);\n"
"height:40px;\n"
"}\n"
"")
        self.middlebuttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.middlebuttons.setFrameShadow(QFrame.Shadow.Raised)
        self.middlebuttons.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.middlebuttons)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 7, 7, -1)
        self.MainFeatures = QFrame(self.middlebuttons)
        self.MainFeatures.setObjectName(u"MainFeatures")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainFeatures.sizePolicy().hasHeightForWidth())
        self.MainFeatures.setSizePolicy(sizePolicy3)
        self.MainFeatures.setMaximumSize(QSize(16777215, 440))
        self.MainFeatures.setStyleSheet(u"")
        self.MainFeatures.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFeatures.setFrameShadow(QFrame.Shadow.Raised)
        self.MainFeatures.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.MainFeatures)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 14, 0, 0)
        self.TimetableButton = QPushButton(self.MainFeatures)
        self.TimetableButton.setObjectName(u"TimetableButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.TimetableButton.sizePolicy().hasHeightForWidth())
        self.TimetableButton.setSizePolicy(sizePolicy4)
        self.TimetableButton.setMinimumSize(QSize(0, 0))
        self.TimetableButton.setMaximumSize(QSize(50, 45))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.TimetableButton.setFont(font2)
        self.TimetableButton.setToolTipDuration(-2)
        self.TimetableButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/Timetable logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TimetableButton.setIcon(icon4)
        self.TimetableButton.setIconSize(QSize(30, 30))
        self.TimetableButton.setCheckable(True)

        self.verticalLayout_5.addWidget(self.TimetableButton)

        self.DatesheetButton = QPushButton(self.MainFeatures)
        self.DatesheetButton.setObjectName(u"DatesheetButton")
        sizePolicy.setHeightForWidth(self.DatesheetButton.sizePolicy().hasHeightForWidth())
        self.DatesheetButton.setSizePolicy(sizePolicy)
        self.DatesheetButton.setMinimumSize(QSize(0, 0))
        self.DatesheetButton.setMaximumSize(QSize(50, 45))
        self.DatesheetButton.setFont(font2)
        self.DatesheetButton.setStyleSheet(u"\n"
"padding-left:12px;")
        icon5 = QIcon()
        icon5.addFile(u":/DateSheet logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DatesheetButton.setIcon(icon5)
        self.DatesheetButton.setIconSize(QSize(32, 32))
        self.DatesheetButton.setCheckable(True)
        self.DatesheetButton.setChecked(False)

        self.verticalLayout_5.addWidget(self.DatesheetButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.SetWeekDays = QPushButton(self.MainFeatures)
        self.SetWeekDays.setObjectName(u"SetWeekDays")
        self.SetWeekDays.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.SetWeekDays.sizePolicy().hasHeightForWidth())
        self.SetWeekDays.setSizePolicy(sizePolicy4)
        self.SetWeekDays.setMinimumSize(QSize(0, 0))
        self.SetWeekDays.setMaximumSize(QSize(50, 45))
        self.SetWeekDays.setFont(font2)
        self.SetWeekDays.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Days logo copy2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SetWeekDays.setIcon(icon6)
        self.SetWeekDays.setIconSize(QSize(30, 30))
        self.SetWeekDays.setCheckable(True)

        self.verticalLayout_5.addWidget(self.SetWeekDays)

        self.SetLectures = QPushButton(self.MainFeatures)
        self.SetLectures.setObjectName(u"SetLectures")
        self.SetLectures.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.SetLectures.sizePolicy().hasHeightForWidth())
        self.SetLectures.setSizePolicy(sizePolicy4)
        self.SetLectures.setMinimumSize(QSize(0, 0))
        self.SetLectures.setMaximumSize(QSize(50, 45))
        self.SetLectures.setFont(font2)
        self.SetLectures.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/Time Logo copy2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SetLectures.setIcon(icon7)
        self.SetLectures.setIconSize(QSize(30, 30))
        self.SetLectures.setCheckable(True)

        self.verticalLayout_5.addWidget(self.SetLectures)

        self.SetClasses = QPushButton(self.MainFeatures)
        self.SetClasses.setObjectName(u"SetClasses")
        self.SetClasses.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.SetClasses.sizePolicy().hasHeightForWidth())
        self.SetClasses.setSizePolicy(sizePolicy4)
        self.SetClasses.setMinimumSize(QSize(0, 0))
        self.SetClasses.setMaximumSize(QSize(50, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setItalic(False)
        self.SetClasses.setFont(font3)
        self.SetClasses.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/Class logo copy2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SetClasses.setIcon(icon8)
        self.SetClasses.setIconSize(QSize(30, 30))
        self.SetClasses.setCheckable(True)

        self.verticalLayout_5.addWidget(self.SetClasses)

        self.SetRooms = QPushButton(self.MainFeatures)
        self.SetRooms.setObjectName(u"SetRooms")
        self.SetRooms.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.SetRooms.sizePolicy().hasHeightForWidth())
        self.SetRooms.setSizePolicy(sizePolicy4)
        self.SetRooms.setMinimumSize(QSize(0, 0))
        self.SetRooms.setMaximumSize(QSize(50, 45))
        self.SetRooms.setFont(font2)
        self.SetRooms.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/Rooms logo copy2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SetRooms.setIcon(icon9)
        self.SetRooms.setIconSize(QSize(30, 30))
        self.SetRooms.setCheckable(True)

        self.verticalLayout_5.addWidget(self.SetRooms)

        self.SetCourses = QPushButton(self.MainFeatures)
        self.SetCourses.setObjectName(u"SetCourses")
        self.SetCourses.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.SetCourses.sizePolicy().hasHeightForWidth())
        self.SetCourses.setSizePolicy(sizePolicy4)
        self.SetCourses.setMinimumSize(QSize(0, 0))
        self.SetCourses.setMaximumSize(QSize(50, 45))
        self.SetCourses.setFont(font2)
        self.SetCourses.setStyleSheet(u"*{\n"
"padding-left: 11px;}")
        icon10 = QIcon()
        icon10.addFile(u":/S & I logo copy2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SetCourses.setIcon(icon10)
        self.SetCourses.setIconSize(QSize(30, 30))
        self.SetCourses.setCheckable(True)

        self.verticalLayout_5.addWidget(self.SetCourses)


        self.verticalLayout_6.addWidget(self.MainFeatures, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.OtherButtons = QFrame(self.middlebuttons)
        self.OtherButtons.setObjectName(u"OtherButtons")
        sizePolicy3.setHeightForWidth(self.OtherButtons.sizePolicy().hasHeightForWidth())
        self.OtherButtons.setSizePolicy(sizePolicy3)
        self.OtherButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.OtherButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.OtherButtons.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.OtherButtons)
        self.verticalLayout_8.setSpacing(17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.SettingButton = QPushButton(self.OtherButtons)
        self.SettingButton.setObjectName(u"SettingButton")
        self.SettingButton.setMinimumSize(QSize(0, 0))
        self.SettingButton.setMaximumSize(QSize(50, 45))
        self.SettingButton.setStyleSheet(u"*{\n"
"font-size:14pt;\n"
"font-weight: Bold;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingButton.setIcon(icon11)
        self.SettingButton.setIconSize(QSize(27, 27))

        self.verticalLayout_8.addWidget(self.SettingButton, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_6.addWidget(self.OtherButtons)


        self.horizontalLayout_7.addWidget(self.middlebuttons)

        self.frame_2 = QFrame(self.LeftMenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 16, 0, 0)
        self.ExpandMenuButton = QPushButton(self.frame_2)
        self.ExpandMenuButton.setObjectName(u"ExpandMenuButton")
        self.ExpandMenuButton.setMinimumSize(QSize(0, 0))
        self.ExpandMenuButton.setMaximumSize(QSize(35, 35))
        icon12 = QIcon()
        icon12.addFile(u":/expand icon copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExpandMenuButton.setIcon(icon12)
        self.ExpandMenuButton.setIconSize(QSize(35, 35))
        self.ExpandMenuButton.setCheckable(True)
        self.ExpandMenuButton.setChecked(True)

        self.verticalLayout_17.addWidget(self.ExpandMenuButton, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_7.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.LeftMenu, 0, Qt.AlignmentFlag.AlignLeft)

        self.MainContentBody = QStackedWidget(self.Middle)
        self.MainContentBody.setObjectName(u"MainContentBody")
        sizePolicy1.setHeightForWidth(self.MainContentBody.sizePolicy().hasHeightForWidth())
        self.MainContentBody.setSizePolicy(sizePolicy1)
        self.MainContentBody.setStyleSheet(u"*{;\n"
"background-color: rgb(222, 228, 234)	;\n"
"}\n"
"")
        self.MainContentBody.setLineWidth(0)
        self.TimetablePage = QWidget()
        self.TimetablePage.setObjectName(u"TimetablePage")
        self.TimetablePage.setStyleSheet(u"*{\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color: rgb(56, 73, 89);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:rgb(255, 255, 255);\n"
"font-size:15px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.TimetablePage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.TimetablePageExtention = QStackedWidget(self.TimetablePage)
        self.TimetablePageExtention.setObjectName(u"TimetablePageExtention")
        self.ButtonsPage = QWidget()
        self.ButtonsPage.setObjectName(u"ButtonsPage")
        self.gridLayout_10 = QGridLayout(self.ButtonsPage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ButtonFrame = QFrame(self.ButtonsPage)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ButtonFrame.sizePolicy().hasHeightForWidth())
        self.ButtonFrame.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(14)
        self.ButtonFrame.setFont(font4)
        self.ButtonFrame.setStyleSheet(u"QPushButton{\n"
"padding:5px;\n"
"background-color:rgb(33, 47, 61);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border:1px solid rgb(255,255,255);\n"
"}")
        self.ButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ButtonFrame)
        self.verticalLayout_2.setSpacing(14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NewTimetableButton = QPushButton(self.ButtonFrame)
        self.NewTimetableButton.setObjectName(u"NewTimetableButton")
        self.NewTimetableButton.setMinimumSize(QSize(240, 42))
        self.NewTimetableButton.setMaximumSize(QSize(240, 42))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(12)
        self.NewTimetableButton.setFont(font5)

        self.verticalLayout_2.addWidget(self.NewTimetableButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.OpenButton = QPushButton(self.ButtonFrame)
        self.OpenButton.setObjectName(u"OpenButton")
        self.OpenButton.setMinimumSize(QSize(240, 42))
        self.OpenButton.setMaximumSize(QSize(240, 42))
        self.OpenButton.setFont(font5)

        self.verticalLayout_2.addWidget(self.OpenButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.gridLayout_10.addWidget(self.ButtonFrame, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.TimetablePageExtention.addWidget(self.ButtonsPage)
        self.Showuppage = QWidget()
        self.Showuppage.setObjectName(u"Showuppage")
        self.verticalLayout_28 = QVBoxLayout(self.Showuppage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_5 = QLabel(self.Showuppage)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(20)
        self.label_5.setFont(font6)

        self.verticalLayout_28.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.TimetablePageExtention.addWidget(self.Showuppage)
        self.NewTimeTablePage = QWidget()
        self.NewTimeTablePage.setObjectName(u"NewTimeTablePage")
        self.verticalLayout_27 = QVBoxLayout(self.NewTimeTablePage)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.NewTimeTablePageFrame1 = QWidget(self.NewTimeTablePage)
        self.NewTimeTablePageFrame1.setObjectName(u"NewTimeTablePageFrame1")
        self.NewTimeTablePageFrame1.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.NewTimeTablePageFrame1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.MainFrame = QFrame(self.NewTimeTablePageFrame1)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"#MainFrame{\n"
"background-color: rgb(33, 47, 61);\n"
"background-color: rgb(222, 228, 234);\n"
"\n"
"border: 2px solid rgb(33, 47, 61);\n"
"border-radius:20px;\n"
"padding-left:30px;\n"
"\n"
"}\n"
"#CloseProjectButton {\n"
"    background: none;\n"
"    padding: 3px;\n"
"}\n"
"#CloseProjectButton:hover {\n"
"icon-size: 30px 30px;\n"
"	border:none;\n"
"}\n"
"\n"
"#StartProjectButton{\n"
"border-radius:0px;\n"
"padding:0px;\n"
"}\n"
"#StartProjectButton:hover{\n"
"border:1px solid rgb(255,255,255);\n"
"padding:2px;\n"
"}\n"
"#ProjectNameInput{\n"
"padding-left:5px;\n"
"border: 1px solid rgb(33, 47, 61);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"#NewProjectForm{\n"
"border-left: 3px solid rgb(33, 47, 61);\n"
"padding: 10px;\n"
"}\n"
"")
        self.MainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.MainFrame.setLineWidth(2)
        self.verticalLayout_30 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(2, 3, 0, 7)
        self.CloseProjectButton = QPushButton(self.MainFrame)
        self.CloseProjectButton.setObjectName(u"CloseProjectButton")
        self.CloseProjectButton.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/image 4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CloseProjectButton.setIcon(icon13)
        self.CloseProjectButton.setIconSize(QSize(25, 25))

        self.verticalLayout_30.addWidget(self.CloseProjectButton, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.NewProjectForm = QFrame(self.MainFrame)
        self.NewProjectForm.setObjectName(u"NewProjectForm")
        self.NewProjectForm.setStyleSheet(u"color:rgb(33, 47, 61);\n"
"")
        self.NewProjectForm.setFrameShape(QFrame.Shape.StyledPanel)
        self.NewProjectForm.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.NewProjectForm)
        self.verticalLayout_31.setSpacing(13)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 8, 0)
        self.frame = QFrame(self.NewProjectForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Heading = QLabel(self.frame)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setFont(font5)

        self.verticalLayout_29.addWidget(self.Heading)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_29.addWidget(self.label_8)


        self.verticalLayout_31.addWidget(self.frame)

        self.ProjectNameInput = QLineEdit(self.NewProjectForm)
        self.ProjectNameInput.setObjectName(u"ProjectNameInput")
        self.ProjectNameInput.setMinimumSize(QSize(200, 30))
        self.ProjectNameInput.setMaximumSize(QSize(200, 30))
        self.ProjectNameInput.setFont(font1)

        self.verticalLayout_31.addWidget(self.ProjectNameInput, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_30.addWidget(self.NewProjectForm, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_13)

        self.StartProjectButton = QPushButton(self.MainFrame)
        self.StartProjectButton.setObjectName(u"StartProjectButton")
        self.StartProjectButton.setMinimumSize(QSize(100, 0))
        self.StartProjectButton.setFont(font5)
        self.StartProjectButton.setStyleSheet(u"QPushButton{\n"
"padding:5px;\n"
"background-color:rgb(33, 47, 61);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border:1px solid rgb(255,255,255);\n"
"}")

        self.verticalLayout_30.addWidget(self.StartProjectButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.gridLayout_8.addWidget(self.MainFrame, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_27.addWidget(self.NewTimeTablePageFrame1)

        self.TimetablePageExtention.addWidget(self.NewTimeTablePage)

        self.verticalLayout_9.addWidget(self.TimetablePageExtention)

        self.MainContentBody.addWidget(self.TimetablePage)
        self.DatesheetPage = QWidget()
        self.DatesheetPage.setObjectName(u"DatesheetPage")
        self.DatesheetPage.setStyleSheet(u"*{\n"
"background-color:transparent;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color: rgb(56, 73, 89);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.DatesheetPage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.DateSheetFramePage = QFrame(self.DatesheetPage)
        self.DateSheetFramePage.setObjectName(u"DateSheetFramePage")
        self.DateSheetFramePage.setStyleSheet(u"QPushButton{\n"
"padding:5px;\n"
"background-color:rgb(33, 47, 61);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255)\n"
"}")
        self.DateSheetFramePage.setFrameShape(QFrame.Shape.StyledPanel)
        self.DateSheetFramePage.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.DateSheetFramePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.PageTitle_2 = QLabel(self.DateSheetFramePage)
        self.PageTitle_2.setObjectName(u"PageTitle_2")
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(22)
        self.PageTitle_2.setFont(font7)

        self.verticalLayout_10.addWidget(self.PageTitle_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_11.addWidget(self.DateSheetFramePage, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.MainContentBody.addWidget(self.DatesheetPage)
        self.UserInputPage = QWidget()
        self.UserInputPage.setObjectName(u"UserInputPage")
        self.UserInputPage.setStyleSheet(u"*{\n"
"background-color:transparent;\n"
"}\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color:  rgb(0, 85, 127);\n"
"border:1px solid  rgb(0, 85, 127);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.UserInputPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.MainBodyContent = QWidget(self.UserInputPage)
        self.MainBodyContent.setObjectName(u"MainBodyContent")
        self.MainBodyContent.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.MainBodyContent)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Inputpages = QStackedWidget(self.MainBodyContent)
        self.Inputpages.setObjectName(u"Inputpages")
        self.Inputpages.setStyleSheet(u"\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color: rgb(33, 47, 61);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(255,255,255);\n"
"}")
        self.WorkingDaysPage = QWidget()
        self.WorkingDaysPage.setObjectName(u"WorkingDaysPage")
        self.verticalLayout_26 = QVBoxLayout(self.WorkingDaysPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.WorkingDayPageFrame = QFrame(self.WorkingDaysPage)
        self.WorkingDayPageFrame.setObjectName(u"WorkingDayPageFrame")
        sizePolicy5.setHeightForWidth(self.WorkingDayPageFrame.sizePolicy().hasHeightForWidth())
        self.WorkingDayPageFrame.setSizePolicy(sizePolicy5)
        self.WorkingDayPageFrame.setStyleSheet(u"QComboBox, QAbstractItemView{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"padding : 10px;\n"
"selection-background-color: #337ab7; \n"
"selection-color: #fff;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 5px; /* Padding around each item in the dropdown menu */\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #337ab7; /* Background color of the selected item */\n"
"    color: #fff; /* Text color of the selected item */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCheckBox{\n"
"padding : 5px;\n"
"}\n"
"QCheckBox::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"background-color: rgba(0,0,0,0.15)	;\n"
"border: 1px solid rgb(0,0,0);\n"
"border-radius : 5px;\n"
"}\n"
"QCheckBox:unchecked {\n"
"background: rgb(255,255,255);\n"
"border: 1px solid rgb(0,0,0);\n"
"border-radius : 5px;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"border: 1px solid  rgba(0,0,"
                        "0,0.15)	;\n"
"}\n"
"\n"
"#Heading1Frame{\n"
"border-left: 3px solid rgb(33, 47, 61);\n"
"padding: 10px;\n"
" }\n"
"#Heading1{\n"
"padding-left:1px;\n"
"}\n"
"#Heading2{\n"
" color: rgb(0, 85, 127);\n"
"font-size: 14pt;\n"
"padding-left:1px;\n"
"}\n"
"#OptionalDayInput_Frame{\n"
"border-left: 3px solid rgb(33, 47, 61);\n"
"border-bottom: 3px solid rgb(33, 47, 61);\n"
"}\n"
"\n"
"")
        self.WorkingDayPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.WorkingDayPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.WorkingDayPageFrame)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Heading1Frame = QFrame(self.WorkingDayPageFrame)
        self.Heading1Frame.setObjectName(u"Heading1Frame")
        self.Heading1Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Heading1Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.Heading1Frame)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Heading1 = QLabel(self.Heading1Frame)
        self.Heading1.setObjectName(u"Heading1")
        self.Heading1.setFont(font1)

        self.verticalLayout_32.addWidget(self.Heading1)

        self.MainLabel = QLabel(self.Heading1Frame)
        self.MainLabel.setObjectName(u"MainLabel")
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(26)
        font8.setBold(True)
        self.MainLabel.setFont(font8)

        self.verticalLayout_32.addWidget(self.MainLabel)


        self.verticalLayout_15.addWidget(self.Heading1Frame)

        self.Heading2 = QLabel(self.WorkingDayPageFrame)
        self.Heading2.setObjectName(u"Heading2")
        font9 = QFont()
        font9.setFamilies([u"Roboto"])
        font9.setPointSize(14)
        font9.setUnderline(False)
        self.Heading2.setFont(font9)

        self.verticalLayout_15.addWidget(self.Heading2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.days = QFrame(self.WorkingDayPageFrame)
        self.days.setObjectName(u"days")
        self.days.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.days)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.day1 = QCheckBox(self.days)
        self.day1.setObjectName(u"day1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.day1.sizePolicy().hasHeightForWidth())
        self.day1.setSizePolicy(sizePolicy6)
        self.day1.setMinimumSize(QSize(90, 0))
        self.day1.setMaximumSize(QSize(90, 16777215))
        self.day1.setAutoRepeatDelay(0)
        self.day1.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day1, 1, 0, 1, 1)

        self.day7 = QCheckBox(self.days)
        self.day7.setObjectName(u"day7")
        sizePolicy6.setHeightForWidth(self.day7.sizePolicy().hasHeightForWidth())
        self.day7.setSizePolicy(sizePolicy6)
        self.day7.setMinimumSize(QSize(90, 0))
        self.day7.setMaximumSize(QSize(90, 16777215))
        self.day7.setAutoRepeatDelay(0)
        self.day7.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day7, 6, 1, 1, 1)

        self.day4 = QCheckBox(self.days)
        self.day4.setObjectName(u"day4")
        sizePolicy6.setHeightForWidth(self.day4.sizePolicy().hasHeightForWidth())
        self.day4.setSizePolicy(sizePolicy6)
        self.day4.setMinimumSize(QSize(90, 0))
        self.day4.setMaximumSize(QSize(90, 16777215))
        self.day4.setAutoRepeatDelay(0)
        self.day4.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day4, 4, 0, 1, 1)

        self.day6 = QCheckBox(self.days)
        self.day6.setObjectName(u"day6")
        sizePolicy6.setHeightForWidth(self.day6.sizePolicy().hasHeightForWidth())
        self.day6.setSizePolicy(sizePolicy6)
        self.day6.setMinimumSize(QSize(90, 0))
        self.day6.setMaximumSize(QSize(90, 16777215))
        self.day6.setAutoRepeatDelay(0)
        self.day6.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day6, 4, 2, 1, 1)

        self.day2 = QCheckBox(self.days)
        self.day2.setObjectName(u"day2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.day2.sizePolicy().hasHeightForWidth())
        self.day2.setSizePolicy(sizePolicy7)
        self.day2.setMinimumSize(QSize(90, 0))
        self.day2.setMaximumSize(QSize(90, 16777215))
        self.day2.setAutoRepeatDelay(0)
        self.day2.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day2, 1, 1, 1, 1)

        self.day5 = QCheckBox(self.days)
        self.day5.setObjectName(u"day5")
        sizePolicy6.setHeightForWidth(self.day5.sizePolicy().hasHeightForWidth())
        self.day5.setSizePolicy(sizePolicy6)
        self.day5.setMinimumSize(QSize(90, 0))
        self.day5.setMaximumSize(QSize(90, 16777215))
        self.day5.setAutoRepeatDelay(0)
        self.day5.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day5, 4, 1, 1, 1)

        self.day3 = QCheckBox(self.days)
        self.day3.setObjectName(u"day3")
        sizePolicy6.setHeightForWidth(self.day3.sizePolicy().hasHeightForWidth())
        self.day3.setSizePolicy(sizePolicy6)
        self.day3.setMinimumSize(QSize(90, 0))
        self.day3.setMaximumSize(QSize(90, 35))
        self.day3.setAutoRepeatDelay(0)
        self.day3.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.day3, 1, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.days)

        self.OptionalDayInput_Frame = QFrame(self.WorkingDayPageFrame)
        self.OptionalDayInput_Frame.setObjectName(u"OptionalDayInput_Frame")
        self.OptionalDayInput_Frame.setStyleSheet(u"QLabel{\n"
"color: rgb(0, 85, 127);\n"
"padding-left: 10px;\n"
"}\n"
"#OptioanlDayInput{\n"
"border:1px solid rgb(0, 85, 127);\n"
"\n"
"\n"
"}\n"
"")
        self.OptionalDayInput_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.OptionalDayInput_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.OptionalDayInput_Frame)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 0, 8, 25)
        self.OptionalDayLabel = QLabel(self.OptionalDayInput_Frame)
        self.OptionalDayLabel.setObjectName(u"OptionalDayLabel")
        font10 = QFont()
        font10.setPointSize(11)
        font10.setBold(False)
        self.OptionalDayLabel.setFont(font10)

        self.verticalLayout_16.addWidget(self.OptionalDayLabel)

        self.OptioanlDayInput = QComboBox(self.OptionalDayInput_Frame)
        self.OptioanlDayInput.setObjectName(u"OptioanlDayInput")
        self.OptioanlDayInput.setMinimumSize(QSize(371, 0))

        self.verticalLayout_16.addWidget(self.OptioanlDayInput, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_15.addWidget(self.OptionalDayInput_Frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.BottomButtons = QFrame(self.WorkingDayPageFrame)
        self.BottomButtons.setObjectName(u"BottomButtons")
        sizePolicy4.setHeightForWidth(self.BottomButtons.sizePolicy().hasHeightForWidth())
        self.BottomButtons.setSizePolicy(sizePolicy4)
        self.BottomButtons.setMinimumSize(QSize(385, 43))
        self.BottomButtons.setStyleSheet(u"\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px;\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"#NextButton_1{\n"
"border-top-right-radius: 7px;\n"
"border-Bottom-right-radius: 7px;\n"
"}\n"
"\n"
"#PreviousButton_1{\n"
"border-top-left-radius: 7px;\n"
"border-Bottom-left-radius: 7px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"Background-color: rgb(33, 47, 61);\n"
"color:   rgb(240, 255, 253);\n"
"}\n"
"\n"
"#NextButton_Label_1{\n"
"border-bottom-left-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"padding-left: 5px;\n"
"}\n"
"\n"
"#PreviousButton_Label_1{\n"
"border-top-right-radius: 7px;\n"
"border-Bottom-right-radius: 7px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#NextButtonFrame:hover{\n"
"border: 1px solid rgb(33, 47, 61);\n"
"border-radius: 7px;\n"
"}\n"
"#PreviousButtonFrame:hover{\n"
"border: 1px solid rgb(33, 47, 61);\n"
"border-radius: 7px;\n"
"}")
        self.BottomButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.BottomButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.BottomButtons.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.BottomButtons)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.PreviousButtonFrame = QFrame(self.BottomButtons)
        self.PreviousButtonFrame.setObjectName(u"PreviousButtonFrame")
        self.PreviousButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PreviousButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.PreviousButtonFrame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.PreviousButtonFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.PreviousButton_1 = QPushButton(self.PreviousButtonFrame)
        self.PreviousButton_1.setObjectName(u"PreviousButton_1")
        sizePolicy5.setHeightForWidth(self.PreviousButton_1.sizePolicy().hasHeightForWidth())
        self.PreviousButton_1.setSizePolicy(sizePolicy5)
        self.PreviousButton_1.setFont(font5)
        icon14 = QIcon()
        icon14.addFile(u":/PreviousLogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PreviousButton_1.setIcon(icon14)
        self.PreviousButton_1.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.PreviousButton_1)

        self.PreviousButton_Label_1 = QLabel(self.PreviousButtonFrame)
        self.PreviousButton_Label_1.setObjectName(u"PreviousButton_Label_1")
        sizePolicy5.setHeightForWidth(self.PreviousButton_Label_1.sizePolicy().hasHeightForWidth())
        self.PreviousButton_Label_1.setSizePolicy(sizePolicy5)
        self.PreviousButton_Label_1.setMinimumSize(QSize(0, 35))
        self.PreviousButton_Label_1.setFont(font5)
        self.PreviousButton_Label_1.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.PreviousButton_Label_1)


        self.horizontalLayout_10.addWidget(self.PreviousButtonFrame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.NextButtonFrame = QFrame(self.BottomButtons)
        self.NextButtonFrame.setObjectName(u"NextButtonFrame")
        self.NextButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.NextButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.NextButtonFrame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.NextButtonFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.NextButton_Label_1 = QLabel(self.NextButtonFrame)
        self.NextButton_Label_1.setObjectName(u"NextButton_Label_1")
        sizePolicy5.setHeightForWidth(self.NextButton_Label_1.sizePolicy().hasHeightForWidth())
        self.NextButton_Label_1.setSizePolicy(sizePolicy5)
        self.NextButton_Label_1.setMinimumSize(QSize(65, 35))
        self.NextButton_Label_1.setFont(font5)
        self.NextButton_Label_1.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.NextButton_Label_1)

        self.NextButton_1 = QPushButton(self.NextButtonFrame)
        self.NextButton_1.setObjectName(u"NextButton_1")
        self.NextButton_1.setFont(font5)
        self.NextButton_1.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/NextLogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.NextButton_1.setIcon(icon15)
        self.NextButton_1.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.NextButton_1)


        self.horizontalLayout_10.addWidget(self.NextButtonFrame)


        self.verticalLayout_15.addWidget(self.BottomButtons, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_26.addWidget(self.WorkingDayPageFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.Inputpages.addWidget(self.WorkingDaysPage)
        self.LectureTimePage = QWidget()
        self.LectureTimePage.setObjectName(u"LectureTimePage")
        self.LectureTimePage.setStyleSheet(u"")
        self.verticalLayout_35 = QVBoxLayout(self.LectureTimePage)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.LectureTimePageFrame1 = QFrame(self.LectureTimePage)
        self.LectureTimePageFrame1.setObjectName(u"LectureTimePageFrame1")
        self.LectureTimePageFrame1.setMinimumSize(QSize(0, 370))
        self.LectureTimePageFrame1.setMaximumSize(QSize(16777215, 620))
        self.LectureTimePageFrame1.setStyleSheet(u"\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color:rgb(33, 47, 61);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    font-size: 14px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    font-weight: bold;\n"
"    background-color: #f0f0f0;\n"
"    padding: 5px;\n"
"    border: 1px solid #ddd;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	background-color:rgba(0,0,0,0.15)	;\n"
"    padding: 4px;\n"
"    border: none;\n"
"}\n"
"\n"
"#Heading1Frame_2{\n"
"border-left: 3px solid rgb(33, 47, 61);\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#AddMoreLecture_Button{\n"
"background: none;\n"
"border:none\n"
"}\n"
"")
        self.LectureTimePageFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.LectureTimePageFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.LectureTimePageFrame1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.Heading1Frame_2 = QFrame(self.LectureTimePageFrame1)
        self.Heading1Frame_2.setObjectName(u"Heading1Frame_2")
        self.Heading1Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Heading1Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Heading1Frame_2)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Heading1_2 = QLabel(self.Heading1Frame_2)
        self.Heading1_2.setObjectName(u"Heading1_2")
        font11 = QFont()
        font11.setFamilies([u"Roboto"])
        font11.setPointSize(10)
        self.Heading1_2.setFont(font11)

        self.verticalLayout_33.addWidget(self.Heading1_2)

        self.MainLabel_2 = QLabel(self.Heading1Frame_2)
        self.MainLabel_2.setObjectName(u"MainLabel_2")
        self.MainLabel_2.setFont(font8)

        self.verticalLayout_33.addWidget(self.MainLabel_2)

        self.label_9 = QLabel(self.Heading1Frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_33.addWidget(self.label_9)


        self.verticalLayout_14.addWidget(self.Heading1Frame_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_10)

        self.frame_3 = QFrame(self.LectureTimePageFrame1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.LectureTable = QTableWidget(self.frame_3)
        if (self.LectureTable.columnCount() < 4):
            self.LectureTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.LectureTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.LectureTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.LectureTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(255, 255, 255));
        self.LectureTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.LectureTable.rowCount() < 1):
            self.LectureTable.setRowCount(1)
        self.LectureTable.setObjectName(u"LectureTable")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.LectureTable.sizePolicy().hasHeightForWidth())
        self.LectureTable.setSizePolicy(sizePolicy8)
        self.LectureTable.setMinimumSize(QSize(422, 0))
        self.LectureTable.setMaximumSize(QSize(16777215, 16777215))
        self.LectureTable.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"border:none;\n"
"padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding:2px;\n"
"}")
        self.LectureTable.setFrameShape(QFrame.Shape.NoFrame)
        self.LectureTable.setLineWidth(1)
        self.LectureTable.setMidLineWidth(0)
        self.LectureTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.LectureTable.setAutoScroll(True)
        self.LectureTable.setDragDropOverwriteMode(False)
        self.LectureTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.LectureTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.LectureTable.setGridStyle(Qt.PenStyle.NoPen)
        self.LectureTable.setRowCount(1)
        self.LectureTable.horizontalHeader().setVisible(True)
        self.LectureTable.horizontalHeader().setMinimumSectionSize(32)
        self.LectureTable.horizontalHeader().setHighlightSections(True)
        self.LectureTable.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_14.addWidget(self.LectureTable)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_34 = QVBoxLayout(self.frame_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, -1, 0, 0)
        self.AddMoreLecture_Button = QPushButton(self.frame_4)
        self.AddMoreLecture_Button.setObjectName(u"AddMoreLecture_Button")
        icon16 = QIcon()
        icon16.addFile(u":/Add button logo Black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AddMoreLecture_Button.setIcon(icon16)
        self.AddMoreLecture_Button.setIconSize(QSize(25, 25))

        self.verticalLayout_34.addWidget(self.AddMoreLecture_Button)


        self.horizontalLayout_14.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_14.addWidget(self.frame_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.BottomButtons_2 = QFrame(self.LectureTimePageFrame1)
        self.BottomButtons_2.setObjectName(u"BottomButtons_2")
        sizePolicy.setHeightForWidth(self.BottomButtons_2.sizePolicy().hasHeightForWidth())
        self.BottomButtons_2.setSizePolicy(sizePolicy)
        self.BottomButtons_2.setMinimumSize(QSize(385, 43))
        self.BottomButtons_2.setStyleSheet(u"\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px;\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"#NextButton_2{\n"
"border-top-right-radius: 7px;\n"
"border-Bottom-right-radius: 7px;\n"
"}\n"
"\n"
"#PreviousButton_2{\n"
"border-top-left-radius: 7px;\n"
"border-Bottom-left-radius: 7px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"Background-color: rgb(33, 47, 61);\n"
"color:   rgb(240, 255, 253);\n"
"}\n"
"\n"
"#NextButton_Label_2{\n"
"border-bottom-left-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"padding-left: 5px;\n"
"}\n"
"\n"
"#PreviousButton_Label_2{\n"
"border-top-right-radius: 7px;\n"
"border-Bottom-right-radius: 7px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#NextButtonFrame:hover{\n"
"border: 1px solid rgb(33, 47, 61);\n"
"border-radius: 7px;\n"
"}\n"
"#PreviousButtonFrame:hover{\n"
"border: 1px solid rgb(33, 47, 61);\n"
"border-radius: 7px;\n"
"}")
        self.BottomButtons_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.BottomButtons_2.setFrameShadow(QFrame.Shadow.Raised)
        self.BottomButtons_2.setLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self.BottomButtons_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.PreviousButtonFrame_2 = QFrame(self.BottomButtons_2)
        self.PreviousButtonFrame_2.setObjectName(u"PreviousButtonFrame_2")
        self.PreviousButtonFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.PreviousButtonFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.PreviousButtonFrame_2.setLineWidth(0)
        self.horizontalLayout_12 = QHBoxLayout(self.PreviousButtonFrame_2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.PreviousButton_2 = QPushButton(self.PreviousButtonFrame_2)
        self.PreviousButton_2.setObjectName(u"PreviousButton_2")
        sizePolicy5.setHeightForWidth(self.PreviousButton_2.sizePolicy().hasHeightForWidth())
        self.PreviousButton_2.setSizePolicy(sizePolicy5)
        self.PreviousButton_2.setFont(font5)
        self.PreviousButton_2.setIcon(icon14)
        self.PreviousButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.PreviousButton_2)

        self.PreviousButton_Label_2 = QLabel(self.PreviousButtonFrame_2)
        self.PreviousButton_Label_2.setObjectName(u"PreviousButton_Label_2")
        sizePolicy5.setHeightForWidth(self.PreviousButton_Label_2.sizePolicy().hasHeightForWidth())
        self.PreviousButton_Label_2.setSizePolicy(sizePolicy5)
        self.PreviousButton_Label_2.setMinimumSize(QSize(0, 35))
        self.PreviousButton_Label_2.setFont(font5)
        self.PreviousButton_Label_2.setLineWidth(0)

        self.horizontalLayout_12.addWidget(self.PreviousButton_Label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_11.addWidget(self.PreviousButtonFrame_2)

        self.NextButtonFrame_2 = QFrame(self.BottomButtons_2)
        self.NextButtonFrame_2.setObjectName(u"NextButtonFrame_2")
        self.NextButtonFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.NextButtonFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.NextButtonFrame_2.setLineWidth(0)
        self.horizontalLayout_13 = QHBoxLayout(self.NextButtonFrame_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(1, 1, 1, 1)
        self.NextButton_Label_2 = QLabel(self.NextButtonFrame_2)
        self.NextButton_Label_2.setObjectName(u"NextButton_Label_2")
        sizePolicy5.setHeightForWidth(self.NextButton_Label_2.sizePolicy().hasHeightForWidth())
        self.NextButton_Label_2.setSizePolicy(sizePolicy5)
        self.NextButton_Label_2.setMinimumSize(QSize(65, 35))
        self.NextButton_Label_2.setFont(font5)
        self.NextButton_Label_2.setLineWidth(0)

        self.horizontalLayout_13.addWidget(self.NextButton_Label_2)

        self.NextButton_2 = QPushButton(self.NextButtonFrame_2)
        self.NextButton_2.setObjectName(u"NextButton_2")
        self.NextButton_2.setFont(font5)
        self.NextButton_2.setStyleSheet(u"")
        self.NextButton_2.setIcon(icon15)
        self.NextButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.NextButton_2)


        self.horizontalLayout_11.addWidget(self.NextButtonFrame_2)


        self.verticalLayout_14.addWidget(self.BottomButtons_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_35.addWidget(self.LectureTimePageFrame1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.Inputpages.addWidget(self.LectureTimePage)
        self.SetupClasses = QWidget()
        self.SetupClasses.setObjectName(u"SetupClasses")
        self.verticalLayout_19 = QVBoxLayout(self.SetupClasses)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.SetupClassesFrame1 = QFrame(self.SetupClasses)
        self.SetupClassesFrame1.setObjectName(u"SetupClassesFrame1")
        self.SetupClassesFrame1.setMinimumSize(QSize(0, 370))
        self.SetupClassesFrame1.setMaximumSize(QSize(16777215, 16777215))
        self.SetupClassesFrame1.setStyleSheet(u"QPushButton{\n"
"padding:5px;\n"
"background-color:rgb(33, 47, 61);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    font-size: 14px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:  rgb(255, 255, 255);\n"
"	border: none;\n"
"    color: black;\n"
"    font-weight: 2px;\n"
"    padding: 4px;\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	background-color:rgba(0,0,0,0.15)	;\n"
"    padding: 4px;\n"
"    border: none;\n"
"}")
        self.SetupClassesFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.SetupClassesFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.SetupClassesFrame1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.MainHeading = QLabel(self.SetupClassesFrame1)
        self.MainHeading.setObjectName(u"MainHeading")
        self.MainHeading.setFont(font8)

        self.verticalLayout_20.addWidget(self.MainHeading, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_4)

        self.ClassForm = QFrame(self.SetupClassesFrame1)
        self.ClassForm.setObjectName(u"ClassForm")
        self.ClassForm.setStyleSheet(u"QComboBox, QAbstractItemView{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"padding : 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color: rgb(56, 73, 89);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.ClassForm.setFrameShape(QFrame.Shape.StyledPanel)
        self.ClassForm.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.ClassForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DepartmentInput = QComboBox(self.ClassForm)
        self.DepartmentInput.setObjectName(u"DepartmentInput")
        self.DepartmentInput.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.DepartmentInput.sizePolicy().hasHeightForWidth())
        self.DepartmentInput.setSizePolicy(sizePolicy5)
        self.DepartmentInput.setMinimumSize(QSize(260, 40))
        self.DepartmentInput.setEditable(False)

        self.gridLayout_2.addWidget(self.DepartmentInput, 1, 1, 1, 1)

        self.DegreeInput = QComboBox(self.ClassForm)
        self.DegreeInput.addItem("")
        self.DegreeInput.setObjectName(u"DegreeInput")
        self.DegreeInput.setMinimumSize(QSize(260, 32))
        self.DegreeInput.setEditable(False)

        self.gridLayout_2.addWidget(self.DegreeInput, 1, 2, 1, 1)

        self.DisciplineInput = QComboBox(self.ClassForm)
        self.DisciplineInput.setObjectName(u"DisciplineInput")
        self.DisciplineInput.setMinimumSize(QSize(260, 32))
        self.DisciplineInput.setEditable(False)

        self.gridLayout_2.addWidget(self.DisciplineInput, 2, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.ClassForm, 0, Qt.AlignmentFlag.AlignTop)

        self.SectionTable = QTableWidget(self.SetupClassesFrame1)
        if (self.SectionTable.columnCount() < 2):
            self.SectionTable.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.SectionTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.SectionTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        if (self.SectionTable.rowCount() < 7):
            self.SectionTable.setRowCount(7)
        self.SectionTable.setObjectName(u"SectionTable")
        self.SectionTable.setLineWidth(5)
        self.SectionTable.setRowCount(7)
        self.SectionTable.setColumnCount(2)

        self.verticalLayout_20.addWidget(self.SectionTable)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)

        self.pushButton_2 = QPushButton(self.SetupClassesFrame1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(155, 33))
        self.pushButton_2.setMaximumSize(QSize(155, 33))
        self.pushButton_2.setFont(font4)

        self.verticalLayout_20.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_19.addWidget(self.SetupClassesFrame1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.Inputpages.addWidget(self.SetupClasses)
        self.SetUpRooms = QWidget()
        self.SetUpRooms.setObjectName(u"SetUpRooms")
        self.gridLayout_3 = QGridLayout(self.SetUpRooms)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SetupRoomsPageFrame1 = QFrame(self.SetUpRooms)
        self.SetupRoomsPageFrame1.setObjectName(u"SetupRoomsPageFrame1")
        self.SetupRoomsPageFrame1.setStyleSheet(u"QLabels{\n"
"font-size: 14px;\n"
"}\n"
"QPushButton{\n"
"padding:5px;\n"
"background-color:rgb(33, 47, 61);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255)\n"
"}")
        self.SetupRoomsPageFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.SetupRoomsPageFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.SetupRoomsPageFrame1)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.SetupRoomsPageFrame1)
        self.label.setObjectName(u"label")
        self.label.setFont(font8)

        self.verticalLayout_7.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(36)
        self.gridLayout_4.setVerticalSpacing(16)
        self.lectureRoomsSpinBox = QSpinBox(self.SetupRoomsPageFrame1)
        self.lectureRoomsSpinBox.setObjectName(u"lectureRoomsSpinBox")

        self.gridLayout_4.addWidget(self.lectureRoomsSpinBox, 0, 1, 1, 1)

        self.miniComputerLabSpinBox = QSpinBox(self.SetupRoomsPageFrame1)
        self.miniComputerLabSpinBox.setObjectName(u"miniComputerLabSpinBox")

        self.gridLayout_4.addWidget(self.miniComputerLabSpinBox, 1, 1, 1, 1)

        self.bioLabsSpinBox = QSpinBox(self.SetupRoomsPageFrame1)
        self.bioLabsSpinBox.setObjectName(u"bioLabsSpinBox")

        self.gridLayout_4.addWidget(self.bioLabsSpinBox, 3, 1, 1, 1)

        self.computerLabsLabel = QLabel(self.SetupRoomsPageFrame1)
        self.computerLabsLabel.setObjectName(u"computerLabsLabel")
        self.computerLabsLabel.setFont(font4)

        self.gridLayout_4.addWidget(self.computerLabsLabel, 2, 0, 1, 1)

        self.computerLabsSpinBox = QSpinBox(self.SetupRoomsPageFrame1)
        self.computerLabsSpinBox.setObjectName(u"computerLabsSpinBox")

        self.gridLayout_4.addWidget(self.computerLabsSpinBox, 2, 1, 1, 1)

        self.bioLabsLabel = QLabel(self.SetupRoomsPageFrame1)
        self.bioLabsLabel.setObjectName(u"bioLabsLabel")
        self.bioLabsLabel.setFont(font4)

        self.gridLayout_4.addWidget(self.bioLabsLabel, 3, 0, 1, 1)

        self.miniComputerLabLabel_2 = QLabel(self.SetupRoomsPageFrame1)
        self.miniComputerLabLabel_2.setObjectName(u"miniComputerLabLabel_2")
        self.miniComputerLabLabel_2.setFont(font4)

        self.gridLayout_4.addWidget(self.miniComputerLabLabel_2, 1, 0, 1, 1)

        self.lectureRoomsLabel = QLabel(self.SetupRoomsPageFrame1)
        self.lectureRoomsLabel.setObjectName(u"lectureRoomsLabel")
        font12 = QFont()
        font12.setFamilies([u"Roboto"])
        font12.setPointSize(14)
        font12.setItalic(False)
        self.lectureRoomsLabel.setFont(font12)

        self.gridLayout_4.addWidget(self.lectureRoomsLabel, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.pushButton = QPushButton(self.SetupRoomsPageFrame1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(155, 33))
        self.pushButton.setMaximumSize(QSize(155, 33))
        self.pushButton.setFont(font4)

        self.verticalLayout_7.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.gridLayout_3.addWidget(self.SetupRoomsPageFrame1, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.Inputpages.addWidget(self.SetUpRooms)
        self.SetLecturers = QWidget()
        self.SetLecturers.setObjectName(u"SetLecturers")
        self.verticalLayout_3 = QVBoxLayout(self.SetLecturers)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SetLecturesPageFrame1 = QFrame(self.SetLecturers)
        self.SetLecturesPageFrame1.setObjectName(u"SetLecturesPageFrame1")
        self.SetLecturesPageFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.SetLecturesPageFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.SetLecturesPageFrame1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.SetLecturesPageFrame1)
        self.label_3.setObjectName(u"label_3")
        font13 = QFont()
        font13.setFamilies([u"Roboto"])
        font13.setPointSize(26)
        self.label_3.setFont(font13)

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_3.addWidget(self.SetLecturesPageFrame1)

        self.Inputpages.addWidget(self.SetLecturers)

        self.verticalLayout_13.addWidget(self.Inputpages)


        self.verticalLayout_12.addWidget(self.MainBodyContent)

        self.MainContentBody.addWidget(self.UserInputPage)
        self.IntroPage = QWidget()
        self.IntroPage.setObjectName(u"IntroPage")
        self.verticalLayout_21 = QVBoxLayout(self.IntroPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget = QWidget(self.IntroPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_22 = QVBoxLayout(self.widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)

        self.verticalLayout_22.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_21.addWidget(self.widget)

        self.MainContentBody.addWidget(self.IntroPage)
        self.ContactUsPage = QWidget()
        self.ContactUsPage.setObjectName(u"ContactUsPage")
        self.verticalLayout_24 = QVBoxLayout(self.ContactUsPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_2 = QWidget(self.ContactUsPage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_23 = QVBoxLayout(self.widget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_24.addWidget(self.widget_2)

        self.MainContentBody.addWidget(self.ContactUsPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.verticalLayout_25 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_2 = QLabel(self.SettingsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)

        self.verticalLayout_25.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.MainContentBody.addWidget(self.SettingsPage)

        self.horizontalLayout.addWidget(self.MainContentBody)


        self.verticalLayout.addWidget(self.Middle)

        self.Footer = QWidget(self.centralwidget)
        self.Footer.setObjectName(u"Footer")
        sizePolicy.setHeightForWidth(self.Footer.sizePolicy().hasHeightForWidth())
        self.Footer.setSizePolicy(sizePolicy)
        self.Footer.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"background-color: rgb(33, 47, 61);\n"
"\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.Footer)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 5, 2)
        self.FooterRoughLabel = QLabel(self.Footer)
        self.FooterRoughLabel.setObjectName(u"FooterRoughLabel")
        font14 = QFont()
        font14.setFamilies([u"Roboto"])
        font14.setPointSize(12)
        font14.setItalic(False)
        self.FooterRoughLabel.setFont(font14)
        self.FooterRoughLabel.setStyleSheet(u"color: rgb(33, 47, 61);")

        self.horizontalLayout_5.addWidget(self.FooterRoughLabel)

        self.FooterHorizontaSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.FooterHorizontaSpacer2)

        self.FooterMiddleLabel = QLabel(self.Footer)
        self.FooterMiddleLabel.setObjectName(u"FooterMiddleLabel")
        self.FooterMiddleLabel.setFont(font)

        self.horizontalLayout_5.addWidget(self.FooterMiddleLabel)

        self.FooterHorizontaSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.FooterHorizontaSpacer1)

        self.FooterRightLabel = QFrame(self.Footer)
        self.FooterRightLabel.setObjectName(u"FooterRightLabel")
        self.FooterRightLabel.setStyleSheet(u"")
        self.FooterRightLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.FooterRightLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.FooterRightLabel)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ContactUsButton = QPushButton(self.FooterRightLabel)
        self.ContactUsButton.setObjectName(u"ContactUsButton")
        font15 = QFont()
        font15.setFamilies([u"Roboto"])
        font15.setUnderline(True)
        self.ContactUsButton.setFont(font15)

        self.horizontalLayout_6.addWidget(self.ContactUsButton)


        self.horizontalLayout_5.addWidget(self.FooterRightLabel)


        self.verticalLayout.addWidget(self.Footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainContentBody.setCurrentIndex(0)
        self.TimetablePageExtention.setCurrentIndex(0)
        self.Inputpages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LogoButton.setText("")
        self.HeaderMiddleLabel_2.setText(QCoreApplication.translate("MainWindow", u"   Ai-Powered University Timetable", None))
        self.Minimize_Button.setText("")
        self.Fullscreen_Button.setText("")
        self.Close_window_Button.setText("")
        self.Project_Label.setText("")
        self.CloseProject_Button.setText("")
#if QT_CONFIG(tooltip)
        self.TimetableButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Timetable(click to start)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TimetableButton.setText(QCoreApplication.translate("MainWindow", u"  TimeTable", None))
        self.DatesheetButton.setText(QCoreApplication.translate("MainWindow", u"  Datesheet", None))
        self.SetWeekDays.setText(QCoreApplication.translate("MainWindow", u"  Weekely Days", None))
        self.SetLectures.setText(QCoreApplication.translate("MainWindow", u"  Lecture Time ", None))
        self.SetClasses.setText(QCoreApplication.translate("MainWindow", u"  Classes", None))
        self.SetRooms.setText(QCoreApplication.translate("MainWindow", u"  Rooms", None))
        self.SetCourses.setText(QCoreApplication.translate("MainWindow", u"   Courses", None))
        self.SettingButton.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.ExpandMenuButton.setText("")
        self.NewTimetableButton.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.OpenButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MainTime table will be here", None))
        self.CloseProjectButton.setText("")
        self.Heading.setText(QCoreApplication.translate("MainWindow", u"Enter Project Name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Your Timetable will be saved with same name specified here.", None))
        self.StartProjectButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.PageTitle_2.setText(QCoreApplication.translate("MainWindow", u"Date sheet options", None))
        self.Heading1.setText(QCoreApplication.translate("MainWindow", u"Step 1:", None))
        self.MainLabel.setText(QCoreApplication.translate("MainWindow", u"Customize Your Week", None))
        self.Heading2.setText(QCoreApplication.translate("MainWindow", u"Select Working days", None))
        self.day1.setText(QCoreApplication.translate("MainWindow", u"Monday", None))
        self.day7.setText(QCoreApplication.translate("MainWindow", u"Sunday", None))
        self.day4.setText(QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.day6.setText(QCoreApplication.translate("MainWindow", u"Saturday", None))
        self.day2.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.day5.setText(QCoreApplication.translate("MainWindow", u"Friday", None))
        self.day3.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None))
        self.OptionalDayLabel.setText(QCoreApplication.translate("MainWindow", u"Setup additional working day to arrange makeup lectures", None))
        self.OptioanlDayInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optional day", None))
        self.PreviousButton_1.setText("")
        self.PreviousButton_Label_1.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.NextButton_Label_1.setText(QCoreApplication.translate("MainWindow", u"Step 2", None))
        self.NextButton_1.setText("")
        self.Heading1_2.setText(QCoreApplication.translate("MainWindow", u"Step 2:", None))
        self.MainLabel_2.setText(QCoreApplication.translate("MainWindow", u"Setup Lectures and Timings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Add Lectures and their timings", None))
        ___qtablewidgetitem = self.LectureTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Start Time", None));
        ___qtablewidgetitem1 = self.LectureTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"End Time", None));
        ___qtablewidgetitem2 = self.LectureTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.LectureTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DelLecture", None));
        self.AddMoreLecture_Button.setText("")
        self.PreviousButton_2.setText("")
        self.PreviousButton_Label_2.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.NextButton_Label_2.setText(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.NextButton_2.setText("")
        self.MainHeading.setText(QCoreApplication.translate("MainWindow", u"Setting up Classes", None))
        self.DepartmentInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.DegreeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"BS/MS/FSc etc", None))

        self.DegreeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bs / Ms /  etc", None))
        self.DisciplineInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Discipline", None))
        ___qtablewidgetitem4 = self.SectionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Choose Semester", None));
        ___qtablewidgetitem5 = self.SectionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sections", None));
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SetUp Rooms, Labs, Halls", None))
        self.computerLabsLabel.setText(QCoreApplication.translate("MainWindow", u"Computer-Labs", None))
        self.bioLabsLabel.setText(QCoreApplication.translate("MainWindow", u"Bio-Labs", None))
        self.miniComputerLabLabel_2.setText(QCoreApplication.translate("MainWindow", u"Mini-Computer-Lab", None))
        self.lectureRoomsLabel.setText(QCoreApplication.translate("MainWindow", u"Lecture Rooms", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Set Lectures page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Intro page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contact us Page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings page", None))
        self.FooterRoughLabel.setText(QCoreApplication.translate("MainWindow", u"OneCli         ck TIme    table", None))
        self.FooterMiddleLabel.setText(QCoreApplication.translate("MainWindow", u"Developed by \"Aqib Maqsood\"", None))
        self.ContactUsButton.setText(QCoreApplication.translate("MainWindow", u"Need Support ?", None))
    # retranslateUi

