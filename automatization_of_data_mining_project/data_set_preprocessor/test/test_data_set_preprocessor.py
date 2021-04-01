import unittest

import pandas

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from data_set_preprocessor.classes.processing_method.min_max_scaler_method import MinMaxScalerProcessingMethod
from data_set_preprocessor.classes.processing_method.one_hot_encoder_processing_method import \
    OneHotEncoderProcessingMethod
from data_set_preprocessor.depedency_injector.container import Container
from data_set_preprocessor.exceptions.preprocessor_exceptions import WrongInputFormatError, CanNotScaleStringValueError


class DataSetPreprocessorTestBase(unittest.TestCase):
    pass


class DataSetPreprocessorErrorCases(DataSetPreprocessorTestBase):
    def setUp(self):
        self.data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[])

    def test_given_nones_when_preprocess_data_set_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_preprocessor.get_preprocessed_data(None)

    def test_given_wrong_input_type_when_preprocess_data_set_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_preprocessor.get_preprocessed_data(1)

    def test_given_nones_when_get_train_validation_test_data_sets_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_preprocessor.get_train_validation_test_split_of_data_set(None, None, None)

    def test_given_wrong_input_type_get_train_validation_test_data_sets_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_preprocessor.get_preprocessed_data(1)

    def test_given_data_set_info_with_categorical_column_when_preprocess_data_set_with_scaling_then_throw_can_not_scale_string_value_error(
            self):
        data_set = get_data_set_with_category_column()
        scale_processing_method = MinMaxScalerProcessingMethod()
        data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[scale_processing_method])

        with self.assertRaises(CanNotScaleStringValueError):
            data_set_preprocessor.get_preprocessed_data(data_set)


class DataSetPreprocessorDummyCases(DataSetPreprocessorTestBase):
    def test_given_data_set_with_existing_column_when_get_train_validation_test_sets_then_return_train_validation_test_splits(
            self):
        data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[])

        data_set = get_only_numerical_data_set()

        x_columns = data_set.columns.tolist()
        x_columns.remove('Numerical Column')
        x_data = data_set[x_columns]
        y_data = data_set[['Numerical Column']]
        preprocessed_data_set_object: PreprocessedDataSetInfo = data_set_preprocessor.get_train_validation_test_split_of_data_set(
            x_data, y_data, 0.2)

        train_set_length = len(preprocessed_data_set_object.x_train)
        test_set_length = len(preprocessed_data_set_object.x_test)

        predictor_columns = preprocessed_data_set_object.x_train.columns.tolist()
        dependent_variable = preprocessed_data_set_object.y_train.columns.tolist()

        self.assertEqual(4, train_set_length)
        self.assertEqual(2, test_set_length)
        self.assertEqual(predictor_columns, ['Year'])
        self.assertEqual(dependent_variable, ['Numerical Column'])

    def test_given_data_set_with_existing_column_and_no_categorical_columns_when_preprocess_data_set_with_column_encoding_then_return_train_validation_test_splits(
            self):
        data_set = get_only_numerical_data_set()

        one_hot_encode_processing_method = OneHotEncoderProcessingMethod()
        data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[one_hot_encode_processing_method])
        preprocessed_data_set: pandas.DataFrame = data_set_preprocessor.get_preprocessed_data(
            data_set)

        predictor_columns = preprocessed_data_set.columns.tolist()

        self.assertEqual(predictor_columns, ['Year', 'Numerical Column'])

    def test_given_data_set_with_existing_column_and_with_categorical_column_when_preprocess_data_set_with_column_encoding_then_return_correct_train_validation_test_splits(
            self):
        data_set = get_only_numerical_data_set()

        scale_processing_method = MinMaxScalerProcessingMethod()
        data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[scale_processing_method])
        preprocessed_data_set: pandas.DataFrame = data_set_preprocessor.get_preprocessed_data(
            data_set)

        max_value = preprocessed_data_set.max().max()
        min_value = preprocessed_data_set.min().min()

        self.assertTrue(max_value <= 1)
        self.assertTrue(min_value >= 0)

    def test_given_data_set_with_categorical_column_when_preprocess_data_set_with_encoding_then_return_data_set_with_multiple_columns(
            self):
        data_set = get_data_set_with_category_column()

        one_hot_encode_processing_method = OneHotEncoderProcessingMethod()
        data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[one_hot_encode_processing_method])
        preprocessed_data_set: pandas.DataFrame = data_set_preprocessor.get_preprocessed_data(
            data_set)

        preprocessed_data_frame_columns = preprocessed_data_set.columns.tolist()

        self.assertEqual(4, len(preprocessed_data_frame_columns))

    def test_given_data_set_with_categorical_column_when_preprocess_data_set_with_encoding_and_scaling_then_return_data_set_with_multiple_columns_with_values_between_0_and_1(
            self):
        data_set = get_data_set_with_category_column()

        one_hot_encode_processing_method = OneHotEncoderProcessingMethod()
        scale_processing_method = MinMaxScalerProcessingMethod()
        data_set_preprocessor = Container.data_set_preprocessor(processing_methods=[one_hot_encode_processing_method,
                                                                                    scale_processing_method])

        preprocessed_data_set: pandas.DataFrame = data_set_preprocessor.get_preprocessed_data(data_set)

        preprocessed_data_frame_columns = preprocessed_data_set.columns.tolist()

        max_value = preprocessed_data_set.max().max()
        min_value = preprocessed_data_set.min().min()

        self.assertEqual(4, len(preprocessed_data_frame_columns))
        self.assertTrue(max_value <= 1)
        self.assertTrue(min_value >= 0)


def get_data_set_with_category_column():
    data_frame_values = [[1900, "SRB"], [1940, "JPN"], [1940, "DEN"], [2010, "JPN"], [2020, "SRB"],
                         [1996, "JPN"]]
    data_frame_columns = ['Year', 'Country Code']
    data_set = pandas.DataFrame(data_frame_values, columns=data_frame_columns)

    return data_set


def get_only_numerical_data_set():
    data_frame_values = [[1900, 11], [1940, 32], [1940, 2], [2010, 2332], [2020, 2],
                         [1996, 231]]
    data_frame_columns = ['Year', 'Numerical Column']
    data_set = pandas.DataFrame(data_frame_values, columns=data_frame_columns)

    return data_set
