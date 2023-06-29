import sketch
import pandas as pd

data_pd = pd.read_csv("maestro.csv", sep=';')

print(data_pd.sketch.ask("mostrar los primeros 20 registros de dni 243400999, solo el saldo", call_display=False))
