#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\arpit\Downloads\Zomato-data-.csv")
print(df.head())
#data cleaning and preparation
def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)
df['rate']=df['rate'].apply(handleRate)
print(df.head())
print(df.info())
print(df.isnull().sum())
#Exploring Restaurant Types
sns.countplot(data=df,x=df['listed_in(type)'],hue=df['listed_in(type)'])
plt.xlabel("Type of Restaurant")
plt.show()
#Votes by Restaurant Type
grouped_data=df.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='green',marker='o')
plt.xlabel("Types of Restaurant")
plt.ylabel('Votes')
plt.show()
#Identify the Most Voted Restaurant
max_votes=df['votes'].max()
restaurant_with_max_votes=df.loc[df['votes']==max_votes,'name']
print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)
#Online Order Availability
sns.countplot(x=df['online_order'],hue=df['online_order'])
plt.show()
#Analyze Ratings
plt.hist(df['rate'],bins=5)
plt.title('Ratings Distribution')
plt.show()
#Approximate Cost for Couples
couple_data=df['approx_cost(for two people)']
sns.countplot(x=couple_data,palette='Set1',hue=couple_data,legend=False)
plt.xlabel('Approximate Cost for Couples')
plt.ylabel('Count')
plt.show()
#Ratings Comparison - Online vs Offline Orders
plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y='rate',data=df,hue='online_order')
plt.show()
#Order Mode Preferences by Restaurant Type
pivot_table=df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap='YlGnBu',fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()