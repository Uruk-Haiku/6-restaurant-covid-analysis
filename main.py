"""
This is the main file for the project, which will display all my graphs and results
from my data collection. A large part of this project was pre-processing the data into a useful
form in cleaned_data.csv, so please go check out data_prep.py for more information on that. As
is clarified in data_prep.py, UNLESS YOU HAVE A SPARE FIVE (5) HOURS, DO NOT RUN data_prep.py.

This program pulls cleaned data from the csv file that was previously created (this has been
provided for you), graphs and analyzes it.
"""
import plotly.express as px
from FSA import FSA
import csv


def read_cleaned_data() -> {str: FSA}:
    """
    This method reads from the cleaned_data.csv file prepared by data_prep.py, and then returns
    the data in a dict mapping the names of FSAs (Forward Sortation Areas, the first 3 digits of
    your postal code) to the data for each FSA.
    """
    data = {}  # Creating dict to store data

    # Open cleaned_data.csv
    with open('cleaned_data.csv', newline='') as cleaned_data_csv:
        datareader = csv.reader(cleaned_data_csv, delimiter=',')
        for row in datareader:  # Passing through all rows
            if row[0] != 'FSA':  # Making sure we aren't taking in the first row, which describes
                # the data format.

                # Assigning data
                data[row[0]] = FSA(row[0])  # Creating a new FSA instance with the name
                data[row[0]].number_of_restaurants = int(row[1])
                data[row[0]].number_of_minor_infractions = int(row[2])
                data[row[0]].number_of_significant_infractions = int(row[3])
                data[row[0]].number_of_crucial_infractions = int(row[4])
                data[row[0]].total_covid_cases_per_100 = float(row[5])
                data[row[0]].total_covid_hospitalizations_per_1000 = float(row[6])
                data[row[0]].total_covid_deaths_per_1000 = float(row[7])
                data[row[0]].population = int(row[8])
                data[row[0]].percent_1_dose = float(row[9])
                data[row[0]].percent_2_doses = float(row[10])

    return data


# ==================================================================================================
#                              Actually running the code
# ==================================================================================================
data = read_cleaned_data()

# Number of Restaurants as compares to COVID-19 Cases per 100 People
x1 = []
y1 = []
for FSA in data:
    if data[FSA].total_covid_cases_per_100 != -1.0:  # Checking to see if cases are unsuppressed
        x1.append(data[FSA].number_of_restaurants)
        y1.append(data[FSA].total_covid_cases_per_100)

