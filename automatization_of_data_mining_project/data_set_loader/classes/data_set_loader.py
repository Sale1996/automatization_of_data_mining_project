from typing import List, Tuple

import pandas


class DataSetLoader(object):
    
    def __init__(self, column_names: List[str], pairs_of_must_contained_columns: List[Tuple[str, str]]):
        self.must_contained_columns = column_names
        # Each pair contains of two lists and one of them needs to be in loaded data set
        self.pairs_of_must_contained_columns = pairs_of_must_contained_columns
    
    def load_data_set_and_column_names(self, pathname: str) -> (pandas.DataFrame, List[str], List[str]):
        pass
