#    This file is part of zBrac.
#
#    zBrac is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    zBrac is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with zBrac.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

#import zbrac.mainwindow
import zbrac.functions as functions
from zbrac.mainwindow import Ui_MainWindow

available_encodings = {
    'West Europe(ISO-8859-1)': 'ISO-8859-1'
    , 'Central and Eastern Europe(ISO-8859-2)': 'ISO-8859-2'
    , 'Esperanto, Maltese(ISO-8859-3)': 'ISO-8859-3'
    , 'Baltic languagues(ISO-8859-4)': 'ISO-8859-4'
    , 'Bulg., Byel., Maced., Russ., Serb.(ISO-8859-5)': 'ISO-8859-5'
    , 'Arabic(ISO-8859-6)': 'ISO-8859-6'
    , 'Greek(ISO-8859-7)': 'ISO-8859-7'
    , 'Hebrew(ISO-8859-8)': 'ISO-8859-8'
    , 'Turkish(ISO-8859-9)': 'ISO-8859-9'
    , 'Nordic languages(ISO-8859-10)': 'ISO-8859-10'
    , 'Baltic languages(ISO-8859-13)': 'ISO-8859-13'
    , 'Celtic languages(ISO-8859-14)': 'ISO-8859-14'
    , 'Western Europe(ISO-8859-15)': 'ISO-8859-15'
    }


titletext = "zBrac 1.0.4"

opening_credits = titletext + """ 
Copyright © 2018, Ali Seyhun Saral and Anna Schröter
Licensed under GNU General Public License v3.0 
----------------------------------------------------------
zBrac is an open-source project: it is free to use, to modify and to distribute. Everyone is welcome to contribute to the source code as well. If you use zBrac for your scientific study, although it is not obligatory to cite the software, it is appreciated. 

Please check the documentation for more information about the project and for the proper citation format.
----------------------------------------------------------
"""

description_CL = """Creates a language file from an exported treatment file (txt). zBrac recognizes only the text in treatment file that are wrapped in double brackets. For instance: [[this is a text]].

The files that are generated with this function can later be used for translations/text replacement.
"""

description_IL = """
Generates zTree treatment file from an exported zTree file(txt) and a language file (xlsx) in the target language. The first column of the language file should refer to keys that are in treatment file.
"""

description_SB = """
Removes double brackets from the file. You can use this option if your zTree file is already in the language you desire. This option is useful if you are coding your zTree files with brackets by default and you would like to see how it looks without them. 
"""

acknowledgements = """
-------------------- Acknowledgements --------------------
zBrac is designed and built at the Max Planck Institute for Research on Collective Goods. We used Python 3.6 and Qt5 to build it. We would like to thank open-source community for making it possible. 

We would like to thank Zvonimir Bašić, Brian Cooper, Andreas Drichoutis, Zwetelina Iliewa, Matteo Ploner, Piero Ronzani, Marco Tecilla and Fabian Winter for their valuable comments and/or for their help. 

zBrac is a Free/Open-Source project and everyone is welcome to contribute. Click on "Documentation" for more information.
----------------------------------------------------------
"""



