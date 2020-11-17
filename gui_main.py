from PyQt5.QtWidgets import QApplication
from randomiserGUI import Randomiser

import sys 

if __name__ == "__main__":
    
    # General needs
    app = QApplication([])
    window = Randomiser()
    
    window.setWindowTitle('Group Randomiser')
    window.show()

    # Run
    sys.exit(app.exec_())
