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

def create_figure(stock_info):
    stock_ticker = stock_info['stock_name']

    kind = stock_info['price_kind']

    data = pdr.get_data_yahoo(stock_ticker, start='2017-09-10', end='2018-09-10')

    p=figure(plot_width=800, plot_height=400)

    tools= "hover,crosshair, pan, reset, box_zoom, tap"
    
    p1 = figure(x_axis_type="datetime", title=kind, tools=tools)
    
    p1.grid.grid_line_alpha=0.3
    
    p1.xaxis.axis_label = 'Date'

    p1.yaxis.axis_label = 'Price'

    p1.line(data.index, data[kind], color='#A6CEE3', legend=stock_ticker)

    return p1

app_lulu={}
@app.route('/', methods=['GET','POST'])

def index():
    return render_template('userinfo_lulu.html')
    # get ticker from user here ..
    """ if request.method == 'GET':
        return render_template('userinfo_lulu.html') """
    """     else:
        app_lulu.vars['stock_name'] = request.form['stock_name']
        plot = create_figure(app_lulu['stock_name'])
        script, div = components(plot)
        return render_template("stockinfo_lulu.html", script=script, div=div) """

app_lulu={}
@app.route('/next_lulu', methods=['GET','POST'])
def next_lulu():  #remember the function name does not need to match the URL
    app_lulu['stock_name'] = request.form['stock_name']
    app_lulu['price_kind'] = request.form['gender']
    plot = create_figure(app_lulu)
    script, div = components(plot)
    return render_template("stockinfo_lulu.html", script=script, div=div)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == "__main__":
    #app.run(port=#debug=True)33507)
    app.run(debug=True)