from sklearn.metrics import mean_squared_error

from predictions_error_calculator.classes.data_class.error_score import ErrorScore
from predictions_error_calculator.classes.error_calculator.error_calculator import ErrorCalculator


class MeanSquareErrorCalculator(ErrorCalculator):
    def calculate_error(self, actual_values, predicted_values):
        mse_error_result = round(mean_squared_error(actual_values, predicted_values), 3)
        mse_error_score_object = ErrorScore("MSE", mse_error_result)

        return mse_error_score_object
