# Moody

A mood tracking web application that logs a user's activities (sleep, diet, social media use, etc.) and presents the user with how those affect their mood over time.

## Data Science 

The data science portion of this app is a python backend script. It reads in JSON data from MongoDB, converts it to a pandas dataframe, and then examines correlations between the input data and mood. It also scrapes Twitter for the user's activity, cleans the text data, and then performs sentiment analysis on it so that correlations between sentiment and mood can be seen. All data is visualized in interactive charts using plotly, and custom text providing a layman's explanation of the relationship is generated with each plot to ensure that the user does not have to interpet the graph on their own.
[See DSscripts.py and utils.py](https://github.com/peytonrunyan/Moody/tree/master/back-end)

## Demo Video

https://vimeo.com/330355490

## Team
|   [**Aaron Harbaugh**](https://github.com/aaharbaugh)  |   [**Jordan Massingill**](https://github.com/jordan-massingill)   |    [**Julie Jonak**](https://github.com/juliejonak)    |   [**Justin Kaseman**](https://github.com/Jkasem)  |   [**Peyton Runyan**](https://github.com/peytonrunyan)  |
|:----------------:|:----------------:|:---------------:|:---------------:|:---------------:|
| [<img src="https://avatars0.githubusercontent.com/u/29643223?s=460&v=4" width="80">](https://github.com/aaharbaugh) | [<img src="https://avatars0.githubusercontent.com/u/37593557?s=460&v=4" width="80">](https://github.com/jordan-massingill)  | [<img src="https://avatars0.githubusercontent.com/u/41002881?s=460&v=4" width="80">](https://github.com/juliejonak) | [<img src="https://avatars1.githubusercontent.com/u/28818476?s=460&v=4" width="80">](https://github.com/Jkasem) | [<img src="https://avatars1.githubusercontent.com/u/44583861?s=460&v=4" width="80">](https://github.com/peytonrunyan) 
| [<img src="https://github.com/favicon.ico" width="15"> Github](https://github.com/aaharbaugh)  |  [<img src="https://github.com/favicon.ico" width="15"> Github](https://github.com/jordan-massingill) | [<img src="https://github.com/favicon.ico" width="15"> Github](https://github.com/juliejonak)  | [<img src="https://github.com/favicon.ico" width="15"> Github](https://github.com/Jkasem) | [<img src="https://github.com/favicon.ico" width="15"> Github](https://github.com/peytonrunyan)  
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> LinkedIn](https://www.linkedin.com/in/aaron-harbaugh-0b56825/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> LinkedIn](https://www.linkedin.com/in/jordan-massingill-53b469bb/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> LinkedIn](https://www.linkedin.com/in/juliejonak/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> LinkedIn](https://www.linkedin.com/in/christopher-beards-1292b529/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> LinkedIn](https://www.linkedin.com/in/justin-kaseman/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> LinkedIn](https://www.linkedin.com/in/peyton-runyan/) |


## Tech Stack

### Frontend

- React
- Router
- FontAwesome
- Bootstrap
- MdbReact

### Backend

- Node.js
- Express
- MongoDB

### Machine Learning

- Python
- Numpy
- Pandas
- Tweepy
- Plotly
- TextBlob
