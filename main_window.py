from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QCheckBox, QScrollArea)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize 
from CustomWidgets.custom_widgets import *

# For future implementation: add possibility to edit items after adding to the list 

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

        main_window_widget = QWidget()
        main_window_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_window_widget)

        self.create_add_new_item_line_edit()
        self.create_scroll_area()
        self.create_buttons_layout()

    def create_add_new_item_line_edit(self):
        add_new_item_line_edit = CustomLineEdit("ADD NEW ITEM...", height = 50)
        add_new_item_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        add_new_item_line_edit.setStyleSheet("""
                                             color: black;
                                             background-color: #BAD6F0;
                                             font-size: 12px;
                                             border-radius: 20px;""")
        add_new_item_line_edit.returnPressed.connect(self.handle_addition_new_item)

        self.main_layout.addWidget(add_new_item_line_edit, alignment=Qt.AlignmentFlag.AlignTop)

    def create_scroll_area(self):
        self.items_scroll_area = QScrollArea()
        self.items_scroll_area.setWidgetResizable(True)
        
        # Container widget
        self.scroll_content_widget = QWidget()
        self.items_layout = QVBoxLayout(self.scroll_content_widget)
        self.items_layout.setAlignment(Qt.AlignmentFlag.AlignTop) # Keeps items pushed to the top
        
        self.items_scroll_area.setWidget(self.scroll_content_widget)        
        self.main_layout.addWidget(self.items_scroll_area)

    def create_buttons_layout(self):
        '''Select All and Clear List buttons'''
        buttons_layout = QHBoxLayout()
        select_all_button = CustomButton('Select All', background_color="#63CE43", height=50)
        select_all_button.clicked.connect(self.handle_select_all_clicked)
        clear_all_button = CustomButton('Clear List', background_color="#B6131B", height=50)
        clear_all_button.clicked.connect(lambda: clear_layout(self.items_layout))
        buttons_layout.addWidget(select_all_button)
        buttons_layout.addWidget(clear_all_button)
        self.main_layout.addLayout(buttons_layout)

    def handle_addition_new_item(self):
        '''Insertion of new item to the list'''
        item_text = self.sender().text()
        if item_text:
            self.sender().clear()
            item_layout = QHBoxLayout()

            item_check_box = QCheckBox(item_text)  
            item_check_box.stateChanged.connect(lambda: self.update_item_style(item_check_box))

            remove_item_button = QPushButton()
            remove_item_button.setIcon(QIcon(r".\images\Trash.png"))
            remove_item_button.setIconSize(QSize(20, 20))
            remove_item_button.setFlat(True)
            remove_item_button.clicked.connect(self.remove_item)

            item_layout.addWidget(item_check_box, alignment=(Qt.AlignmentFlag.AlignLeft))
            item_layout.addWidget(remove_item_button, alignment=(Qt.AlignmentFlag.AlignRight))
            self.items_layout.addLayout(item_layout)

    def update_item_style(self, checkbox):
        '''Visual representation that an item was already checked'''
        if checkbox.isChecked():
            # Set text to dark gray and maybe strikeout
            checkbox.setStyleSheet("color: #808080; text-decoration: line-through;")
        else:
            # Revert to black
            checkbox.setStyleSheet("color: black; text-decoration: none;")

    def handle_select_all_clicked(self):
        for i in range(self.items_layout.count()):
            item_layout = self.items_layout.itemAt(i) # single hbox layout
            
            for j in range(item_layout.count()):
                item = item_layout.itemAt(j)
                widget = item.widget()
                if isinstance(widget, QCheckBox):
                    widget.setChecked(True)

    def remove_item(self):
        '''Handler for trashing an item from the list'''
        for i in range(self.items_layout.count()):
            item_layout = self.items_layout.itemAt(i)

            for j in range(item_layout.count()):
                item = item_layout.itemAt(j)
                widget = item.widget()
                if self.sender() == widget:
                    clear_layout(item_layout)