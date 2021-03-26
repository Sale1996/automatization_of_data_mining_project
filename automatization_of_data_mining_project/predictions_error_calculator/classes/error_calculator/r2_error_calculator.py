from sklearn.metrics import r2_score

from predictions_error_calculator.classes.data_class.error_score import ErrorScore
from predictions_error_calculator.classes.error_calculator.error_calculator import ErrorCalculator


class R2ErrorCalculator(ErrorCalculator):
    def calculate_error(self, actual_values, predicted_values):
        r2_error_result = round(r2_score(actual_values, predicted_values), 3)
        r2_error_score_object = ErrorScore("R2", r2_error_result)

        return r2_error_score_object
