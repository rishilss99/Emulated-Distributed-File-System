from sqlalchemy import text
from itertools import groupby
from operator import itemgetter

"""An important consideration when working with the file system functions of this EDFS
    is that they require absolute path much like the Hadoop DFS"""


class MapReduce:

    def map(self, engine, dataset, partition, inputs):

        result = {}
        if(dataset == 'stocks.csv'):
            stock_name = inputs[0]
            agg_method = inputs[1]
            attrib = inputs[2]
            with engine.connect() as connection:
                with connection.begin():
                    query_result = connection.execute(text(f"select substr(date,1,4), {agg_method}({attrib}) from `{dataset}` partition ({partition}) where Name = '{stock_name}' group by substr(date,1,4);"))
                    for row in query_result:
                        result[row[0]] = float(row[1])
            return result 
                        
    
    def reduce(self, results, agg_method):
        
        pass
