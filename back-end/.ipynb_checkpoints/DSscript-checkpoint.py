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
import functions

# plotly credentials
plotly.tools.set_credentials_file(username=PLOTLY_USER_NAME, api_key=PLOTLY_API_KEY)


def main():
    
    # get data from mongoDB
    lines = functions.read_in()
    
    # create DF for plots and correlations
    df_plot = functions.generate_df(lines)
    
    # create DF from user tweets for sentiment analysis
    tweet_df = functions.tweets_df(lines)
    
    # get most recent date of activity
    most_recent_date = pd.to_datetime(df_plot['date'][0]).date()

    # get sentiment for the today's tweets
    most_recent_tweets = tweet_df.copy()[tweet_df['date'] == most_recent_date]
    most_recent_sentiment = functions.get_sentiment(most_recent_tweets['clean']).mean()

    # create chart captions
    tweet_cap = caption_sentiment(most_recent_sentiment)
    correlation_list = ['caffeine','alcohol','food','sleep','water']
    caption_dict = functions.graph_captions(correlation_list, tweet_cap)
    
    # create mood rolling average
    rolling_mood = df_plot['mood'].rolling(3).mean()

    # handle gaps in input
    rolling_mood.fillna(0)

    # create graphs to be displayed
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

    trace2 = go.Scatter(
        visible = False,
        x = df_plot['date'],
        y = df_plot['caffeine'],
        mode = 'lines',
        name= 'Caffeine',
        text= df_plot['caffeine'],
        fill='tozeroy',
        fillcolor='rgba(0, 153, 0,.2)',
        hoverinfo='text',
        line=dict(
            shape='spline',
        width=0.5),
        opacity = .01,
        marker = dict(color = 'rgba(0, 153, 0,0.8)'))

    trace3 = go.Scatter(
        visible = False,
        x = df_plot['date'],
        y = df_plot['alcohol'],
        mode = 'lines',
        name= 'Alcohol',
        fillcolor='rgba(0, 153, 0,.2)',
        fill='tozeroy',
        hoverinfo = 'text',
        text= df_plot['alcohol'],
        line=dict(
            shape='spline'),
        marker = dict(color = 'rgba(0, 153, 0,0.8)'))

    trace4 = go.Scatter(
        visible = False,
        x = df_plot['date'],
        y = df_plot['food'],
        mode = 'lines',
        name= 'Food',
        fill='tozeroy',
        fillcolor='rgba(0, 153, 0,.2)',
        text= df_plot['food'],
        line=dict(
            shape='spline'),
        marker = dict(color = 'rgba(0, 153, 0,0.8)'))

    trace5 = go.Scatter(
        visible = False,
        x = df_plot['date'],
        y = df_plot['sleep'],
        mode = 'lines',
        name= 'Sleep',
        fill='tozeroy',
        fillcolor='rgba(0, 153, 0,.2)',
        text= df_plot['sleep'],
        line=dict(
            shape='spline'),
        marker = dict(color = 'rgba(0, 153, 0,0.8)'))

    trace6 = go.Scatter(
        visible = False,
        x = df_plot['date'],
        y = df_plot['water'],
        mode = 'lines',
        name= 'Water',
        fill='tozeroy',
        fillcolor='rgba(0, 153, 0,.2)',
        text= df_plot['water'],
        line=dict(
            shape='spline'),
        marker = dict(color = 'rgba(0, 153, 0,0.8)'))

    data = [trace1, trace2, trace3, trace4, trace5, trace6]

    # create interactive menus for graphs
    updatemenus = list([
        dict(active=-1,
            buttons=list([
                dict(label = 'Caffeine',
                    method = 'update',
                    args = [{'visible': [True, True, False, False, False, False]},
                            {'title': caption_dict['caffeine']}]),
                dict(label = 'Alcohol',
                    method = 'update',
                    args = [{'visible': [True, False, True, False, False, False]},
                            {'title': caption_dict['alcohol']}]),
                dict(label = 'Food',
                    method = 'update',
                    args = [{'visible': [True, False, False, True, False, False]},
                            {'title': caption_dict['food']}]),
                dict(label = 'Sleep',
                    method = 'update',
                    args = [{'visible': [True, False, False, False, True, False]},
                            {'title': caption_dict['sleep']}]),
                dict(label = 'Water',
                    method = 'update',
                    args = [{'visible': [True, False, False, False, False, True]},
                            {'title': caption_dict['water']}]),
            ])
        )
    ])

    layout = dict(title = tweet_cap+'<br>Your mood over time',
                xaxis= dict(title='Date', ticklen = 5,
                            zeroline=False),
                autosize=False,
                width=650,
                height=300,
                showlegend=False,
                updatemenus=updatemenus)

    fig = dict(data = data, layout = layout)
    plot_url = py.plot(fig, filename='plot from API (12)', auto_open=False)

#start process
if __name__ == '__main__':
    main()
