import pandas
from sklearn.preprocessing import MinMaxScaler

from data_set_preprocessor.classes.processing_method.processing_method import ProcessingMethod
from data_set_preprocessor.exceptions.preprocessor_exceptions import CanNotScaleStringValueError


class MinMaxScalerProcessingMethod(ProcessingMethod):
    def process_data_set(self, data_set):
        processed_data_set = data_set.copy()
        categorical_columns = self.get_non_numerical_column_names(processed_data_set)

        if categorical_columns:
            raise CanNotScaleStringValueError

        processed_data_set = self.scale_data_set(processed_data_set)

        return processed_data_set

    def get_non_numerical_column_names(self, processed_data_set):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'uint8']
        numerical_columns = list(processed_data_set.select_dtypes(include=numerics).columns)
        categorical_columns = list(set(processed_data_set.columns.tolist()) - set(numerical_columns))
        return categorical_columns

    def scale_data_set(self, processed_data_set):
        scaler = MinMaxScaler()
        processed_data_set = pandas.DataFrame(scaler.fit_transform(processed_data_set),
                                              columns=processed_data_set.columns)
        return processed_data_set