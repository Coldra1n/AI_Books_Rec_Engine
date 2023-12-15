from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

@pipeline()
def train_pipeline(ingest_data, clean_data, model_train, evaluation):
    df = ingest_data()
    x_train, x_test, y_train, y_test = clean_df(df)
    model = model_train(x_train, x_test, y_train, y_test)
    mse, rmse = evaluation(model, x_test, y_test)