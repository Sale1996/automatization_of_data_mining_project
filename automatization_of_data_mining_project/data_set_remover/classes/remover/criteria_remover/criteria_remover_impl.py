from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.classes.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.remover.criteria_remover.criteria_remover import CriteriaRemover


class CriteriaRemoverImpl(CriteriaRemover):
    def remove_and_return_updated_list(self, criteria_remover_data: DataForCriteriaRemove):
        return_data_sets_info = []

        for data_set_info in criteria_remover_data.data_sets_info:
            columns_to_check = self.get_which_columns_to_check(criteria_remover_data, data_set_info)

            criteria_passed, \
            updated_data_set_info = self.get_is_criteria_passed_and_updated_data_set_object(columns_to_check,
                                                                                            criteria_remover_data,
                                                                                            self.criteria_column_validators,
                                                                                            data_set_info)
            if criteria_passed:
                return_data_sets_info.append(updated_data_set_info)

        return return_data_sets_info

    def get_is_criteria_passed_and_updated_data_set_object(self, columns_to_check, criteria_remover_data,
                                                           criteria_validators, data_set_info):
        criteria_passed = True
        for column_name in columns_to_check:
            is_column_passed_by_criteria = self.column_check_by_criteria(column_name, criteria_remover_data,
                                                                         criteria_validators, data_set_info.data_set)
            if not is_column_passed_by_criteria:
                # if column_name is not only one left in "optional" columns, then
                # remove it from data set and pass that data set to the next iteration
                non_must_contained_columns = data_set_info.other_column_names[:]
                if column_name in data_set_info.other_column_names:
                    non_must_contained_columns.remove(column_name)
                    if non_must_contained_columns:
                        data_set_info = self.remove_column_from_data_set(column_name, data_set_info,
                                                                         non_must_contained_columns)
                        continue
                criteria_passed = False

        return criteria_passed, data_set_info

    def remove_column_from_data_set(self, column_name, data_set_info, non_must_contained_columns):
        new_columns = data_set_info.data_set.columns.tolist()[:]
        new_columns.remove(column_name)
        new_data_set_info = DataSetInfo(data_set_info.data_set_name,
                                        data_set_info.data_set[new_columns],
                                        data_set_info.must_contained_columns,
                                        non_must_contained_columns)
        return new_data_set_info

    def column_check_by_criteria(self, column_name, criteria_remover_data, criteria_validators, data_set):
        is_column_passed_by_criteria = True
        for criteria_column_validator in criteria_validators:
            if criteria_column_validator.criteria_name == criteria_remover_data.criteria_name:
                if not criteria_column_validator.is_valid(data_set, column_name, criteria_remover_data.criteria_value):
                    is_column_passed_by_criteria = False
        return is_column_passed_by_criteria

    def get_which_columns_to_check(self, criteria_remover_data, data_set_info):
        if criteria_remover_data.columns_to_include:
            columns_to_check = criteria_remover_data.columns_to_include
        else:
            columns_to_check = self.get_colums_exluded_columns_to_exclude(data_set_info.data_set.columns.tolist(),
                                                                          criteria_remover_data.columns_to_exclude)
        return columns_to_check

    def get_colums_exluded_columns_to_exclude(self, all_columns, columns_to_exclude):
        return list(set(all_columns) - set(columns_to_exclude))
