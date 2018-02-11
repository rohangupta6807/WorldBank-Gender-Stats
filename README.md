# WorldBank-Gender-Stats

## Getting started

What is it?

This app makes a graph of  ""*Death rate,crude (per 1000 people)""*  VS  ""*year*"" of different countries using DASH plotly web framework.

It imports the data present in .csv file and make the graph using this data .
It helps to see the data in graphical manner and helps for prediction .

WorldBank-Gender-Stats data present in Gender_StatsData.csv file
http://databank.worldbank.org/data/download/Gender_Stats_csv.zip  

### Prerequisites

- [Hasura CLI](https://docs.hasura.io/0.15/manual/install-hasura-cli.html)
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) (required only for local development)

## Installation
1. First install python version 3.6.3 or higher in your local machine.
2. Run "pip install Flask" in your cmd or terminal.
3. Run "pip install requests" in your cmd or terminal.
4. Run "python first.py" in your cmd or terminal
5. pip install dash==0.20.0 
6. pip install dash-renderer==0.11.3
7. pip install dash-html-components==0.8.0  
8. pip install dash-core-components==0.18.1 
9. pip install plotly --upgrade

## Deploy this project
$ hasura quickstart hasura/base-python-dash
$ cd base-python-dash
$ git add . && git commit -m "Initial Commit"
$ git push hasura master
Now, your app will be running at https://dash.YOUR-CLUSTER-NAME.hasura-app.io (replace YOUR-CLUSTER-NAME with the name of your cluster). To get the name of your cluster
$ hasura cluster status
Navigate to another page https://dash.YOUR-CLUSTER-NAME.hasura-app.io/app1 to see a graph.

## Support
If you happen to get stuck anywhere, please mail me at gupta.rohan1711@gmail.com. Alternatively, if you find a bug, you can raise an issue here.


