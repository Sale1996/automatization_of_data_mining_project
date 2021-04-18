from dependency_injector import containers, providers

from feature_importance_statistic_generator.classes.facade_feature_importance_statistic_generator import \
    FacadeFeatureImportanceStatisticGenerator
from feature_importance_statistic_generator.classes.input_validator.input_validator_impl import InputValidatorImpl


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(InputValidatorImpl)
    feature_importance_statistic_generator = providers.Factory(FacadeFeatureImportanceStatisticGenerator,
                                                               input_validator=input_validator)
