import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from pydataset import data

def get_db_url(host, username, password, database):
    url = f'mysql+pymysql://{useranme}:{password}@{host}/{database}'
    return url

from env import host, username, password
url = get_db_url(host, username, password, 'employees')

get_db_url(host, username, password, 'employees')

pd.read_sql('SELECT * FROM employees LIMIT OFFSER 50', url)