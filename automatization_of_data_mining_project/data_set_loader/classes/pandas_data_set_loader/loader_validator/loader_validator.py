from typing import List, Tuple

import pandas


class LoaderValidator(object):
    def validate_pathname(self, pathname: str):
        pass

    def validate_loaded_data(self, loaded_data: pandas.DataFrame,
                             must_contained_columns: List[str],
                             pairs_of_must_contained_columns: List[Tuple[str, str]]):
        pass
