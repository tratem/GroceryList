from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QCheckBox, QScrollArea)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize 
from CustomWidgets.custom_widgets import *

class GroceryList(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grocery List")
        self.setMinimumSize(300, 700)
        self.setStyleSheet("background-color: white")
        self.setWindowIcon(QIcon(r".\images\Logo.png"))

        self.init_UI()

    def init_UI(self):
        self.main_layout = QVBoxLayout()

        main_window_scroll = QScrollArea()
        main_window_widget = QWidget()
        main_window_widget.setLayout(self.main_layout)
        main_window_scroll.setWidgetResizable(True)
        main_window_scroll.setWidget(main_window_widget)
        self.setCentralWidget(main_window_scroll)

        self.create_add_new_item_group()

        self.items_layout = QVBoxLayout() 
        self.main_layout.addLayout(self.items_layout)

        buttons_layout = QHBoxLayout()
        select_all_button = CustomButton('SelectAll', background_color="#63CE43", height=50)
        select_all_button.clicked.connect(self.handle_select_all_clicked)
        clear_all_button = CustomButton('ClearAll', background_color="#B6131B", height=50)
        clear_all_button.clicked.connect(lambda: clear_layout(self.items_layout))
        buttons_layout.addWidget(select_all_button)
        buttons_layout.addWidget(clear_all_button)
        self.main_layout.addLayout(buttons_layout)

    def create_add_new_item_group(self):
        add_new_item_line_edit = CustomLineEdit("ADD NEW ITEM...", height = 50)
        add_new_item_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        add_new_item_line_edit.setStyleSheet("""
                                             color: black;
                                             background-color: #BAD6F0;
                                             font-size: 12px;
                                             border-radius: 20px;""")
        add_new_item_line_edit.returnPressed.connect(self.handle_addition_new_item)

        self.main_layout.addWidget(add_new_item_line_edit, alignment=Qt.AlignmentFlag.AlignTop)

    def handle_addition_new_item(self):
        '''Insertion of new item to the list'''
        item_text = self.sender().text()
        self.sender().clear()
        item_layout = QHBoxLayout()

        item_check_box = QCheckBox(item_text)
        remove_item_button = QPushButton()
        remove_item_button.setIcon(QIcon(r".\images\Trash.png"))
        remove_item_button.setIconSize(QSize(20, 20))
        remove_item_button.setFlat(True)
        remove_item_button.clicked.connect(self.remove_item)

        item_layout.addWidget(item_check_box, alignment=(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop))
        item_layout.addWidget(remove_item_button, alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop))
        self.items_layout.addLayout(item_layout, stretch=10)

    def handle_select_all_clicked(self):
        for i in range(self.items_layout.count()):
            item_layout = self.items_layout.itemAt(i) # single hbox layout
            
            for j in range(item_layout.count()):
                item = item_layout.itemAt(j)
                widget = item.widget()
                if isinstance(widget, QCheckBox):
                    widget.setChecked(True)

    def remove_item(self):
        # Fix
        for i in range(self.items_layout.count()):
            item_layout = self.items_layout.itemAt(i)

            for j in range(item_layout.count()):
                item = item_layout.itemAt(j)
                widget = item.widget()
                if self.sender() == widget:
                    clear_layout(item_layout)