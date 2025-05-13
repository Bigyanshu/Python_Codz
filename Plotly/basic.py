import plotly.express as px

# Sample Data
data = px.data.iris()

# Create a scatter plot
fig = px.scatter(
    data, 
    x="sepal_width", 
    y="sepal_length", 
    color="species", 
    title="Sepal Dimensions of Iris Species"
)

# Show the plot
fig.show()