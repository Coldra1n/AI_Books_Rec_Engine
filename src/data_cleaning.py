import logging
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Union

class DataStrategy(ABC):
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass
    

class DataPreProcessStrategy():
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        
        try:
            data = data.drop(
                [
                    'order_approved_at',
                    'order_delivered_carrier_date',
                    'order_delivered_customer_date',
                    'order_estimated_delivery_date',
                    'order_purchase_timestamp',
                ], axis=1)
            data["product_weight_g"].fillna(data["product_weight_g"].mean(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].mean(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].mean(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].mean(), inplace=True)
            data["review_comment_message"].fillna("No review", inplace=True)
            
            data = data.select_dtypes(include=[np.number])
            cols_to_drop = ['customer_zip_code_prefix', 'order_item_id']
            data.drop(cols_to_drop, axis=1) # inplace=True
            return data
        except Exception as e:
            logging.error(e)
            raise e

class DataDivideStrategy(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        try:
            X = data.drop('review_score', axis=1)
            y = data['review_score']
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
            return X_train,X_test,y_train,y_test
        except Exception as e:
            logging.error(e)
            raise e


class DataCleaning:
    """ 
    Class for cleaning data which precesses the data and divides it into train and test data
    """
    def __init__(self,data: pd.DataFrame, strategy: DataStrategy):
        self.data = data
        self.strategy = strategy
        
    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error(e)
            raise e
    
#if __name__=='__main__':
#    data = pd.read_csv('data/olist_order_reviews_dataset.csv')
#    data_cleaning = DataCleaning(data, DataPreProsessStrategy())
#    data_cleaning.handle_data()