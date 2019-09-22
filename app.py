#from productservice import app
from flask import Flask
from pyhive import hive
import pandas as pd
import sys

# Init app
app = Flask(__name__)

host_name = "0.0.0.0"
port = 10000
user = "userhd"
password = "userhd"
database = "default"

conn = hive.Connection(host=host_name, port=port, auth='NONE')
c = conn.cursor()
print('connected')
df = pd.read_sql("SELECT * FROM tuto limit 50", conn)
print(sys.getsizeof(df))
print(df.head())




#if __name__ == '__main__':
    # Run Server
    #app.run(host='0.0.0.0', debug=True)

