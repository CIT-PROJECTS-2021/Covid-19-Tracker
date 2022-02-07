import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv("covid-19-results1.csv", usecols=[1, 2, 3, 4, 5, 6, 8, 12, 14], sep=',')
cols = ['Country', 'TotalDeaths', 'NewDeaths', 'ActiveCases', 'NewCases', 'TotalCases', 'TotalRecovered']
country_results = []
title_results = []
print(df.columns)

def searchBy_country():
    country = input("Search Country: ")
    print(df.loc[df.Country == country])

    df.head()
    df[df.columns].hist(figsize=(12, 6))
    plt.show()

searchBy_country()

