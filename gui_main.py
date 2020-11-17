from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication
from randomiserGUI import Randomiser

import sys 

if __name__ == "__main__":
    
    # General needs
    appctxt = ApplicationContext()
    app = QApplication([])
    window = Randomiser()
    
    window.setWindowTitle('Group Randomiser')
    window.show()

    # Run
    exit_code = appctxt.app.exec_() 
    sys.exit(exit_code)