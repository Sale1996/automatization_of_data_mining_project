from typing import List, Tuple

import pandas


class DataProcessor(object):

    def update_data_set_and_must_contained_columns(self, loaded_data: pandas.DataFrame,
                                                   must_contained_columns: List[str],
                                                   pairs_of_must_contained_columns: List[Tuple[str, str]])\
            -> (pandas.DataFrame, List[str]):

        pass