# Creates plotly graph complete with axis labels, descriptive title, and an r-squared
# trendline that can be hovered to see the r-squared value.
fig1 = px.scatter(x=x1, y=y1, labels={'x': 'Number of Restaurants per FSA',
                                      'y': 'COVID-19 Cases per 100 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Number of Restaurants vs. COVID-19 Cases per 100 people for each FSA')
fig1.show()

# Total number of health infractions as compares to COVID-19 Cases per 100 People
x2 = []
y2 = []
for FSA in data:
    if data[FSA].total_covid_cases_per_100 != -1.0:  # Checking to see if cases are unsuppressed
        x2.append(data[FSA].number_of_minor_infractions
                  + data[FSA].number_of_significant_infractions
                  + data[FSA].number_of_crucial_infractions)
        y2.append(data[FSA].total_covid_cases_per_100)

fig2 = px.scatter(x=x2, y=y2, labels={'x': 'Total Number of Health Infractions per FSA',
                                      'y': 'COVID-19 Cases per 100 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Total Number of Health Infractions vs. ' +
                        'COVID-19 Cases per 100 people for each FSA')
fig2.show()

# Number of Restaurants as Compares to Hospitalizations
x3 = []
y3 = []
for FSA in data:
    # Checking to see if hospitalizations are unsuppressed
    if data[FSA].total_covid_hospitalizations_per_1000 != -1.0:
        x3.append(data[FSA].number_of_restaurants)
        y3.append(data[FSA].total_covid_hospitalizations_per_1000)

fig3 = px.scatter(x=x3, y=y3, labels={'x': 'Number of Restaurants per FSA',
                                      'y': 'COVID-19 Hospitalizations per 1000 People'},
                  opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Number of Restaurants vs. ' +
                        'COVID-19 Hospitalizations per 1000 people for each FSA')
fig3.show()

# Number of Restaurants as Compares to Deaths
x4 = []
y4 = []
for FSA in data:
    if data[FSA].total_covid_deaths_per_1000 != -1.0:  # Checking to see if deaths are unsuppressed
        x4.append(data[FSA].number_of_restaurants)
        y4.append(data[FSA].total_covid_deaths_per_1000)

fig4 = px.scatter(x=x4, y=y4, labels={'x': 'Number of Restaurants per FSA',
                                      'y': 'COVID-19 Deaths per 1000 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Number of Restaurants vs. ' +
                        'COVID-19 Deaths per 1000 people for each FSA')
fig4.show()

# Number of Crucial Health Infractions as Compares to Cases
x5 = []
y5 = []
for FSA in data:
    if data[FSA].total_covid_cases_per_100 != -1.0:  # Checking to see if cases are unsuppressed
        x5.append(data[FSA].number_of_crucial_infractions)
        y5.append(data[FSA].total_covid_cases_per_100)

fig5 = px.scatter(x=x5, y=y5, labels={'x': 'Number of Crucial Health Infractions per FSA',
                                      'y': 'COVID-19 Cases per 100 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Number of Crucial Health Infractions vs. ' +
                        'COVID-19 Cases per 100 People for each FSA')
fig5.show()

# Number of Crucial Health Infractions as Compares to Hospitalizations
x6 = []
y6 = []
for FSA in data:
    # Checking to see if hospitalizations are unsuppressed
    if data[FSA].total_covid_hospitalizations_per_1000 != -1.0:
        x6.append(data[FSA].number_of_crucial_infractions)
        y6.append(data[FSA].total_covid_hospitalizations_per_1000)

fig6 = px.scatter(x=x6, y=y6, labels={'x': 'Number of Crucial Health Infractions per FSA',
                                      'y': 'COVID-19 Hospitalizations per 1000 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Number of Crucial Health Infractions vs. ' +
                        'COVID-19 Hospitalizations per 1000 People for each FSA')
fig6.show()

# Percent Fully Vaccinated as Compares to Hospitalizations
x7 = []
y7 = []
for FSA in data:
    # Checking to see if hospitalizations are unsuppressed
    if data[FSA].total_covid_hospitalizations_per_1000 != -1.0:
        x7.append(data[FSA].percent_2_doses)
        y7.append(data[FSA].total_covid_hospitalizations_per_1000)

fig7 = px.scatter(x=x7, y=y7, labels={'x': 'Percentage of Population with 2 Doses of ' +
                                           'COVID-19 Vaccine',
                                      'y': 'COVID-19 Hospitalizations per 1000 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Percentage of Population with 2 Doses of COVID-19 Vaccine vs. ' +
                        'COVID-19 Hospitalizations per 1000 People for each FSA')
fig7.show()

# Density of restaurants by population as compares to COVID-19 cases
x8 = []
y8 = []
for FSA in data:
    if data[FSA].total_covid_cases_per_100 != -1.0:  # Checking to see if  are unsuppressed
        x8.append(data[FSA].number_of_restaurants / data[FSA].population)
        y8.append(data[FSA].total_covid_cases_per_100)

fig8 = px.scatter(x=x8, y=y8, labels={'x': 'Density of Restaurants by Population per FSA',
                                      'y': 'COVID-19 Cases per 100 People'}, opacity=0.60,
                  trendline='ols', trendline_color_override='darkblue',
                  title='Density of Restaurants by Population vs. ' +
                        'COVID-19 Cases per 100 People for each FSA')
fig8.show()

# Blank format for adding more graphs.
"""
x = []
y = []
for FSA in data:
    if data[FSA]. != -1.0:  # Checking to see if  are unsuppressed
        x.append(data[FSA].)
        y.append(data[FSA].)

fig = px.scatter(x=x, y=y, labels={'x': '',
                                   'y': ''}, opacity=0.60,
                 trendline='ols', trendline_color_override='darkblue',
                 title=' vs. ' +
                       '')
fig.show()
"""
