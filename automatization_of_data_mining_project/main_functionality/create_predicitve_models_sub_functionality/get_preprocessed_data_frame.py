import pandas
from pip._vendor.distlib.compat import raw_input
from termcolor import colored

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from data_set_preprocessor import Preprocessor
from data_set_preprocessor.classes.processing_method.one_hot_encoder_processing_method import \
    OneHotEncoderProcessingMethod

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def get_preprocessed_data_frame(data_frame: pandas.DataFrame):
    chosen_column = ""
    while True:
        preprocessed_step_main_menu = ('----------------------------------------------------------\n'
                                       '|            Data set preprocessor                       |\n'
                                       '|--------------------------------------------------------|\n'
                                       ' Choose column which will be used as prediction value:    \n'
                                       '                                                          \n')

        available_columns = list(set(data_frame.columns.tolist()) - set(['Year', 'Country Code']))
        map_menu_index_to_column_name = {}
        starting_index = 1

        for column_name in available_columns:
            column_input = " " + str(starting_index) + ") " + column_name + "\n"
            preprocessed_step_main_menu += column_input
            map_menu_index_to_column_name[str(starting_index)] = column_name
            starting_index += 1

        user_choice = raw_input(preprocessed_step_main_menu)

        if user_choice not in map_menu_index_to_column_name:
            print(ERROR_STRING, "Wrong user input!")
            continue
        else:
            chosen_column = map_menu_index_to_column_name[user_choice]
            break

    predictor_column_type = ""
    while True:
        preprocessed_step_prediction_column_type_menu = ('----------------------------------------------------------\n'
                                                         '|            Data set preprocessor                       |\n'
                                                         '|--------------------------------------------------------|\n'
                                                         ' Which type is chosen prediction column:                  \n'
                                                         '                                                          \n'
                                                         ' 1) Numerical value                                       \n'
                                                         ' 2) Categorical value                                     \n'
                                                         '                                                          \n'
                                                         ' Choose:')

        user_type_choice = raw_input(preprocessed_step_prediction_column_type_menu)

        if user_type_choice == "1":
            predictor_column_type = "numerical_value"
            break
        elif user_type_choice == "2":
            predictor_column_type = "categorical_value"
            break
        else:
            print(ERROR_STRING, "Input value must be 1 or 2!")
            continue

    one_hot_encode_processing_method = OneHotEncoderProcessingMethod()
    data_set_preprocessor = Preprocessor(processing_methods=[one_hot_encode_processing_method])

    encoded_data_set = data_set_preprocessor.get_preprocessed_data(data_frame)

    x_data_columns = list(set(encoded_data_set.columns.tolist()) - set([chosen_column]))
    x_data = encoded_data_set[x_data_columns]
    y_data = encoded_data_set[[chosen_column]]
    preprocessed_data_set: PreprocessedDataSetInfo = data_set_preprocessor.get_train_test_split_of_data_set(
        x_data, y_data, 0.2)

    return preprocessed_data_set, predictor_column_type
