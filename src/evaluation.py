from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def evaluate_model(y_true, y_pred, y_proba):
    print("Classification Report:")
    print(classification_report(y_true, y_pred))
    
    print("ROC AUC Score:", roc_auc_score(y_true, y_proba))
    
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
