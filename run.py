from pyhive import hive
from TCLIService.ttypes import TOperationState

host_name = "0.0.0.0"
port = 10000
user = "userhd"
password = "userhd"

# Connect to server

cursor = hive.connect(host=host_name, port=port, auth='NONE').cursor()
print('connected')

# Create database products

cursor.execute('CREATE DATABASE products', async=True)
print('created')

# Create table catalog

cursor.execute('CREATE TABLE IF NOT EXISTS products.catalog \
               ( pid String, name String, price float, category String, brand String, image String) \
               COMMENT "Products details" \
               ROW FORMAT DELIMITED  \
               FIELDS TERMINATED BY " " \
               LINES TERMINATED BY "\n" \
               STORED AS TEXTFILE')

print('table created')

# Load data to table

cursor.execute('LOAD DATA LOCAL INPATH "/home/ameni/PycharmProjects/Product_Service/productdb.csv" \
                INTO TABLE products.catalog')
print('data loaded')

cursor.execute('SELECT * FROM products.catalog LIMIT 5')
print('data displayed')


status = cursor.poll().operationState
while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
    logs = cursor.fetch_logs()
    for message in logs:
        print(message)

    # If needed, an asynchronous query can be cancelled at any time with:
    # cursor.cancel()

    status = cursor.poll().operationState

print(cursor.fetchall())
