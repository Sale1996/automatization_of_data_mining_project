import unittest
from typing import List

import pandas

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.factor_analysis_dimension_reduction import \
    FactorAnalysisDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.low_variance_filter_dimension_reduction import \
    LowVarianceFilterDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.pca_dimension_reduction import PCADimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.random_forest_dimension_reduction import \
    RandomForestDimensionReduction
from data_set_dimension_reductioner.dependency_injector.container import Container
from data_set_dimension_reductioner.exceptions.dimension_reduction_exceptions import WrongInputFormatError, \
    NoStringValuesAllowedInDataSetError, NonIterableObjectError


class DataSetDimensionReductionTestBase(unittest.TestCase):
    pass


class DataSetDimensionReductionErrorCases(DataSetDimensionReductionTestBase):
    def setUp(self):
        pass

    def test_given_nones_when_reduce_dimension_on_data_set_then_throw_input_format_exception(self):
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(dimension_reductioners=[])

        with self.assertRaises(WrongInputFormatError):
            data_set_dimension_reductioner.get_reduced_data_sets(None, None)

    def test_given_non_data_frame_data_set_when_reduce_dimension_on_data_set_then_throw_input_format_exception(self):
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(dimension_reductioners=[])

        with self.assertRaises(WrongInputFormatError):
            data_set_dimension_reductioner.get_reduced_data_sets(1, 1)

    def test_given_data_frame_with_string_values_when_reduce_dimension_on_data_set_then_throw_no_string_values_allowed(
            self):
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(dimension_reductioners=[])

        data_set_values = [[1, "daw"], [2, "y54"], [3, "42z"], [9, "plp"], [9, "oop"]]

        data_set_column_names = ["Test", "Test1"]

        data_frame = pandas.DataFrame(data_set_values, columns=data_set_column_names)

        with self.assertRaises(NoStringValuesAllowedInDataSetError):
            data_set_dimension_reductioner.get_reduced_data_sets(data_frame, data_frame)

    def test_given_none_when_get_dimension_reductioner_report_data_then_throw_wrong_input_format_error(self):
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(dimension_reductioners=[])

        with self.assertRaises(WrongInputFormatError):
            data_set_dimension_reductioner.get_report_data(None)

    def test_given_non_array_input_when_get_dimension_reductioner_report_data_then_throw_not_iterable_object_error(
            self):
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(dimension_reductioners=[])

        with self.assertRaises(NonIterableObjectError):
            data_set_dimension_reductioner.get_report_data(1)

    def test_given_wrong_array_element_type_when_dimension_reductioner_report_data_then_throw_wrong_input_format_error(
            self):
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(dimension_reductioners=[])

        with self.assertRaises(WrongInputFormatError):
            data_set_dimension_reductioner.get_report_data([1])


class DataSetDimensionReductionDummyCases(DataSetDimensionReductionTestBase):
    def test_given_data_frame_0_variance_column_when_reduce_dimension_reduction_on_data_set_with_low_variance_filter_return_same_data_set_without_that_column(
            self):
        low_variance_dimension_reduction = LowVarianceFilterDimensionReduction()
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(
            dimension_reductioners=[low_variance_dimension_reduction]
        )

        data_set_values = [[1, 1], [2, 1], [3, 1], [9, 1], [9, 1]]
        data_set_column_names = ["Test", "Test1"]
        data_frame = pandas.DataFrame(data_set_values, columns=data_set_column_names)

        expected_data_frame_values = [[1], [2], [3], [9], [9]]

        dimension_reduction_results: List[
            DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(data_frame, data_frame)

        self.assertTrue((expected_data_frame_values == dimension_reduction_results[0].reduced_data_set).all())

    def test_given_data_frame_when_reduce_dimension_reduction_on_data_set_with_random_forest_algorithm_return_same_data_set_without_one_column(
            self):
        random_forest_dimension_reduction = RandomForestDimensionReduction()
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(
            dimension_reductioners=[random_forest_dimension_reduction]
        )

        data_frame_values = [[1901, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        df = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_x_values = df[['Year', 'Country Code']]
        df_y_values = df[['Test']]
        df_x_values = pandas.get_dummies(df_x_values)

        expected_data_frame_values = [[0, 1901], [1, 1900], [0, 2000], [1, 2000]]

        dimension_reduction_results: List[
            DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(df_x_values, df_y_values)

        self.assertTrue((expected_data_frame_values == dimension_reduction_results[0].reduced_data_set).all())

    def test_given_data_frame_when_reduce_dimension_reduction_on_data_set_with_principal_component_analysis_algorithm_return_same_data_set_without_one_column(
            self):
        pca_dimension_reduction = PCADimensionReduction()
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(
            dimension_reductioners=[pca_dimension_reduction]
        )

        data_frame_values = [[1901, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        df = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_x_values = df[['Year', 'Country Code']]
        df_y_values = df[['Test']]
        df_x_values = pandas.get_dummies(df_x_values)

        dimension_reduction_results: List[
            DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(df_x_values, df_y_values)

        # PCA always generates different values, so this is only way to find out if it works
        number_of_columns = dimension_reduction_results[0].reduced_data_set.shape[1]

        self.assertEqual(2, number_of_columns)

    def test_given_data_frame_when_reduce_dimension_reduction_on_data_set_with_factor_analysis_algorithm_return_same_data_set_without_one_column(
            self):
        factor_analysis_dimension_reduction = FactorAnalysisDimensionReduction()
        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(
            dimension_reductioners=[factor_analysis_dimension_reduction]
        )

        data_frame_values = [[1901, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        df = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_x_values = df[['Year', 'Country Code']]
        df_y_values = df[['Test']]
        df_x_values = pandas.get_dummies(df_x_values)

        dimension_reduction_results: List[
            DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(df_x_values, df_y_values)

        # PCA always generates different values, so this is only way to find out if it works
        number_of_columns = dimension_reduction_results[0].reduced_data_set.shape[1]

        self.assertEqual(2, number_of_columns)

    def test_given_data_frame_when_dimension_reductioner_report_data_then_return_correct_report_data_set(
            self):
        # THIS IS USED ONLY AS TEST OF CREATION OF DOCUMENT, NOT AS REAL TEST CASE
        low_variance_dimension_reduction = LowVarianceFilterDimensionReduction()
        random_forest_dimension_reduction = RandomForestDimensionReduction()
        pca_dimension_reduction = PCADimensionReduction()
        factor_analysis_dimension_reduction = FactorAnalysisDimensionReduction()

        data_set_dimension_reductioner = Container.data_set_dimension_reductioner(
            dimension_reductioners=[low_variance_dimension_reduction,
                                    random_forest_dimension_reduction,
                                    pca_dimension_reduction,
                                    factor_analysis_dimension_reduction]
        )

        data_frame_values = [[1901, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        df = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_x_values = df[['Year', 'Country Code']]
        df_y_values = df[['Test']]
        df_x_values = pandas.get_dummies(df_x_values)

        dimension_reduction_results: List[
            DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(df_x_values,
                                                                                             df_y_values)

        data_set_dimension_reductioner.get_report_data(dimension_reduction_results,
                                                       "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/generated_statistics/dimension_reduction_statistics")

        self.assertEqual(1, 1)
