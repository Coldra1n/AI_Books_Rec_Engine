from zenml import pipeline
from pipelines.training_pipeline import train_pipeline

if __name__ =="__main__":
    train_pipeline(data_path="C:/Users/Nick/Desktop/DLOPS/data/Amazon_books_cleaned.csv")
