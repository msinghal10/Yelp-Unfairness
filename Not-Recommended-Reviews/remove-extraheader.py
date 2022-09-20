import pandas as pd
import numpy as np

df = pd.read_csv('Total-reviews.csv',engine='python')

df1=df[df.ne(df.columns).any(1)]

df1.to_csv('Total-noextraheader.csv',index=False)


df2=pd.read_csv('Total-noextraheader.csv',engine='python')


df3=df2[~df2.Review.str.contains("This review has been removed for violating our Terms of Service",na=False)]

df3.to_csv('Total-noexheadnore.csv',index=False)

df2=pd.read_csv('Total-noexheadnore.csv',engine='python')

df1 = df2[df2.isna().any(axis=1)]

print(df1)

df1 = df2.dropna()

print(df1)

df1.to_csv('Final-Dataset.csv',index=False)