class MLModel:
    def __init__(self, model_id: int, name: str, description: str, cost_per_prediction: float, version: str):
        self._model_id = model_id
        self._name = name
        self._description = description
        self._cost_per_prediction = cost_per_prediction
        self._version = version

    @property
    def model_id(self):
        return self._model_id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def cost_per_prediction(self):
        return self._cost_per_prediction

    @property
    def version(self):
        return self._version
