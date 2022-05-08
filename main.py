import pandas as pd
dt = pd.DataFrame(pd.read_excel('test1.csv'))
dto = dt.to_csv("test1.csv")
new_data = pd.read_csv("test1.csv")
data = pd.DataFrame(new_data)
x = data.head()
print (x)


