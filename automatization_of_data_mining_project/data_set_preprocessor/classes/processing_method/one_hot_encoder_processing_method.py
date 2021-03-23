from data_set_preprocessor.classes.processing_method.processing_method import ProcessingMethod
import pandas


class OneHotEncoderProcessingMethod(ProcessingMethod):
    def process_data_set(self, data_set):
        processed_data_set = data_set.copy()
        categorical_columns = self.get_non_numerical_columns(processed_data_set)

        if categorical_columns:
            processed_data_set = self.encode_dataset(categorical_columns, processed_data_set)

        return processed_data_set

    def get_non_numerical_columns(self, processed_data_set):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        numerical_columns = list(processed_data_set.select_dtypes(include=numerics).columns)
        categorical_columns = list(set(processed_data_set.columns.tolist()) - set(numerical_columns))
        return categorical_columns

    def encode_dataset(self, categorical_columns, processed_data_set):
        dummies = pandas.get_dummies(processed_data_set[categorical_columns])
        processed_data_set = pandas.concat([processed_data_set, dummies], axis=1)
        processed_data_set = processed_data_set.drop(categorical_columns, axis=1)
        return processed_data_set
