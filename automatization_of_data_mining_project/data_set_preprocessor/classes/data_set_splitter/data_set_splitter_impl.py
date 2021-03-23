"""
    Test data percentage is calculated based on number of rows of input data

    Validation data percentage is calculated based on already split train data

"""
from sklearn.model_selection import train_test_split

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from data_set_preprocessor.classes.data_set_splitter.data_set_splitter import DataSetSplitter


class DataSetSplitterImpl(DataSetSplitter):
    def split_data_set_into_train_validation_test(self, x_data, y_data, test_data_percentage,
                                                  validation_data_percentage):
        x_train_validation, x_test, y_train_validation, y_test = train_test_split(x_data, y_data,
                                                                                  test_size=test_data_percentage,
                                                                                  random_state=123)

        x_train, x_validation, y_train, y_validation = train_test_split(x_train_validation, y_train_validation,
                                                                        test_size=validation_data_percentage,
                                                                        random_state=123)

        preprocessed_data = PreprocessedDataSetInfo(x_train, x_validation, x_test, y_train, y_validation, y_test)

        return preprocessed_data
