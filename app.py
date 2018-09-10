from flask import Flask, render_template, request
import pandas as pd
from bokeh.embed import components

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from pandas_datareader import data as pdr
import fix_yahoo_finance

app = Flask(__name__)

# Load the Iris Data Set
""" iris_df = pd.read_csv("data/iris.data", 
    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist() """

def create_figure(stock_ticker):

    data = pdr.get_data_yahoo(stock_ticker, start='2017-09-10', end='2018-09-10')

    p=figure(plot_width=400, plot_height=400)

    tools= "hover,crosshair, pan, reset, box_zoom, tap"
    
    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices", tools=tools)
    
    p1.grid.grid_line_alpha=0.3
    
    p1.xaxis.axis_label = 'Date'

    p1.yaxis.axis_label = 'Price'

    p1.line(data.index,data['High'], color='#A6CEE3', legend=stock_ticker)

    return p1

@app.route('/')

def index():
    print("hello")
    plot = create_figure('AAPL')

	# Embed plot into HTML via Flask Render
    script, div = components(plot)

    return render_template("userinfo_lulu.html", script=script, div=div)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == "__main__":
    app.run(port=33507)#debug=True)