from dependency_injector import containers, providers

from nan_value_filler.classes.facade_nan_value_filler import FacadeNanValueFiller
from nan_value_filler.classes.input_validator.input_validator_impl import InputValidatorImpl
from nan_value_filler.classes.nan_filler.fill_with_max import FillWithMaxValue
from nan_value_filler.classes.nan_filler.fill_with_mean import FillWithMeanValue
from nan_value_filler.classes.nan_filler.fill_with_min import FillWithMinValue
from nan_value_filler.classes.nan_filler.fill_with_missing_value_category import FillWithMissingValueCategory
from nan_value_filler.classes.nan_filler.fill_with_predictor.fill_with_knn import FillWithKNN
from nan_value_filler.classes.nan_filler.fill_with_predictor.fill_with_logistic_regression import \
    FillWithLogisticRegression
from nan_value_filler.classes.nan_filler.fill_with_predictor.fill_with_multiple_linear_regression import FillWithMultipleLinearRegression
from nan_value_filler.classes.nan_filler.fill_with_zero import FillWithZero


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(InputValidatorImpl)

    # nan fillers
    fill_with_max = providers.Factory(FillWithMaxValue)
    fill_with_mean = providers.Factory(FillWithMeanValue)
    fill_with_min = providers.Factory(FillWithMinValue)
    fill_with_zero = providers.Factory(FillWithZero)
    fill_with_multiple_linear_regression = providers.Factory(FillWithMultipleLinearRegression)
    fill_with_logistic_regression = providers.Factory(FillWithLogisticRegression)
    fill_with_missing_value_category_name = providers.Factory(FillWithMissingValueCategory)
    fill_with_knn = providers.Factory(FillWithKNN)

    nan_value_filler = providers.Factory(FacadeNanValueFiller, input_validator=input_validator(),
                                         nan_fillers=[fill_with_max(),
                                                      fill_with_mean(),
                                                      fill_with_min(),
                                                      fill_with_zero(),
                                                      fill_with_multiple_linear_regression(),
                                                      fill_with_missing_value_category_name(),
                                                      fill_with_logistic_regression(),
                                                      fill_with_knn()])
