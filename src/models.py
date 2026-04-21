from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier   
from sklearn.pipeline import Pipeline



def build_logistic_model(preprocessor):
    return Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000))
    ])

def build_decision_tree(preprocessor):
    return Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', DecisionTreeClassifier(max_depth=8, random_state=42))
    ])


def build_xgboost_model(preprocessor):
    return Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', XGBClassifier(
            n_estimators=200, 
            learning_rate=0.1, 
            max_depth=5,
            subsample=0.8,
            colsample_bytree=0.8,
            scale_pos_weight=2.5, 
            random_state=42,
            eval_metric='logloss'
        ))
    ])
