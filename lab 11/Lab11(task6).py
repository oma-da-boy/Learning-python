import pandas as pd
data = pd.read_csv("pandaslab11.csv")

print(data[data["Attempts"] > 2])