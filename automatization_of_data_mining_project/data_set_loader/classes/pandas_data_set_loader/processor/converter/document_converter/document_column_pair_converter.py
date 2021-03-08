import pandas

from data_set_loader.classes.pandas_data_set_loader.loader.data_loader import DataLoader
from data_set_loader.classes.pandas_data_set_loader.processor.converter.column_pair_converter import ColumnPairConverter

'''

UKLONI COUNTRY CODE I COUNTRY NAME IZ NAZIVA VARIABLI, NAPRAVI GA VISE GENERALIZOVANIM!

'''

class DocumentColumnPairConverter(ColumnPairConverter):

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def convert_values_of_changeable_column_to_match_important_column(self, loaded_data, pair_important_column, pair_changeable_column):
        countries_data_set = self.load_countries_data_set(pair_important_column, pair_changeable_column)

        country_name_to_country_code_map = self.get_country_name_to_country_code_map(countries_data_set)

        updated_data_frame = self.change_country_name_to_country_code_in_data_set(country_name_to_country_code_map,
                                                                                  loaded_data)
        return updated_data_frame

    def change_country_name_to_country_code_in_data_set(self, country_name_to_country_code_map, loaded_data):
        country_name_index = loaded_data.columns.get_loc("Country Name")
        new_columns = self.change_country_name_column_name_to_country_code(country_name_index, loaded_data)

        updated_data_set = self.change_country_name_fields_to_country_code(country_name_index,
                                                                           country_name_to_country_code_map,
                                                                           loaded_data)

        updated_data_frame = pandas.DataFrame(updated_data_set, columns=new_columns)
        return updated_data_frame

    def change_country_name_fields_to_country_code(self, country_name_index, country_name_to_country_code_map,
                                                   loaded_data):
        # Add it only if there is Country code for country name!
        updated_data_set = []
        for row in loaded_data.values:
            if row[country_name_index] in country_name_to_country_code_map:
                new_row = row
                new_row[country_name_index] = country_name_to_country_code_map[row[country_name_index]]
                updated_data_set.append(new_row)
        return updated_data_set

    def change_country_name_column_name_to_country_code(self, country_name_index, loaded_data):
        new_columns = loaded_data.columns.tolist()[:]
        new_columns[country_name_index] = "Country Code"
        return new_columns

    def get_country_name_to_country_code_map(self, iso3_data_values):
        country_name_to_country_code_map = {}
        for country_value in iso3_data_values:
            country_name_to_country_code_map[country_value[1]] = country_value[0]
        return country_name_to_country_code_map

    def load_countries_data_set(self, pair_important_column, pair_changeable_column):
        document_name = pair_important_column + '_' + pair_changeable_column
        document_name = document_name.replace(' ', '_')
        loaded_iso3_data = self.loader.load_data(
            'C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/data_set_loader/classes/pandas_data_set_loader/processor/converter/document_converter/data/' + document_name + '.xlsx')
        iso3_data_values = loaded_iso3_data[['Country Code', 'Country Name']].values
        return iso3_data_values