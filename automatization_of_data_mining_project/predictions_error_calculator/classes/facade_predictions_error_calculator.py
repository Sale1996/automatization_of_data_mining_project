from typing import List

from predictions_error_calculator.classes.calculator_validator.calculator_validator import CalculatorValidator
from predictions_error_calculator.classes.error_calculator.error_calculator import ErrorCalculator
from predictions_error_calculator.classes.predictions_error_calculator import PredictionsErrorCalculator


class FacadePredictionsErrorCalculator(PredictionsErrorCalculator):
    def __init__(self, calculator_validator: CalculatorValidator,
                 error_calculators: List[ErrorCalculator]):
        self.calculator_validator = calculator_validator
        self.error_calculators = error_calculators

    def calculate_errors(self, actual_values, predicted_values):
        self.calculator_validator.validate_input(actual_values, predicted_values)

        error_scores = []

        for error_calculator in self.error_calculators:
            error_scores.append(error_calculator.calculate_error(actual_values, predicted_values))

        return error_scores
