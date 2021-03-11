from typing import List

import pandas


class DataLoader(object):
    def load_data(self, pathname: str) -> pandas.DataFrame:
        pass

    def extract_data(self, loaded_data: pandas.DataFrame, must_contained_columns: List[str])\
            -> (pandas.DataFrame, List[str], List[str]):
        pass
