from prediction_module.classes.facade_predictor import FacadePredictor
from prediction_module.depedency_injector.container import Container

PredictorFactory: FacadePredictor = Container.facade_predictions_module
