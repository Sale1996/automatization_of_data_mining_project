from dependency_injector import containers, providers

from predictions_error_calculator.classes.calculator_validator.calculator_validator_impl import CalculatorValidatorImpl
from predictions_error_calculator.classes.facade_predictions_error_calculator import FacadePredictionsErrorCalculator


class Container(containers.DeclarativeContainer):
    calculator_validator = providers.Factory(CalculatorValidatorImpl)
    predictions_error_calculator = providers.Factory(FacadePredictionsErrorCalculator,
                                                     calculator_validator=calculator_validator())
