from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

product = pd.read_csv('data/products.csv')
store = pd.read_csv('data/stores.csv')

store["store_id"] = store["store_id"].astype("object")
product["product_id"] = product["product_id"].astype("object")

store.drop_duplicates(inplace=True)
product.drop_duplicates(inplace=True)


def get_stats(X):
    X = eval(str(X))
    max_14 = np.max(X)
    min_14 = min(X)
    max_7 = max(X[7:])
    min_7 = min(X[7:])
    mean_14 = np.mean(X[:])
    mean_7 = np.mean(X[7:])
    mean_3 = np.mean(X[11:])
    std_14 = np.std(X)
    std_7 = np.std(X[7:])
    std_3 = np.std(X[11:])
    return pd.Series([max_14, min_14, max_7, min_7, mean_14, mean_7, mean_3, std_14, std_7, std_3],
                     index=['max_14', 'min_14', 'max_7', 'min_7', 'mean_14', 'mean_7', 'mean_3', 'std_14', 'std_7',
                            'std_3'])


class Stats_translate(BaseEstimator, TransformerMixin):
    def __init__(self, base=np.exp(1)):
        BaseEstimator.__init__(self)
        TransformerMixin.__init__(self)
        self.base = base

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        Series_list = [get_stats(x) for x in X.sales]
        return pd.DataFrame(Series_list)


def transform_store_data(store_id):
    store_data = store[store["store_id"] == str(store_id)][['region', 'type']]
    return store_data


class Store_translate(BaseEstimator, TransformerMixin):

    def __init__(self, base=np.exp(1)):
        BaseEstimator.__init__(self)
        TransformerMixin.__init__(self)
        self.base = base

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        store_id = X.store_id
        df_list = [transform_store_data(i) for i in store_id]
        return pd.concat(df_list)


def transform_product_data(product_id):
    product_data = product[product["product_id"] == int(
        product_id)][["meat_type", "product_type", "who_eat", "manufacturer"]]
    return product_data


class Product_translate(BaseEstimator, TransformerMixin):
    def __init__(self, base=np.exp(1)):
        BaseEstimator.__init__(self)
        TransformerMixin.__init__(self)
        self.base = base

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        product_id = X.product_id
        df_list = [transform_product_data(i) for i in product_id]
        return pd.concat(df_list)


a = {"date": [3], "product_id": [122788], "store_id": [5699], "sales": [[4, 453, 45, 345, 34, 534, 53, 45, 345,
                                                                         34, 53, 34, 15, 35]]}
