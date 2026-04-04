from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from CustomWidgets.custom_widgets import *

class GroceryList(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grocery List")
        self.setMinimumSize(300, 700)
        self.setWindowIcon(QIcon(r".\images\Logo.png"))

        self.main_layout = QVBoxLayout()

        main_window_widget = QWidget()
        main_window_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_window_widget)

        self.create_add_new_item_group()

    def create_add_new_item_group(self):
        add_new_item_line_edit = CustomLineEdit("ADD NEW ITEM...")
        add_new_item_line_edit.returnPressed.connect(self.handle_addition_new_item)

        self.main_layout.addWidget(add_new_item_line_edit)

    def handle_addition_new_item(self):
        item_text = self.sender().text()
        item_layout = QHBoxLayout()

        item_check_box = QCheckBox(item_text)
        remove_item_button = QPushButton()
        remove_item_button.setFixedHeight(40)
        remove_item_button.setFixedWidth(40)
        remove_item_button.setIcon(QIcon(r".\images\Trash.png"))
        remove_item_button.setIconSize(QSize(40, 40))
        remove_item_button.setFlat(True)

        item_layout.addWidget(item_check_box)
        item_layout.addWidget(remove_item_button)
        self.main_layout.addLayout(item_layout)