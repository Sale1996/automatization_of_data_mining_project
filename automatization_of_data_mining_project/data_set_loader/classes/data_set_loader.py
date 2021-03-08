class DataSetLoader(object):
    
    def __init__(self, column_names, pairs_of_column_names):
        self.must_contained_columns = column_names
        # Each pair contains of two lists and one of them needs to be in loaded data set
        self.pairs_of_must_contained_columns = pairs_of_column_names
    
    def load_data_set_and_column_names(self, pathname):
        pass
