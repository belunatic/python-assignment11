import plotly.express as px
import plotly.data as pldata


df = pldata.iris(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
print(df.head())
print(df.info())
fig = px.scatter(df, x='sepal_width', y='petal_width', color='species',
                 title="Iris Data, Sepal vs. Petal Length", hover_data=["species", "species_id"])
fig.write_html("iris.html", auto_open=True)

# Do not try fig.show()!  This sometimes works, but usually it just hangs.