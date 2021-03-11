from data_set_loader.classes.pandas_data_set_loader.loader.pandas_reader.pandas_reader import PandasReader
import pandas as pd


class CsvExcelPandasReader(PandasReader):

    def read(self, pathname: str) -> pd.DataFrame:
        if pathname.endswith(".xlsx"):
            loaded_data = pd.read_excel(pathname)
        else:
            loaded_data = pd.read_csv(pathname, encoding='ISO-8859-1', error_bad_lines=False)
        return loaded_data
