from PySide6.QtCore import Qt, QSize,QCoreApplication
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QMainWindow, QLabel, QTimeEdit, QPushButton
from ui_MainWindow import Ui_MainWindow

class CMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # ******  ***   REMOVING OF DEFAULT TITLEBAR **** ******
        self.setWindowFlags(Qt.FramelessWindowHint)
 
        # ******  ***   Connecting ToolBar buttons to their functions **** ******
        # ````````````````````````````````````````````````````````````````````````
        
        # Connecting Window Header Buttons
        self.Close_window_Button.clicked.connect(self.close)
        self.Minimize_Button.clicked.connect(self.showMinimized)
        self.Fullscreen_Button.clicked.connect(self.toggle_maximize)


        # ******  ***   navigation of HOME PAGE necessary  buttons **** ******# #````````````````````````````````````````````````````````````````````````
        self.LogoButton.clicked.connect(lambda: self.MainContentBody.setCurrentIndex(3))
        self.ContactUsButton.clicked.connect(lambda: self.MainContentBody.setCurrentIndex(4))
        self.SettingButton.clicked.connect(lambda: self.MainContentBody.setCurrentIndex(5))
        
        
        
        
        # ******  ***   navigation of Left Manu buttons buttons **** ******
        #````````````````````````````````````````````````````````````````````````
        self.TimetableButton.clicked.connect(lambda:self.MainContentBody.setCurrentIndex(0))
        self.DatesheetButton.clicked.connect(lambda:self.MainContentBody.setCurrentIndex(1))
        self.SetWeekDays.clicked.connect(self.setWeekDays)
        self.SetLectures.clicked.connect(self.setLectures)
        self.SetClasses.clicked.connect(self.setClasses)
        self.SetCourses.clicked.connect(self.setCourses)
        self.SetRooms.clicked.connect(self.setRooms)
        self.ExpandMenuButton.clicked.connect(self.ControlLeftMenu)
        
        
        
        
        #  ******  ***   Implementing the TImetable  Page's form **** ******
        #````````````````````````````````````````````````````````````````````````
        # Connecting Main screen Button
        self.NewTimetableButton.clicked.connect(lambda: self.TimetablePageExtention.setCurrentIndex(2))
        self.CloseProjectButton.clicked.connect(lambda: self.TimetablePageExtention.setCurrentIndex(0))
        self.StartProjectButton.clicked.connect(self.StartNewProject)
        
        
        #  ******  ***   Implementing the Customized Week Page's form **** ******
        #````````````````````````````````````````````````````````````````````````
        
        # Connecting 'Day (Monday, Tuesday etc)' Button (for updating option of "Optional day" box every click)
        self.day1.checkStateChanged.connect(self.setOptionalDays)
        self.day2.checkStateChanged.connect(self.setOptionalDays)
        self.day3.checkStateChanged.connect(self.setOptionalDays)
        self.day4.checkStateChanged.connect(self.setOptionalDays)
        self.day5.checkStateChanged.connect(self.setOptionalDays)
        self.day6.checkStateChanged.connect(self.setOptionalDays)
        self.day7.checkStateChanged.connect(self.setOptionalDays)
        
        # Connecting Button to navigating the next page "SetLectures"
        self.NextButton_1.clicked.connect(self.saveCustomizedWeekForm)
        
        # Connecting 'Close Project' Button (For closing the current project)
        self.CloseProject_Button.clicked.connect(self.CloseCurrentProject)
        
        
        #  ******  ***   Implmenting Add Lectures page **** ******
        #````````````````````````````````````````````````````````````````````````
              
        #  {-- Settingup the INITIAL STATE of  Lecture-table --}
        
        # setting total lecture counter
        self.Total_Lectures = 0
        
        # Initializing the table dimensions headers etc
        self.LectureTable.setColumnCount(4)
        self.LectureTable.setHorizontalHeaderLabels(['Start Time', 'End Time', 'Total Time', ''])
        self.LectureTable.horizontalHeader().setStretchLastSection(True)
        self.LectureTable.setColumnWidth(0,105)
        self.LectureTable.setColumnWidth(1,105)
        self.LectureTable.setColumnWidth(2,135)
        self.LectureTable.setColumnWidth(3,50)
        # Setting First row of table
        self.addNewLecture()
        
        # Connecting 'Add More Lecture' Button
        self.AddMoreLecture_Button.clicked.connect(self.addNewLecture)
        


