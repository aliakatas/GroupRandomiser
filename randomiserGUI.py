# Building with help from https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QFileDialog, QMessageBox
import os
import functions as fns
import datetime

class Randomiser(QWidget):
    def __init__(self, parent=None):
        super(Randomiser, self).__init__(parent)

        self.userhome = os.path.expanduser("~")

        openFileWidget = QWidget()
        saveFileWidget = QWidget()
        optionsWidget = QWidget()
        execWidget = QWidget()

        # Get the correct layout - top-level
        windowLayout = QVBoxLayout()
        openLayout = QHBoxLayout()
        saveToLayout = QHBoxLayout()
        optionsLayout = QHBoxLayout()
        execLayout = QHBoxLayout()

        # Create Buttons
        browseOpenButton = QPushButton('Browse')
        browseOpenButton.clicked.connect(self.openFileDialog)

        browseSaveToButton = QPushButton('Browse')
        browseSaveToButton.clicked.connect(self.saveFileDialog)
        
        runButton = QPushButton('Run')
        runButton.clicked.connect(self.createList)
        
        closeButton = QPushButton('Quit')
        closeButton.clicked.connect(self.closeMe)

        # Create data entry fields
        self.openFileEntry = QLineEdit()
        self.saveFileEntry = QLineEdit()
        self.saveFileEntry.setText(os.path.join(self.userhome, 'mygroup.csv'))

        # Create options entry
        self.sizeOfGroupEntry = QLineEdit()
        self.sizeOfGroupEntry.setText('2')
        self.allowLessInGroupOpt = QCheckBox('Allow less in group')
        self.hasHeader = QCheckBox('Has Header')
        self.hasHeader.setChecked(True)

        # Upper block
        openLayout.addWidget(QLabel('Name list:'))
        openLayout.addWidget(self.openFileEntry)
        openLayout.addWidget(browseOpenButton)
        openLayout.addWidget(self.hasHeader)
        openFileWidget.setLayout(openLayout)
        openFileWidget.show()

        # Mid block 
        saveToLayout.addWidget(QLabel('Save groups to:'))
        saveToLayout.addWidget(self.saveFileEntry)
        saveToLayout.addWidget(browseSaveToButton)
        saveFileWidget.setLayout(saveToLayout)
        saveFileWidget.show()

        # Options block
        optionsLayout.addWidget(QLabel('Group size:'))
        optionsLayout.addWidget(self.sizeOfGroupEntry)
        optionsLayout.addWidget(self.allowLessInGroupOpt)
        optionsWidget.setLayout(optionsLayout)
        optionsWidget.show()

        # Lower block
        execLayout.addWidget(runButton)
        execLayout.addWidget(closeButton)
        execWidget.setLayout(execLayout)
        execWidget.show()

        # Sort out a few more bits...
        windowLayout.addWidget(openFileWidget)
        windowLayout.addWidget(saveFileWidget)
        windowLayout.addWidget(optionsWidget)
        windowLayout.addWidget(execWidget)
        self.setLayout(windowLayout)

    #################################
    def closeMe(self):
        self.close()
    
    #################################
    def openFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', self.userhome, "CSV files (*.csv *.*)")
        if len(str(fname[0])) > 0:
            self.openFileEntry.setText(str(fname[0]))

    #################################
    def saveFileDialog(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', self.userhome, "CSV files (*.csv)")
        if len(str(fname[0])) > 0:
            self.saveFileEntry.setText(str(fname[0]))

    #################################
    def createList(self):
        msg = QMessageBox()

        dataFile = self.openFileEntry.text()
        if len(dataFile.strip()) == 0:
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f'Source file entry is empty!')
            msg.setWindowTitle('Failed')
            msg.setDetailedText('Enter a valid file name and try again.')
            msg.exec_()
            return 
        elif not os.path.exists(dataFile):    
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f'{dataFile} does not exist!')
            msg.setWindowTitle('Failed')
            msg.setDetailedText('Enter a valid file name and try again.')
            msg.exec_()
            return 

        groupFile = self.saveFileEntry.text()
        if len(groupFile.strip()) == 0:
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Target file entry is empty!')
            msg.setWindowTitle('Failed')
            msg.setDetailedText('Enter a valid file name and try again.')
            msg.exec_()
            return 
        
        groupSizeRaw = self.sizeOfGroupEntry.text()
        if not groupSizeRaw.isnumeric():
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Group size must be a number!')
            msg.setWindowTitle('Failed')
            msg.setDetailedText('Enter a valid number and try again.')
            msg.exec_()
            return 

        groupSize = int(groupSizeRaw)
        allowLess = self.allowLessInGroupOpt.isChecked()
        hasHeader = self.hasHeader.isChecked()
        startRow = 0
        if hasHeader:
            startRow = 1

        # Do the work
        ok = fns.main(dataFile, groupFile, groupSize, allowLess, start=startRow)
        if not ok:
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Operation failed!')
            msg.setWindowTitle('Failed')
            msg.setDetailedText('Reason: Group size grater than input size.')
            msg.exec_()
            return 

        fname = os.path.split(groupFile)
        now = datetime.datetime.now()
        
        msg.setIcon(QMessageBox.Information)
        msg.setText(f'{fname[1]} was created')
        msg.setWindowTitle('Success')
        msg.setDetailedText(f'Operation completed at {now.strftime("%Y-%m-%d %H:%M:%S")} \n\nRead from {dataFile} \n\nWrite to {groupFile}')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()