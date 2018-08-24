import glob
import os
import pandas as pd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.csv')

vkDataFrame = pd.concat([pd.read_csv(f, index_col=0, encoding='utf-8') for f in glob.glob(path)], ignore_index = True).dropna(how='any')

