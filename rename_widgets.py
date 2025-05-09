import re
import fileinput
import os
from xml.etree import ElementTree as ET

class WidgetRenamer:
    def __init__(self):
        self.rename_mappings = {
            # Main Windows and Containers
            'MainWindow': 'main_window',
            'MainContentBody': 'main_container',
            'LeftMenu': 'menu_left',
            'Header': 'header_container',
            'Footer': 'footer_container',
            'ButtonFrame': 'button_frame',
            'middlebuttons': 'middle_menu',
            
            # Pages/Views
            'TimetablePage': 'timetable_view',
            'DatesheetPage': 'datesheet_view',
            'UserInputPage': 'input_view',
            'WorkingDaysPage': 'workdays_view',
            'LectureTimePage': 'lecturetime_view',
            'SetupClasses': 'classes_view',
            'SetUpRooms': 'rooms_view',
            
            # Navigation Buttons  
            'TimetableButton': 'timetable_btn',
            'DatesheetButton': 'datesheet_btn',
            'SetWeekDays': 'weekdays_btn',
            'SetLectures': 'lectures_btn',
            'SetClasses': 'classes_btn',
            'SetRooms': 'rooms_btn',
            'SetCourses': 'courses_btn',
            
            # Control Buttons
            'LogoButton': 'logo_btn',  
            'Close_window_Button': 'close_btn',
            'Minimize_Button': 'minimize_btn',
            'Fullscreen_Button': 'maximize_btn',
            'ExpandMenuButton': 'expandmenu_btn',
            'ContactUsButton': 'contactus_btn',
            'SettingButton': 'settings_btn',
            
            # Form Elements
            'Department_Input_Combobox': 'department_cmb',
            'LevelInput_Combobox': 'level_cmb', 
            'Discipline_Input_Combobox': 'discipline_cmb',
            'ProjectNameInput': 'projectname_txt',
            
            # Tables
            'LectureTable': 'lectures_tbl',
            'SectionTable': 'sections_tbl',
            
            # Labels
            'HeaderMiddleLabel_2': 'title_lbl',
            'Project_Label': 'projectname_lbl',
            'FooterMiddleLabel': 'footer_lbl',
            'Total_Time': 'totaltime_lbl',
            
            # Action Buttons
            'AddMoreLecture_Button': 'addlecture_btn',
            'CloseProject_Button': 'closeproject_btn',
            'Del_Lecture_Button': 'deletelecture_btn',
            'StartProjectButton': 'startproject_btn',
            
            # Navigation Controls
            'PreviousButton_1': 'previous_btn',
            'NextButton_1': 'next_btn',
            'PreviousButton_Label_1': 'previous_lbl',
            'NextButton_Label_1': 'next_lbl',
            
            # TimeEdits
            'StartTime': 'start_time',
            'End_Time': 'end_time'
        }

    def rename_in_python_file(self, filepath):
        print(f"Processing Python file: {filepath}")
        with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
            for line in file:
                new_line = line
                for old_name, new_name in self.rename_mappings.items():
                    pattern = r'\b' + old_name + r'\b'
                    new_line = re.sub(pattern, new_name, new_line)
                print(new_line, end='')

    def rename_in_ui_file(self, filepath):
        print(f"Processing UI file: {filepath}")
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # Create backup of UI file
        backup_path = filepath + '.bak'
        tree.write(backup_path)
        
        # Function to process XML elements
        def process_element(elem):
            if 'name' in elem.attrib:
                old_name = elem.attrib['name']
                if old_name in self.rename_mappings:
                    elem.attrib['name'] = self.rename_mappings[old_name]
            
            # Process objectName properties
            for prop in elem.findall(".//property[@name='objectName']"):
                if prop.text in self.rename_mappings:
                    prop.text = self.rename_mappings[prop.text]
            
            # Recursively process children
            for child in elem:
                process_element(child)
        
        # Process the entire tree
        process_element(root)
        
        # Save changes
        tree.write(filepath, encoding='UTF-8', xml_declaration=True)

    def run(self):
        base_path = r"e:\Visual Studio Code\Practice Projects\University-Timetable-using-Ai"
        files_to_update = {
            'python': [
                os.path.join(base_path, 'GUI-Files', 'ui_MainWindow.py'),
                os.path.join(base_path, 'GUI-Files', 'CMainWindow.py')
            ],
            'ui': [
                os.path.join(base_path, 'QT-designer-files', 'ui_MainWindow.ui')
            ]
        }

        # Process Python files
        for py_file in files_to_update['python']:
            try:
                self.rename_in_python_file(py_file)
                print(f"Successfully processed {py_file}")
            except Exception as e:
                print(f"Error processing {py_file}: {str(e)}")

        # Process UI files
        for ui_file in files_to_update['ui']:
            try:
                self.rename_in_ui_file(ui_file)
                print(f"Successfully processed {ui_file}")
            except Exception as e:
                print(f"Error processing {ui_file}: {str(e)}")

if __name__ == "__main__":
    renamer = WidgetRenamer()
    renamer.run()