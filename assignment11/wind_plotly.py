import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

# Extract numeric part and convert to float
df['strength'] = df['strength'].str.extract(r'^(\d+)').astype(float)

fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data, Strength vs. Frequency")
fig.write_html("wind.html", auto_open=True)