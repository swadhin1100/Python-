import pandas as pd
df= pd.read_csv("imdb_top_1000.csv")
print(df.head(10))
df.tail()
df.info()
df.rename()
df.column()