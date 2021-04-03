from dependency_injector import containers, providers

from prediction_module.classes.facade_predictor import FacadePredictor
from prediction_module.classes.input_validator.input_validator_impl import InputValidatorImpl
from prediction_module.classes.predictors.classificators.decision_tree_classifier import DecisionTreeClassification
from prediction_module.classes.predictors.classificators.knn_classificator import KNNClassificator
from prediction_module.classes.predictors.classificators.logicstic_regressor import LogisticRegressor
from prediction_module.classes.predictors.classificators.random_forest_classification import RandomForestClassification
from prediction_module.classes.predictors.classificators.support_vector_machine import SupportVectorMachine
from prediction_module.classes.predictors.regressors.decision_tree_regression import DecisionTreeRegression
from prediction_module.classes.predictors.regressors.multiple_linear_regression import MultipleLinearRegression
from prediction_module.classes.predictors.regressors.polynomial_regression import PolynomialRegression
from prediction_module.classes.predictors.regressors.random_forest_regression import RandomForestRegression
from prediction_module.classes.predictors.regressors.support_vector_regression import SupportVectorRegression


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(InputValidatorImpl)
    # predictors
    decision_tree_regression = providers.Factory(DecisionTreeRegression)
    multiple_linear_regression = providers.Factory(MultipleLinearRegression)
    polynomial_regression = providers.Factory(PolynomialRegression)
    random_forest_regression = providers.Factory(RandomForestRegression)
    support_vector_regression = providers.Factory(SupportVectorRegression)

    decision_tree_classification = providers.Factory(DecisionTreeClassification)
    knn_classification = providers.Factory(KNNClassificator)
    logistic_regression = providers.Factory(LogisticRegressor)
    random_forest_classification = providers.Factory(RandomForestClassification)
    support_vector_machine = providers.Factory(SupportVectorMachine)

    # predictor
    facade_predictions_module = providers.Factory(FacadePredictor,
                                                  input_validator=input_validator(),
                                                  predictors=[
                                                      decision_tree_regression(),
                                                      multiple_linear_regression(),
                                                      polynomial_regression(),
                                                      random_forest_regression(),
                                                      support_vector_regression(),
                                                      decision_tree_classification(),
                                                      knn_classification(),
                                                      logistic_regression(),
                                                      random_forest_classification(),
                                                      support_vector_machine()
                                                  ])
