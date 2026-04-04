from PyQt5.QtWidgets import QApplication
from main_window import GroceryList
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_class = GroceryList()
    main_class.show()
    
    sys.exit(app.exec_())