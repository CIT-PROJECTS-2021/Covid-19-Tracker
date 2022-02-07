import csv
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objs as go
from matplotlib import pyplot as plt

cols = ['Country', 'TotalDeaths', 'NewDeaths', 'ActiveCases', 'NewCases', 'TotalCases', 'TotalRecovered',
        'TotalTests', 'Population']
df = pd.read_csv("covid-19-results1.csv", usecols=[1, 2, 3, 4, 5, 6, 8, 12, 14], sep=',')
def searchBy_country():
    country = input("Search Country: ")

    print(df.loc[df.Country == country])

    # plotting the Data
    # x = df.TotalCases  # the problem lies here. with some columns it can work. others it will not work
    x_TCases = pd.to_numeric(df['TotalCases'], errors='coerce')
    # y = df.NewCases
    y_NCases = pd.to_numeric(df['NewCases'], errors='coerce')
    # for active Cases
    ac = df.ActiveCases
    ac_y = pd.to_numeric(df['ActiveCases'], errors='coerce')
    # for new deaths
    new_dts = df.NewDeaths
    new_dts_y = pd.to_numeric(df['NewDeaths'], errors='coerce')
    # for total deaths
    tt_dth = df.TotalDeaths
    tt_dth_y = pd.to_numeric(df['TotalDeaths'], errors='coerce')
    # recovery
    tt_rcv = pd.to_numeric(df['TotalRecovered'], errors='coerce')
    # population
    population = pd.to_numeric(df['Population'],  errors='coerce')

    """
    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True

    plt.scatter(ac_y, x_TCases)
    plt.show()
"""

    labels = ['TotalDeaths', 'NewDeaths', 'ActiveCases']
    """
    x = [population]
    xy = np.arange(len(x))
    width = 0.25
    fig, ax = plt.subplots()
    
    rect1 = ax.bar(xy - width/2, tt_dth_y, width, label="New Cases")
    rect2 = ax.bar(xy, ac_y, width, label="Active cases")
    rect3 = ax.bar(xy + width/2, new_dts_y, width, label="New Deaths")

    
    ax.set_ylabel("Total Cases")
    ax.set_title("Cases by Country")

    ax.legend()
    ax.bar_label(rect1, padding=2)
    ax.bar_label(rect2, padding=2)
    fig.tight_layout()
    plt.show()
    """
    plt.style.use("fivethirtyeight")
    plt.scatter(tt_dth_y, new_dts_y)
    # plt.bar(str('Country'), tt_dth_y)
    plt.legend()
    plt.title("Death graph by total cases")
    plt.xlabel("Total Cases")
    plt.ylabel("Total & New")
    plt.tight_layout()
    plt.show()

    # before the end, add new cases, total cases, active cases
    plt.scatter(y_NCases, x_TCases)
    plt.legend()
    plt.title("Cases by population")
    plt.xlabel("POPULATION")
    plt.ylabel("Total cases")
    plt.tight_layout()
    plt.show()

    plt.scatter(tt_rcv, x_TCases)
    plt.legend()
    plt.title("Total cases for the recovered")
    plt.xlabel("Total Cases")
    plt.ylabel("Total recovered")
    plt.tight_layout()
    plt.show()

searchBy_country()

