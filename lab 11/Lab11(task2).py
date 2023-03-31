
import pandas as pd
data = pd.read_csv("pandaslab11.csv",)
#df = pd.DataFrame("pandaslab11.csv", index=labels)


for x in data.index:
         if data.loc[x, "Passed"] == "no":
            data.drop(x, inplace = True)
print(data)

#print(data[data["Passed"] == "yes"])