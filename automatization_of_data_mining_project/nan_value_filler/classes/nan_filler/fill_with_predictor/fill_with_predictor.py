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
        columns_to_include = data_set_info.must_contained_columns.copy()
        columns_to_include.append(filling_column_name)

        data_set_with_needed_columns = data_set_info.data_set[columns_to_include]

        non_missing_data = data_set_with_needed_columns[data_set_with_needed_columns[filling_column_name].notna()]
        data_frame_with_missing_data = data_set_with_needed_columns[
            data_set_with_needed_columns[filling_column_name].isna()]
        one_hot_encode_processing_method = OneHotEncoderProcessingMethod()
        data_set_preprocessor = Preprocessor(processing_methods=[one_hot_encode_processing_method])

        # split to x_Train, y_train
        x_data = non_missing_data[data_set_info.must_contained_columns]
        y_data = non_missing_data[[filling_column_name]]
        preprocessed_data_set: PreprocessedDataSetInfo = data_set_preprocessor.get_train_test_split_of_data_set(
            x_data, y_data, 0.2)

        # preprocess data sets
        preprocessed_data_set.x_train = data_set_preprocessor.get_preprocessed_data(preprocessed_data_set.x_train)
        preprocessed_data_set.x_test = data_set_preprocessor.get_preprocessed_data(preprocessed_data_set.x_test)

        # train model on data
        predictor_factory = PredictorFactory()

        predictor_model = predictor_factory.get_fitted_predictor_by_name(preprocessed_data_set, predictor_method)

        filled_rows = []
        preprocessed_missing_data_rows = data_set_preprocessor.get_preprocessed_data(
            data_frame_with_missing_data[data_set_info.must_contained_columns])
        for processed_row, actual_row in itertools.zip_longest(preprocessed_missing_data_rows.values,
                                                               data_frame_with_missing_data.values):
            predicted_value = predictor_model.predict([processed_row])
            filling_column_index = data_frame_with_missing_data.columns.get_loc(filling_column_name)

            new_row = actual_row.copy()
            new_row[filling_column_index] = predicted_value.flat[0]
            filled_rows.append(new_row)

        filled_rows = numpy.array(filled_rows)
        updated_data_frame_values = numpy.concatenate([non_missing_data.values.copy(), filled_rows])

        updated_data_frame = pandas.DataFrame(updated_data_frame_values,
                                              columns=data_set_info.data_set.columns.tolist())

        data_set_info.data_set = updated_data_frame

        return data_set_info
