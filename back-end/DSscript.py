#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:15:38 2019
@author: peytonrunyan
"""

# imports
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import utils

# plotly credentials
plotly.tools.set_credentials_file(username=PLOTLY_USER_NAME, api_key=PLOTLY_API_KEY)

def prepare_data(lines, df_plot, correlation_list):
    """
    Returns string with HTML formatting, pandas series, dictionary
    
    See utils.py for specifics 
    """
    
    # get data
    tweet_df = utils.tweets_df(lines)
    
    # graph captions
    most_recent_date = pd.to_datetime(df_plot['date'][0]).date()
    most_recent_tweets = tweet_df.copy()[tweet_df['date'] == most_recent_date]
    most_recent_sentiment = utils.get_sentiment(most_recent_tweets['clean']).mean()
    tweet_cap = caption_sentiment(most_recent_sentiment)
    caption_dict = utils.graph_captions(correlation_list, tweet_cap)
    
    # provides smoothing for mood line and fills gaps
    rolling_mood = df_plot['mood'].rolling(3).mean()
    rolling_mood.fillna(0)
    
    return tweet_cap, caption_dict, rolling_mood


def generate_plot(column, visibility=False, col_name=False, marker_color='rgba(0, 153, 0,0.8)'):
    """
    Returns a plotly graph
    """
    if col_name:
        name = col_name
    else:
        name = column.capitalize()
    
    trace = go.Scatter(
        visible = visibility,
        x = df_plot['date'],
        y = df_plot[column],
        mode = 'lines',
        name = name,
        fillcolor = marker_color,
        fill ='tozeroy',
        hoverinfo ='text',
        text = df_plot[column],
        line = dict(
            shape='spline',
        marker = dict(color = marker_color)) 
    
    return trace
        
        
def create_buttons(correlation_list):
    """
    Returns a list of buttons and their default visibility state for plotly graphs
    """
    buttons_list = []
    for i in range(len(correlation_list)):
        visibility_index = i+1
        visible = ([True]+len(correlation_list)*[False])
        visible[visibility_index] = True

        buttons.append(dict(label = correlation_list[i].capitalize(),
                   method = 'update',
                   args = [{'visible': visible},
                                {'title': caption_dict[correlation_list[i]]}]))
        
        
def main():
    
    # get data
    lines = utils.read_in()
    df_plot = utils.generate_df(lines)
    correlation_list = df_plot.columns.to_list().remove('mood')
    tweet_cap, caption_dict, rolling_mood = prepare_data(lines, df_plot, correlation_list)
   
    # create mood plot
    trace1 = go.Scatter(
        x = df_plot['date'],
        y = rolling_mood,
        mode = 'lines',
        name = 'Mood Score',
        hoverinfo = 'text',
        text= df_plot['mood'].round(2),
        line=dict(
            shape='spline',
        width = 4),
        marker = dict(color='rgba(255,64,153,1)'))

    plots = [trace1]
    
    # generate plots for all other recorded items
    for column in correlation_list:
        plots.append(generate_plot(column))

    # create buttons and set visibility for each plot
    buttons_list = create_buttons(correlation_list)
        
    updatemenus = list([{active: -1, buttons: buttons_list}])

    layout = dict(title = tweet_cap+'<br>Your mood over time',
                xaxis= dict(title='Date', ticklen = 5,
                            zeroline=False),
                autosize=False,
                width=650,
                height=300,
                showlegend=False,
                updatemenus=updatemenus)

    fig = dict(data = plots, layout = layout)
    plot_url = py.plot(fig, filename = 'plot from API (12)', auto_open=False)

#start process
if __name__ == '__main__':
    main()
