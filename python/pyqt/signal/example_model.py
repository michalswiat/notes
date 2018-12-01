from PyQt5.QtCore import QObject, pyqtSignal

class ExampleModel(QObject):
    data_changed = pyqtSignal()
    
    def __init__(self):
        super().__init__()

    def data_was_changed(self):
        self.data_changed.emit()
