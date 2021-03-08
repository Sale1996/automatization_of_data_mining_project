from data_set_loader.classes.data_set_loader import DataSetLoader
from data_set_loader.classes.pandas_data_set_loader.loader.data_loader import DataLoader
from data_set_loader.classes.pandas_data_set_loader.loader_validator.loader_validator import LoaderValidator
from data_set_loader.classes.pandas_data_set_loader.processor.data_processor import DataProcessor


class FacadePandasDataSetLoader(DataSetLoader):

    def __init__(self, column_names, pairs_of_column_names, data_loader: DataLoader, validator: LoaderValidator,
                 data_processor: DataProcessor):
        super().__init__(column_names, pairs_of_column_names)
        self.data_loader = data_loader
        self.validator = validator
        self.data_processor = data_processor

    def load_data_set_and_column_names(self, pathname):
        self.validator.validate_pathname(pathname)

        loaded_data = self.data_loader.load_data(pathname)

        self.validator.validate_loaded_data(
            loaded_data, self.must_contained_columns, self.pairs_of_must_contained_columns)

        updated_data, updated_must_contained_columns = self.data_processor.update_data_set_and_must_contained_columns(
            loaded_data, self.must_contained_columns, self.pairs_of_must_contained_columns)

        return self.data_loader.extract_data(updated_data, updated_must_contained_columns)
