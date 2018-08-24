import pandas as pd
#df = pd.DataFrame({'YES':[50,21],'No':[131,2]},index = ['2','3'])
#sheet name is also required in below -> ,sheet_name in .xls
df = pd.read_csv("./Titanic/all/train.csv",index_col=0);
#if we want to write the data in csv
#df.head().to_csv();

#it returns the size of data
#print (df.shape)

#it returns the first five result of the csv
print (df.head())

# for sql files
# import sqlite3
# conn = sqlite3.connect(the connection path);
# fires = pd.read_sql_query(query in sql,conn);
# print(fires.head);

#for selecting certain data only like if-else
#ndf = df.loc[df.Survived==1]

# lambda data : anything which you want to do with data
# df.[coloum wanted].map(lamda function)
# It will replace everything with the above function outcome
# Another way to do the above thing
# Make a function x
# df.apply(x,axis=''name of coloumn)

#df.groupby(name of the key)

