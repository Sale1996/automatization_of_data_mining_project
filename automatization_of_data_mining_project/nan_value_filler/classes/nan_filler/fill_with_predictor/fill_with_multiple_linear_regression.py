from nan_value_filler.classes.nan_filler.fill_with_predictor.fill_with_predictor import FillWithPredictor
from nan_value_filler.classes.nan_filler.nan_filler import NanFiller


class FillWithMultipleLinearRegression(NanFiller):
    def __init__(self):
        super().__init__()
        self.name = "fill_with_multiple_linear_regression"

    def fill_nan_values(self, data_set_info, filling_column_name):
        fill_with_predictor = FillWithPredictor()

        return fill_with_predictor.fill_nan_values(data_set_info, filling_column_name, "Multiple Linear Regression")
