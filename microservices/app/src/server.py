#from src import app
# from flask import jsonify




# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from flask import Flask,render_template,Markup,redirect
from plotly.offline import plot
from plotly.graph_objs import Scatter


app=Flask(__name__)


apps = dash.Dash(__name__, server=app, url_base_pathname='/')
df = pd.read_csv('https://filestore.barkeeper89.hasura-app.io/v1/file/12e09cf0-f5f8-4297-aa2d-c44a4d763b15')

apps.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                    go.Scatter(
                                x=df["years"],
                                y=df[i],
                                mode='markers',
                                opacity=0.7,
                                name=i,
                                marker={
                                    'size': 15,
                                    'line': {'width': 0.5, 'color': 'white'}
                                },
                            ) for i in df.CountryCode.unique()
            ],
            'layout':go.Layout(
            	xaxis={'type': 'log', 'title': 'Years'},
                yaxis={'title': 'Death rate, crude (per 1,000 people)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


@app.route('/')
def index():
	return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
