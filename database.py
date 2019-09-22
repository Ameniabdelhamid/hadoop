import hive_utils

query = """
CREATE TABLE IF NOT EXISTS products.catalog( pid string, name string,price float, category string, brand string, image string) 
COMMENT 'Products details'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
"""

query1 = """
LOAD DATA LOCAL INPATH '/home/ameni/PycharmProjects/Product_Service/productdb.csv'
INTO TABLE products.catalog;
"""

query2 = """
SELECT * FROM products.catalog LIMIT 5;
"""

hive_client = hive_utils.HiveClient(
    server='0.0.0.0',
    port=10000,
    db='products'
)
a = hive_client.execute(query)
b = hive_client.execute(query1)
c = hive_client.execute(query2)
c = list(c)

import pyhs2
with pyhs2.connect(host='localhost',
           port=10000,
           authMechanism="PLAIN",
           user='your_user',
           password='your_password',
           database='your_default_db') as conn:
        with conn.cursor() as cur:
            print(cur.getDatabases())
            cur.execute("select * from table")
            #Return info from query
            print(cur.getSchema())