class ConsoleStream(QObject):
    message = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ConsoleStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

    def flush(self):
        pass


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.home = home

        ### Create Language File (CL) Items
        # TODO: Create filetype handling function. The filetype definitions are not the nicest way to implement, but we have to roll out soon, we can just handle it after the release.
        self.ui.button_treatment_CL.clicked.connect(lambda: self.browse_file(self.ui.line_treatment_CL,"Text files (*.txt);;All Files(*.*)"))
        self.ui.button_generate_CL.clicked.connect(self.generate_language)
        self.ui.combo_encoding_CL.addItems(list(available_encodings))

        ### Implement Language (IL) Items
        self.ui.button_treatment_IL.clicked.connect(lambda: self.browse_file(self.ui.line_treatment_IL,"Text files (*.txt);;All Files(*.*)"))
        self.ui.button_language_IL.clicked.connect(lambda: self.browse_file(self.ui.line_language_IL,"Excel files (*.xlsx);;Excel 97-2013 Files (*.xls);;All Files(*.*)"))
        self.ui.button_generate_IL.clicked.connect(self.generate_treatment)
        self.ui.combo_encoding_input_IL.addItems(list(available_encodings))
        self.ui.combo_encoding_output_IL.addItems(list(available_encodings))

        ### Strip Brackets (SB) Items
        self.ui.button_treatment_SB.clicked.connect(lambda: self.browse_file(self.ui.line_treatment_SB,"Text files (*.txt);;All Files(*.*)"))
        self.ui.button_generate_SB.clicked.connect(self.generate_stripped)
        self.ui.combo_encoding_SB.addItems(list(available_encodings))

        ### Left side buttons
        self.ui.button_documentation.clicked.connect(self.on_pushButtonPrint_clicked)
        self.ui.button_ack.clicked.connect(self.print_ack)
        self.ui.check_description.stateChanged.connect(self.description_changed)
        self.show()
        
        ### Descriptions
        self.ui.label_description_CL.hide()
        self.ui.label_description_IL.hide()
        self.ui.label_description_SB.hide()

        ### Initial texts
        self.setWindowTitle(titletext)
        self.ui.text_console.setPlainText(opening_credits)
        self.ui.label_description_CL.setText(self.text_format_desc(description_CL))
        self.ui.label_description_IL.setText(self.text_format_desc(description_IL))
        self.ui.label_description_SB.setText(self.text_format_desc(description_SB))


    def print_ack(self):
        print(acknowledgements)


    def pop_error(self, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setWindowTitle('Error')
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()

        
    def browse_file(self, target, filetypetext):
        previous_path = target.text()
        filepath_dialog = QFileDialog.getOpenFileName(self, 'Open file', self.CURRENTWD, filetypetext)
        
        if not (filepath_dialog[0]):
            return
        filepath = os.path.abspath(filepath_dialog[0])
        target.setText(filepath)
        self.CURRENTWD = os.path.dirname(filepath)

        
    def description_changed(self):
        if self.ui.check_description.isChecked():
            self.ui.label_description_CL.show()
            self.ui.label_description_IL.show()
            self.ui.label_description_SB.show()
        else:
            self.ui.label_description_CL.hide()
            self.ui.label_description_IL.hide()
            self.ui.label_description_SB.hide()

            
    def text_format_desc(self,text):
        prefix = "<html><head/><body><p><span style=\" font-size:7pt; font-weight:500;color:#787878\">"
        suffix = "</span></p></body></html>"
        return(prefix + text + suffix)

    
    def generate_language(self):
        treatment_path = self.ui.line_treatment_CL.text()
        treatment_encoding = available_encodings[str(self.ui.combo_encoding_CL.currentText())]
        if (not (os.path.isfile(treatment_path))):
            self.pop_error('The path do not exist')
            return (False)
        source_text = functions.load_treatment_file(treatment_path, treatment_encoding)
        matched_entries = functions.get_matched_entries(source_text)
        if not matched_entries:
            self.pop_error('The file doesn\'t contain any bracketed text \n Did you add [[.]] around the text you want to change? ')
            print('aborting...')
            print('')
            return (False)
        filedialog = QFileDialog()
        filedialog.setDefaultSuffix('.xlsx')  
        save_path_dialog = filedialog.getSaveFileName(self, "Save File", self.CURRENTWD, "Excel files (*.xlsx)");
        if (not save_path_dialog[0]):
                return
        save_path = os.path.abspath(save_path_dialog[0])
        if  (not os.path.splitext(save_path)[1] in ['.xlsx','.xls']):
            save_path = save_path + ".xlsx"
            
        if (save_path == ''):
            self.pop_error('No save path. No files have been created.')
            pass
        elif (not (os.access(os.path.dirname(save_path), os.W_OK))):
            self.pop_error('There was an error saving to this path. Please check that you have proper access')

        else:
            language_list = functions.create_own_list(matched_entries)
            functions.list_to_xlsx(language_list, save_path)


    def generate_treatment(self):
        path_treatment_in = self.ui.line_treatment_IL.text()
        path_language_in = self.ui.line_language_IL.text()
        treatment_encoding_input = available_encodings[str(self.ui.combo_encoding_input_IL.currentText())]
        treatment_encoding_output = available_encodings[str(self.ui.combo_encoding_output_IL.currentText())]
        if (not (os.path.isfile(path_treatment_in))):
            self.pop_error('Problem with the treatment file')

        elif (not (os.path.isfile(path_language_in))):
            self.pop_error('Problem with the language file')

        else:

            filedialog = QFileDialog()
            filedialog.setDefaultSuffix('.txt')
            save_path_dialog = filedialog.getSaveFileName(self, "Save File", self.CURRENTWD, "Text files (*.txt)")
            
            if (not save_path_dialog[0]):
                return
            save_path = os.path.abspath(save_path_dialog[0])
            if not (os.path.splitext(save_path)[1]):
                save_path = save_path + ".txt"
            if (not (os.access(os.path.dirname(save_path), os.W_OK))):
                self.pop_error('Wrong save path')

            else:
                strip_unmatched = self.ui.check_strip_unmatched.isChecked()

                functions.implement_language_file(path_treatment_in, path_language_in, save_path, strip_unmatched,treatment_encoding_input,treatment_encoding_output)


    def generate_stripped(self):
        path_treatment_in = self.ui.line_treatment_SB.text()
        treatment_encoding = available_encodings[str(self.ui.combo_encoding_SB.currentText())]

        if (not (os.path.isfile(path_treatment_in))):
            self.pop_error('Problem with the treatment file')
            return
        
        source_text = functions.load_treatment_file(path_treatment_in, treatment_encoding)
        matched_entries = functions.get_matched_entries(source_text)
        if not matched_entries:
            self.pop_error('No brackets exist in the source file')
            return (False)

        else:

            filedialog = QFileDialog()
            filedialog.setDefaultSuffix('.txt')
            save_path_dialog = filedialog.getSaveFileName(self, "Save File", self.CURRENTWD, "Text files (*.txt)");
            if (not save_path_dialog[0]):
                return

            save_path = os.path.abspath(save_path_dialog[0])

            if not (os.path.splitext(save_path)[1]):
                save_path = save_path + ".txt"

            if (not (os.access(os.path.dirname(save_path), os.W_OK))):
                self.pop_error('Wrong save path')
            else:
                functions.strip_brackets_file(path_treatment_in, save_path, treatment_encoding)

                
    @pyqtSlot()
    def on_pushButtonPrint_clicked(self):
        webbrowser.open_new_tab("https://github.com/seyhunsaral/zBrac/")

        
    @pyqtSlot(str)
    def on_ConsoleStream_message(self, message):
        self.ui.text_console.moveCursor(QTextCursor.End)
        self.ui.text_console.insertPlainText(message)


def startgui():
    app = QApplication(sys.argv)
    # == Config management - Enter
    # TODO Create a nice function
    HOMED = os.path.expanduser("~")
    config_dir = os.path.join(HOMED,".config","zbrac")
    config_filepath = os.path.join(config_dir,"zbrac.conf")
    if (os.path.isfile(config_filepath)):
        config_file = open(config_filepath, "r")
        MyWindow.CURRENTWD = config_file.readline()
        config_file.close()
    else:
        MyWindow.CURRENTWD = os.getcwd()
    # == 

    window = MyWindow()
    consolestream = ConsoleStream()
    consolestream.message.connect(window.on_ConsoleStream_message)

    sys.stdout = consolestream
    
    end = app.exec_()
    # == Config management - Exit
    if not os.path.exists(config_dir):
            os.makedirs(config_dir)
    config_file = open(config_filepath,'w')
    config_file.write(window.CURRENTWD)
    config_file.close()
    # == 

    sys.exit(end)