# LOGIC FUNCTIONS


    # ***** ****** for window maximing  ***** ******
    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    # ***** ****** for Left Menu Toolsbuttons  ***** ******
    def setLectures(self):
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(1)
        
    def setClasses(self):
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(2)
        
    def setRooms(self):
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(3)
        
    def setCourses(self):
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(4)

    def setWeekDays(self):
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(0)

    # ---------- For expanding Left Menu
    def ControlLeftMenu(self):
        LeftMenuButtons = [
            self.DatesheetButton,
            self.TimetableButton,
            self.SetClasses,
            self.SetLectures,
            self.SetCourses,
            self.SetWeekDays,
            self.SetRooms,
            self.SettingButton
        ]
        
        if self.ExpandMenuButton.isChecked():
            # Now AS if the button if checked It mean the left menu if opened. So now clocing it
            # Logic for Collapsing menu
            for button in LeftMenuButtons:
                button.setFixedWidth(50)
                # button.setFixedWidth(50)
            self.middlebuttons.setFixedWidth(70)
            self.middlebuttons.setStyleSheet(u"#middlebuttons{\n"
            "background-color: rgb(33, 47, 61);\n"
            "border-right: 1px solid rgb(0,0,0);\n"
            "border-top:1px solid rgb(0,0,0);\n"
            "}\n"
            "")
            icon12 = QIcon()
            icon12.addFile(u":/expand icon copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ExpandMenuButton.setIcon(icon12)

        else:
            # Now AS if the button if checked It mean the left menu if Closed. So now Opening it
            # Expanding menu Logic
            for button in LeftMenuButtons:
                button.setFixedWidth(157)
                # button.setFixedWidth(155)
            self.middlebuttons.setFixedWidth(175)
            self.middlebuttons.setStyleSheet(u"#middlebuttons{\n"
            "background-color: rgb(33, 47, 61);\n"
            "border-right: 1px solid rgb(0,0,0);\n"
            "border-top:1px solid rgb(0,0,0);\n"
            "border-top-right-radius: 50px;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "")
            icon12 = QIcon()
            icon12.addFile(u":/collapse icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ExpandMenuButton.setIcon(icon12)
            
# -------------------------------------------------------------------------------------------     
    # *****          Logic Functions For "Add Lectures" page        *****
    def StartNewProject(self):
        # User Entered Project name Extracting
        text = self.ProjectNameInput.text()
        if text=='':
            text = 'Untitled_project'
        else:
            text = f" {text} "
        # Setting the Label text as same as the project name
        self.Project_Label.setText(QCoreApplication.translate("MainWindow", text, None))
        # Changing the Label stylesheet
        self.content.setStyleSheet(u"#Project_Label{\n"
            "color: rgb(255,255,255);\n"
            "border:none;\n"
            "\n"
            "background-color:rgb(33, 47, 61) ;\n"
            "border: 1px solid rgb(33, 47, 61);\n"
            "padding:5px;\n"
            "padding-right:10px;\n"
            "}\n"
            "\n"
            "#CloseProject_Button{\n"
            "border:1px solid rgb(33, 47, 61);\n"
            "background:none;\n"
            "border-Bottom-right-radius:10px;\n"
            "}\n"
            "\n"
            "#CloseProject_Button:hover{\n"
            "background-color:  rgb(255, 0, 0);\n"
            "border:none;\n"
            "}")
        # Setting Changing the Icon of project close button
        icon = QIcon()
        icon.addFile(u":/CLose_project_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CloseProject_Button.setIcon(icon)
        
        # As the new project started so enabling the User'Input pages and icon in single iteration
        Buttons_to_enable = [
            self.SetWeekDays,
            self.SetLectures,
            self.SetClasses,
            self.SetRooms,
            self.SetCourses,
        ]
        EnabledButtons_Logos = [
            ":/Days logo.png",
            ":/Time Logo.png",
            ":/Class logo.png",
            ":/Rooms logo.png",
            ":/S & I logo.png"
        ]
        
        Buttons_to_disable = [
            self.TimetableButton,
            self.DatesheetButton
        ]
        DisabledButton_Logos = [
            ":/Timetable logo2.png",
            ":/DateSheet logo2.png",
        ]
        
        for button, logo in zip(Buttons_to_enable, EnabledButtons_Logos):
            button.setEnabled(True)
            icon = QIcon()
            icon.addFile(logo, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            button.setIcon(icon)
            
        for button, logo in zip(Buttons_to_disable, DisabledButton_Logos):
            button.setEnabled(False)
            icon = QIcon()
            icon.addFile(logo, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            button.setIcon(icon)
        
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(0)
        

    def CloseCurrentProject(self):

        # Setting the Label text as same as the project name
        self.Project_Label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.ProjectNameInput.setText('')
        # Changing the Label stylesheet
        self.content.setStyleSheet(u"#Project_Label{\n"
            "border:none;\n"
            "background-color:none;\n"
            "\n"
            "}\n"
            "\n"
            "#CloseProject_Button{\n"
            "background:none;\n"
            "border:none;\n"
            "}")
        # Setting Changing the Icon of project close button
        self.CloseProject_Button.setIcon(QIcon())
        
        # As the new project started so enabling the User'Input pages and icon in single iteration
        Buttons_to_disable = [
            self.SetWeekDays,
            self.SetLectures,
            self.SetClasses,
            self.SetRooms,
            self.SetCourses,
        ]
        DisabledButton_Logos = [
            ":/Days logo copy2.png",
            ":/Time Logo copy2.png",
            ":/Class logo copy2.png",
            ":/Rooms logo copy2.png",
            ":/S & I logo copy2.png"
        ]
        
        Buttons_to_enable = [
            self.TimetableButton,
            self.DatesheetButton
        ]
        EnabledButton_Logos = [
            ":/Timetable logo.png",
            ":/DateSheet logo.png",
        ]
        
        for button, logo in zip(Buttons_to_disable, DisabledButton_Logos):
            button.setEnabled(False)
            icon = QIcon()
            icon.addFile(logo, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            button.setIcon(icon)
            
        for button, logo in zip(Buttons_to_enable, EnabledButton_Logos):
            button.setEnabled(True)
            icon = QIcon()
            icon.addFile(logo, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            button.setIcon(icon)
        
        self.MainContentBody.setCurrentIndex(0)
        self.TimetablePageExtention.setCurrentIndex(0)
        
           

    
    
# -------------------------------------------------------------------------------------------
    # *****          Logic Functions For "Set Days" page            ****
    
    #  For managing the optional days
    def setOptionalDays(self):
        #  _____________  List of days  ______________
        days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ,'Sunday']
        # ______________ Corresponding button for each day ___________
        buttons = [self.day1, self.day2, self.day3, self.day4, self.day5, self.day6, self.day7]
        
        # Collecting options for optional days in variable 'Optional_days'
        optional_days = [day for day, button in zip(days, buttons) if not button.isChecked()]
        
        # After choosing the optional days, removing the current items of combobox => 'OptionalDaysInput'
        while self.OptioanlDayInput.count()>0:
            self.OptioanlDayInput.removeItem(0)
        # Finally setting out the items
        for i in optional_days:
            self.OptioanlDayInput.addItem(i)
    
    #  For Saving the customized week input
    def saveCustomizedWeekForm(self):
        self.MainContentBody.setCurrentIndex(2)
        self.Inputpages.setCurrentIndex(1)
        
        
        days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ,'Sunday']
        buttons = [self.day1, self.day2, self.day3, self.day4, self.day5, self.day6, self.day7]
        working_days = [day for day, button in zip(days, buttons) if button.isChecked()]
        print(working_days)

 
# -------------------------------------------------------------------------------------------     
    # *****          Logic Functions For "Add Lectures" page        *****
    
    # For Adding New Lecture Slot
    def addNewLecture(self):
        # First increment row count to add new row
        if self.Total_Lectures<10:
            self.LectureTable.setRowCount(self.Total_Lectures + 1)
            self.LectureTable.setRowHeight(self.Total_Lectures, 40)

            # Create widgets with unique object names
            Start_Time = QTimeEdit()
            Start_Time.setObjectName(f'StartTime_{self.Total_Lectures}')
            Start_Time.setFixedSize(QSize(100,30))
            
            Start_Time.timeChanged.connect(self.UpdateTotalTime)

            End_Time = QTimeEdit()
            End_Time.setObjectName(f'End_Time_{self.Total_Lectures}')

            Total_Time = QLabel()
            Total_Time.setObjectName(f'Total_Time_{self.Total_Lectures}')

            Del_Lecture_Button = QPushButton()
            Del_Lecture_Button.setObjectName(f'Del_Lecture_Button_{self.Total_Lectures}')
            icon = QIcon()
            icon.addFile(u":/image 4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            Del_Lecture_Button.setIcon(icon)
            Del_Lecture_Button.setIconSize(QSize(20, 20))
            
            Del_Lecture_Button.clicked.connect(self.DeleteCurrentLecture)


            # Insert widgets into table
            Elements_to_Insert = [Start_Time, End_Time, Total_Time, Del_Lecture_Button]
            col = [0,1,2,3]
            for col, widget in zip(col,Elements_to_Insert):
                self.LectureTable.setCellWidget(self.Total_Lectures, col, widget)

            # Increment total lectures counter
            self.Total_Lectures += 1

    # For Deleting the Lecture Slot
    def DeleteCurrentLecture(self):
        # checking that which lecture to delete
        Current_Lecture = int( self.sender().objectName()[-1])
        # deleting that row (extracted in above line)
        self.LectureTable.removeRow(Current_Lecture)
        
        # now changing the names of all the next widgets in table(to change the idx hidden in their name)
        for row in range(Current_Lecture+1, self.Total_Lectures):
            new_idx = row
            for col in range(0,4):
                widget = self.LectureTable.itemAt(row,col)
                if widget:
                    base_name = '_'.join(widget.objectName().split('_')[:-1])
                    widget.setObjectName(f'{base_name}_{new_idx}')
        
        # finally, decrementing the total lectures
        self.Total_Lectures = self.Total_Lectures-1
    
    # For Updating Total time consumed for lecture
    def UpdateTotalTime(self):
        pass
                  

        
# -------------------------------------------------------------------------------------------     
    # ****           Logic Functions For "SetUp Classes" page        *****
    
    # FOr Adding More Sections of same semester
    def addMoreSections(self):
        pass
    
    # FOr manageing 'Departments'
    def manageDepartments(self):
        pass
    # FOr manageing 'Degree'
    def manageDegree(self):
        pass
    # FOr manageing 'Disciplines'
    def manageDisciplines(self):
        pass
    # FOr Saving the Classes Setup
    def saveClassesSetup(self):
        pass