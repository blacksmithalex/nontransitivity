import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline

data2021 = pd.read_csv('SBER_2021.csv', sep = ';')
data2020 = pd.read_csv('SBER_2020.csv', sep = ';')
data2019 = pd.read_csv('SBER_2019.csv', sep = ',')
data2018 = pd.read_csv('SBER_2018.csv', sep = ',')
data2017 = pd.read_csv('SBER_2017.csv', sep = ',')

dfs = [data2017, data2018, data2019, data2020, data2021]