import logging
import pandas as pd
from zenml import step

@step
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # Drop rows with missing values
        cleaned_df = df.dropna()
        

        # Ensure that the cleaned DataFrame is not empty
        if cleaned_df.empty:
            raise ValueError("The resulting DataFrame is empty after cleaning.")

        return cleaned_df

    except Exception as e:
        # Log any exception that occurs
        logging.error(f"Error in clean_df step: {e}")
        # Optionally, re-raise the exception to halt the pipeline
        raise e
