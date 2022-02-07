
import csv

data_file = 'covid-19-results1.csv'
info = ['TotalDeaths', 'NewDeaths', 'ActiveCases', 'NewCases', 'TotalCases', 'TotalRecovered']
search = input("Search Country: ")

with open(data_file) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if search == row['Country']:
            print(row)
