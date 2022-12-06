"""
this code creates a basic window with no layouts or widget in it 
"""

import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.spinBox = widgets.QSpinBox()

        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.setRange([0 , 10 , 1])

        

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.spinBox)

        self.show()



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
