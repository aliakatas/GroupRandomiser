# Building with help from https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox

import sys 

if __name__ == "__main__":
    
    # General needs
    app = QApplication([])
    window = QWidget()
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
    browseSaveToButton = QPushButton('Browse')
    runButton = QPushButton('Run!')
    closeButton = QPushButton('Quit')

    # Create data entry fields
    openFileEntry = QLineEdit()
    saveFileEntry = QLineEdit()

    # Create options entry
    sizeOfGroupEntry = QLineEdit()
    allowLessInGroupOpt = QCheckBox('Allow less in group')

    # Upper block
    openLayout.addWidget(QLabel('Name list:'))
    openLayout.addWidget(openFileEntry)
    openLayout.addWidget(browseOpenButton)
    openFileWidget.setLayout(openLayout)
    openFileWidget.show()

    # Mid block 
    saveToLayout.addWidget(QLabel('Save groups to:'))
    saveToLayout.addWidget(saveFileEntry)
    saveToLayout.addWidget(browseSaveToButton)
    saveFileWidget.setLayout(saveToLayout)
    saveFileWidget.show()

    # Options block
    optionsLayout.addWidget(QLabel('Group size:'))
    optionsLayout.addWidget(sizeOfGroupEntry)
    optionsLayout.addWidget(allowLessInGroupOpt)
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
    window.setLayout(windowLayout)
    window.setWindowTitle('Group Randomiser')
    window.show()

    # Run
    sys.exit(app.exec_())
