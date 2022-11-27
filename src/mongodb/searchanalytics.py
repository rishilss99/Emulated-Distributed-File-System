from importlib.metadata import metadata
from pymongo import MongoClient
from sqlalchemy import create_engine, text
import pandas as pd

"""An important consideration when working with the file system functions of this EDFS
    is that they require absolute path much like the Hadoop DFS"""


class SearchAnalytics:
    def __init__(self):
        # MongoDB database's connection string
        conn_str = "mongodb+srv://dsci551:dsci551@cluster0.eks9nfe.mongodb.net/test"
        client = MongoClient(conn_str)

        # Database
        db = client['EDFS_Directory']

        # Collection
        self.collection = db['DSCI551']

        # Azure MySQL database's connection string
        mysql_config = {
            'user': "shreeram@dsci551",
            'password': "dsci#551",
            'host': "dsci551.mysql.database.azure.com",
            'port': 3306
        }

        self.mysql_engine = create_engine(
            f"mysql+pymysql://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/dsci551")


    def dropdown(self, path):

        path_list = path.split("/")
        result = []
        if(path_list[-1] == 'stocks.csv'):
            with self.mysql_engine.connect() as connection:
                with connection.begin():
                    stock_names = connection.execute(text(f"select distinct Name from `{path_list[-1]}`;"))
                    stock_list = []
                    for stock in stock_names:
                        stock_list.append(''.join(map(str,stock)))
                    agg_method = ["avg", "min", "max"]
                    attributes = connection.execute(text(f"select column_name from information_schema.columns where table_name = '{path_list[-1]}';"))
                    attrib_list = []
                    for attrib in attributes:
                        attrib_list.append(''.join(map(str,attrib)))
                    attrib_list[0] = "all"
                    print(stock_list)
                    print(attrib_list)
                    result.extend([stock_list, agg_method ,attrib_list])
                    return result