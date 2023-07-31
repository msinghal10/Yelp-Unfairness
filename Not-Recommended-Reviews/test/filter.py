import pandas as pd

df = pd.read_csv('Final.csv')
# df1=pd.read_csv('random100.csv')

# s1 = pd.merge(df, df1, how='inner', on=['UserName','Friends','Reviews','ReviewDate'])

# print(s1)

# s1.to_csv('Final.csv',index=False)


df1 = df.drop_duplicates(subset='UserID', keep="first")

df1.to_csv('final-nodupli.csv',index=False)