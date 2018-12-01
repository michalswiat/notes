class ExampleModel:
    def __init__(self):
        self._model_data = 0

    @property
    def model_data(self):
        print("Getting value")
        return self._model_data

    @model_data.setter
    def model_data(self, value):
        print("Setting value")
        self._model_data = value

if __name__== '__main__':
    model = ExampleModel()
    x = model.model_data
    model.model_data = x

