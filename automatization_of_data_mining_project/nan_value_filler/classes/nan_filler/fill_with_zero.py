from nan_value_filler.classes.nan_filler.nan_filler import NanFiller


class FillWithZero(NanFiller):
    def __init__(self):
        super().__init__()
        self.name = "fill_with_zero"

    def fill_nan_values(self, data_set_info, filling_column_name):
        data_set_info.data_set[filling_column_name] = data_set_info.data_set[filling_column_name].fillna(0)

        return data_set_info
