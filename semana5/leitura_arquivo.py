import matplotlib as plot
import numpy as np
import pandas as pd

file_vgsales = "/home/ronaldo/_DESENVOLVIMENTO/Python/USP_python_2/semana5/vgsales/vgsales.csv"

vg_games = pd.read_csv(file_vgsales)

print(vg_games.head())
#print(vg_games.tail())
#print(vg_games.describe())

print(vg_games.plot())
