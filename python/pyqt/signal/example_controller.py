from PyQt5.QtCore import QObject, pyqtSlot

class ExampleController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._model.data_changed.connect(self.example_slot)

    @pyqtSlot()
    def example_slot(self):
        print("Slot was called")
