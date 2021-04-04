import itertools

import numpy
import pandas

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from data_set_preprocessor import Preprocessor
from data_set_preprocessor.classes.processing_method.one_hot_encoder_processing_method import \
    OneHotEncoderProcessingMethod
from prediction_module import PredictorFactory


class FillWithPredictor(object):
    def fill_nan_values(self, data_set_info, filling_column_name, predictor_method):
        data_set_with_needed_columns = self.get_only_columns_needed_for_fill(data_set_info, filling_column_name)
        data_set_preprocessor = self.get_data_set_preprocessor()

        preprocessed_data_set_with_needed_columns = data_set_preprocessor.get_preprocessed_data(data_set_with_needed_columns)

        data_frame_with_missing_data, non_missing_data = self.split_data_with_and_without_missing_values(
            preprocessed_data_set_with_needed_columns, filling_column_name)

        preprocessed_data_set = self.get_preprocessed_data_set(data_set_info, data_set_preprocessor,
                                                               filling_column_name, non_missing_data)

        predictor_model = self.get_fitted_model(predictor_method, preprocessed_data_set)

        updated_data_frame = self.fill_missing_data(data_frame_with_missing_data, data_set_info, data_set_preprocessor,
                                                    filling_column_name, predictor_model)

        data_set_info.data_set = updated_data_frame

        return data_set_info

    def get_only_columns_needed_for_fill(self, data_set_info, filling_column_name):
        columns_to_include = data_set_info.must_contained_columns.copy()
        columns_to_include.append(filling_column_name)
        data_set_with_needed_columns = data_set_info.data_set[columns_to_include]
        return data_set_with_needed_columns

    def get_data_set_preprocessor(self):
        one_hot_encode_processing_method = OneHotEncoderProcessingMethod()
        data_set_preprocessor = Preprocessor(processing_methods=[one_hot_encode_processing_method])
        return data_set_preprocessor

    def split_data_with_and_without_missing_values(self, data_set_with_needed_columns, filling_column_name):
        non_missing_data = data_set_with_needed_columns[data_set_with_needed_columns[filling_column_name].notna()]
        data_frame_with_missing_data = data_set_with_needed_columns[
            data_set_with_needed_columns[filling_column_name].isna()]
        return data_frame_with_missing_data, non_missing_data

    def get_preprocessed_data_set(self, data_set_info, data_set_preprocessor, filling_column_name, non_missing_data):
        x_data_columns = list(set(non_missing_data.columns.tolist()) - set(data_set_info.other_column_names))
        x_data = non_missing_data[x_data_columns]
        y_data = non_missing_data[[filling_column_name]]
        preprocessed_data_set: PreprocessedDataSetInfo = data_set_preprocessor.get_train_test_split_of_data_set(
            x_data, y_data, 0.2)
        return preprocessed_data_set

    def get_fitted_model(self, predictor_method, preprocessed_data_set):
        predictor_factory = PredictorFactory()
        predictor_model = predictor_factory.get_fitted_predictor_by_name(preprocessed_data_set, predictor_method)
        return predictor_model

    def fill_missing_data(self, data_frame_with_missing_data, data_set_info, data_set_preprocessor, filling_column_name,
                          predictor_model):
        filled_rows = []
        # preprocess x_data
        x_data_columns = list(set(data_frame_with_missing_data.columns.tolist()) - set(data_set_info.other_column_names))

        preprocessed_missing_data_rows = data_frame_with_missing_data[x_data_columns]

        whole_data_frame_with_missing_data_on_column_to_fill = data_set_info.data_set[data_set_info.data_set[filling_column_name].isna()]
        for processed_row, actual_row in itertools.zip_longest(preprocessed_missing_data_rows.values, whole_data_frame_with_missing_data_on_column_to_fill.values):
            predicted_value = predictor_model.predict([processed_row])
            new_row = self.update_value(actual_row, whole_data_frame_with_missing_data_on_column_to_fill, filling_column_name, predicted_value)
            filled_rows.append(new_row)

        whole_data_frame_without_missing_data_on_column_to_fill = data_set_info.data_set[data_set_info.data_set[filling_column_name].notna()]
        updated_data_frame = self.get_updated_data_frame(data_set_info, filled_rows, whole_data_frame_without_missing_data_on_column_to_fill)

        return updated_data_frame

    def update_value(self, actual_row, data_frame_with_missing_data, filling_column_name, predicted_value):
        filling_column_index = data_frame_with_missing_data.columns.get_loc(filling_column_name)
        new_row = actual_row.copy()
        new_row[filling_column_index] = predicted_value.flat[0]
        return new_row

    def get_updated_data_frame(self, data_set_info, filled_rows, non_missing_data):
        updated_data_frame_values = []
        for non_missing_data_row in non_missing_data.values:
            updated_data_frame_values.append(non_missing_data_row)

        for filled_row in filled_rows:
            updated_data_frame_values.append(filled_row)

        updated_data_frame = pandas.DataFrame(updated_data_frame_values,
                                              columns=data_set_info.data_set.columns.tolist())
        return updated_data_frame
