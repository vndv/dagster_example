import requests
import pandas as pd
from sqlalchemy import create_engine
from dagster import asset 


@asset 
def get_bts_data():
    btc_url = 'https://api.coincap.io/v2/rates/bitcoin'
    btc_json = requests.get(btc_url)
    btc_data = btc_json.json()['data']

    return btc_data

@asset
def load_data(get_bts_data):
    engine = create_engine("postgresql+psycopg2://admin:admin@dagster-postgres/postgres")
    con = engine
    df = pd.DataFrame(get_bts_data,index=[0])
    
    df.head(n=0).to_sql(
        name="btc_data", con=engine, if_exists="replace"
    )
    df.to_sql(name="btc_data", con=engine, if_exists="append")