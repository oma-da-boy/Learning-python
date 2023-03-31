
import pandas as pd
data = pd.read_csv("pandaslab11.csv")

decen = data.sort_values(by=["Result"], ascending=False)
print(decen)
