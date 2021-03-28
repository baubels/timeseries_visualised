import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('triangle-cleaned-data.csv')

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x = df["Time"],
        y = df["Price"],
        mode="lines",
        name="Stock Prices",
        showlegend=True,
    )
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df['Price'].rolling(50).mean(),
        mode="lines",
        name="Rolling Mean",
        line=go.scatter.Line(color="red"),
        showlegend=True)
)

# print(px.get_trendline_results(fig))

fig2 = px.line(df, x="Time", y=df['Price'].rolling(50).std())

app.layout = html.Div(children=[
    html.H1(children='Algothon 2021 - Team Triangle Data Visualisation',
    style={
        'textAlign': 'center'
    }),

    html.Div(children='''
        Cleaned Data:
    '''),

    dcc.Graph(
        id='graph-1',
        figure=fig
    ),

    html.Div(children='''
        Mean: STD: Min: Max:
    ''',
    style={
        'textAlign': 'center'
    }),

    dcc.Graph(
        id='graph-2',
        figure=fig2
    ),



])

if __name__ == '__main__':
    app.run_server(debug=True)
