import unittest
from typing import List

from predictions_error_calculator.classes.data_class.error_score import ErrorScore
from predictions_error_calculator.classes.error_calculator.mse_error_calculator import MeanSquareErrorCalculator
from predictions_error_calculator.classes.error_calculator.r2_error_calculator import R2ErrorCalculator
from predictions_error_calculator.depedency_injector.container import Container
from predictions_error_calculator.exceptions.predictions_error_calculator_exceptions import WrongInputFormatError, \
    NonIterableObjectError


class PredictionsErrorCalculatorTestBase(unittest.TestCase):
    pass


class PredictionsErrorCalculatorTestErrorCases(PredictionsErrorCalculatorTestBase):
    def setUp(self) -> None:
        self.predictions_error_calculator = Container.predictions_error_calculator(error_calculators=[])

    def test_given_None_when_calculate_error_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.predictions_error_calculator.calculate_errors(None, None)

    def test_given_non_array_element_create_missing_rows_when_calculate_error_then_throw_non_iterable_exception(self):
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            self.predictions_error_calculator.calculate_errors(non_iterable_object, non_iterable_object)


class PredictionsErrorCalculatorTestDummyCases(PredictionsErrorCalculatorTestBase):
    def test_given_same_data_when_calculate_errors_then_return_one_object_with_mse_as_name_and_zero_as_result(self):
        first_pair = [1, 2, 3, 4, 5]
        second_pair = [1, 2, 3, 4, 5]
        mse_error_calculator = MeanSquareErrorCalculator()
        predictions_error_calculator = Container.predictions_error_calculator(error_calculators=[mse_error_calculator])
        calculated_errors: List[ErrorScore] = predictions_error_calculator.calculate_errors(first_pair, second_pair)

        self.assertEqual("MSE", calculated_errors[0].error_calculator_name)
        self.assertEqual(0.0, calculated_errors[0].error_calculator_result)

    def test_given_different_data_when_calculate_errors_then_return_one_object_with_mse_as_name_and_correct_score_as_result(
            self):
        """
          Test score is calculated via: https://www.statology.org/mse-calculator/
        """
        first_pair = [34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24]
        second_pair = [37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23]
        mse_error_calculator = MeanSquareErrorCalculator()
        predictions_error_calculator = Container.predictions_error_calculator(error_calculators=[mse_error_calculator])
        calculated_errors: List[ErrorScore] = predictions_error_calculator.calculate_errors(first_pair, second_pair)

        self.assertEqual("MSE", calculated_errors[0].error_calculator_name)
        self.assertEqual(5.917, calculated_errors[0].error_calculator_result)

    def test_given_same_data_when_calculate_errors_then_return_object_with_r2_error_and_one_as_its_score(self):
        first_pair = [1, 2, 3, 4, 5]
        second_pair = [1, 2, 3, 4, 5]
        r2_error_calculator = R2ErrorCalculator()
        predictions_error_calculator = Container.predictions_error_calculator(error_calculators=[r2_error_calculator])
        calculated_errors: List[ErrorScore] = predictions_error_calculator.calculate_errors(first_pair, second_pair)

        self.assertEqual("R2", calculated_errors[0].error_calculator_name)
        self.assertEqual(1.0, calculated_errors[0].error_calculator_result)

    def test_given_different_data_when_calculate_errors_then_return_one_object_with_r2_as_name_and_correct_score_as_result(
            self):
        """
          Test score is calculated via: https://agrimetsoft.com/calculators/R-squared%20correlation
        """
        first_pair = [34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24]
        second_pair = [37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23]
        r2_error_calculator = R2ErrorCalculator()
        predictions_error_calculator = Container.predictions_error_calculator(error_calculators=[r2_error_calculator])
        calculated_errors: List[ErrorScore] = predictions_error_calculator.calculate_errors(first_pair, second_pair)

        self.assertEqual("R2", calculated_errors[0].error_calculator_name)
        self.assertEqual(0.923, calculated_errors[0].error_calculator_result)
