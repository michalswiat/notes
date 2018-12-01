from example_model import ExampleModel
from example_controller import ExampleController

model = ExampleModel()
controller = ExampleController(model)

model.data_was_changed()
