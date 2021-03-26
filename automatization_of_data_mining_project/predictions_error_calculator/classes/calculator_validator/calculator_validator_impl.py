from predictions_error_calculator.classes.calculator_validator.calculator_validator import CalculatorValidator
from predictions_error_calculator.exceptions.predictions_error_calculator_exceptions import WrongInputFormatError, \
    NonIterableObjectError


class CalculatorValidatorImpl(CalculatorValidator):
    def validate_input(self, actual_values, predicted_values):
        self.check_is_none(actual_values, predicted_values)
        self.check_is_iterable(actual_values, predicted_values)

    def check_is_iterable(self, actual_values, predicted_values):
        if not isinstance(actual_values, list):
            raise NonIterableObjectError
        if not isinstance(predicted_values, list):
            raise NonIterableObjectError

    def check_is_none(self, actual_values, predicted_values):
        if actual_values is None or predicted_values is None:
            raise WrongInputFormatError
