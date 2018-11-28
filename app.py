import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import requests
import pickle
import operator
import time
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from datetime import datetime as dt
from dash.dependencies import Input, Output
from stock_class import *
from dateutil.relativedelta import relativedelta

ticker_set = load_set()
stock_data = load_dict()
stock_list = load_sorted_list()
stock_list = sorted(list(set(stock_list)), key=operator.attrgetter('total_occurances'), reverse=True)

custom_ticker1 = str(stock_list[1].ticker)
custom_ticker2 = str(stock_list[2].ticker)
custom_ticker3 = str(stock_list[3].ticker)
custom_ticker4 = str(stock_list[4].ticker)
custom_ticker5 = str(stock_list[5].ticker)
custom_ticker6 = str(stock_list[6].ticker)

print(stock_data[custom_ticker1])
print(stock_data[custom_ticker2])
print(stock_data[custom_ticker3])
print(stock_data[custom_ticker4])
print(stock_data[custom_ticker5])
print(stock_data[custom_ticker6])

one_month = dt.now() - relativedelta(months=1)
three_months = dt.now() - relativedelta(months=3)
one_year = dt.now() - relativedelta(years=1)
five_year = dt.now() - relativedelta(years=5)


# figure={'layout': custom_ticker1})
### APP ###

app = dash.Dash('Hello World')

app.layout = html.Div([


    html.Div([

        ################### Main Div ###################
        
        html.Div([
            html.H4('$'+custom_ticker1), 
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': '1M', 'value': one_month},
                    {'label': '3M', 'value': three_months},
                    {'label': '1Y', 'value': one_year},
                    {'label': '5Y', 'value': five_year},
                    #add different time choices
                ],
                value=custom_ticker1
            ),
            dcc.Graph(id='my-graph')
        ], style={'width': '500'}, className='six columns'), 


        html.Div([
            html.H4('$'+custom_ticker2), 
            dcc.Dropdown(
                id='my-dropdown2',
                options=[
                    {'label': '1M', 'value': one_month},
                    {'label': '3M', 'value': three_months},
                    {'label': '1Y', 'value': one_year},
                    {'label': '5Y', 'value': five_year},
                ],
                value=custom_ticker2
            ),
            dcc.Graph(id='my-2graph')
        ], style={'width': '500'}, className='six columns'), 


        html.Div([
            html.H4('$'+custom_ticker3), 
            dcc.Dropdown(
                id='my-dropdown3',
                options=[
                    {'label': '1M', 'value': one_month},
                    {'label': '3M', 'value': three_months},
                    {'label': '1Y', 'value': one_year},
                    {'label': '5Y', 'value': five_year},
                ],
                value=custom_ticker3
            ),
            dcc.Graph(id='my-3graph')
        ], style={'width': '500'}, className='six columns'), 


        html.Div([
            html.H4('$'+custom_ticker4), 
            dcc.Dropdown(
                id='my-dropdown4',
                options=[
                    {'label': '1M', 'value': one_month},
                    {'label': '3M', 'value': three_months},
                    {'label': '1Y', 'value': one_year},
                    {'label': '5Y', 'value': five_year},
                ],
                value=custom_ticker4
            ),
            dcc.Graph(id='my-4graph')
        ], style={'width': '500'}, className='six columns'), 


        html.Div([
            html.H4('$'+custom_ticker5), 
            dcc.Dropdown(
                id='my-dropdown5',
                options=[
                    {'label': '1M', 'value': one_month},
                    {'label': '3M', 'value': three_months},
                    {'label': '1Y', 'value': one_year},
                    {'label': '5Y', 'value': five_year},
                ],
                value=custom_ticker5
            ),
            dcc.Graph(id='my-5graph')
        ], style={'width': '500'}, className='six columns'), 


        html.Div([
            html.H4('$'+custom_ticker6), 
            dcc.Dropdown(
                id='my-dropdown6',
                options=[
                    {'label': '1M', 'value': one_month},
                    {'label': '3M', 'value': three_months},
                    {'label': '1Y', 'value': one_year},
                    {'label': '5Y', 'value': five_year},
                ],
                value=custom_ticker6
            ),
            dcc.Graph(id='my-6graph')
        ], style={'width': '500'}, className='six columns'), 


        ################### Main Div ###################

    ],className='row')

])
    


@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        custom_ticker1,
        'iex',
        selected_dropdown_value,
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

@app.callback(Output('my-2graph', 'figure'), [Input('my-dropdown2', 'value')])
def update_graph2(selected_dropdown_value):
    df = web.DataReader(
        custom_ticker2,
        'iex',
        selected_dropdown_value,
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

@app.callback(Output('my-3graph', 'figure'), [Input('my-dropdown3', 'value')])
def update_graph3(selected_dropdown_value):
    df = web.DataReader(
        custom_ticker3,
        'iex',
        selected_dropdown_value, 
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }


@app.callback(Output('my-4graph', 'figure'), [Input('my-dropdown4', 'value')])
def update_graph4(selected_dropdown_value):
    df = web.DataReader(
        custom_ticker4,
        'iex',
        selected_dropdown_value, 
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }
    

@app.callback(Output('my-5graph', 'figure'), [Input('my-dropdown5', 'value')])
def update_graph5(selected_dropdown_value):
    df = web.DataReader(
        custom_ticker5,
        'iex',
        selected_dropdown_value, 
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }


@app.callback(Output('my-6graph', 'figure'), [Input('my-dropdown6', 'value')])
def update_graph6(selected_dropdown_value):
    df = web.DataReader(
        custom_ticker6,
        'iex',
        selected_dropdown_value, 
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }



app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


if __name__ == '__main__':
    app.run_server()
