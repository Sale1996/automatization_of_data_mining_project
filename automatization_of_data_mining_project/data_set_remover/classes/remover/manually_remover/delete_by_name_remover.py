from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.remover.manually_remover.manually_remover import ManuallyRemover


class DeleteByNameRemover(ManuallyRemover):
    def remove_and_return_updated_list(self, data_set_list: List[DataSetInfo], data_set_name: str):
        updated_data_set_list = []

        for data_set_info in data_set_list:
            if data_set_name != data_set_info.data_set_name:
                updated_data_set_list.append(data_set_info)

        return updated_data_set_list
