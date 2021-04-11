import pandas as pd
import plotly.express as px
df=pd.read_csv('Project.csv')
print(df)
fig=px.scatter(df,x='date',y='cases',color='country',title='COVID Cases')
fig.show()