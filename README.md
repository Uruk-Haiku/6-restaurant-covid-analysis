# 6-restaurant-covid-analysis

PREFACE: This code is heavily commented and somewhat sloppy. Please do not make fun of me.

This project was created to analyze the relationship between restaurants in Toronto and COVID-19 cases across forward sortation areas (FSAs, the first three digits of your postal code) across various metrics like number of restaurants, health infractions, etc.

The project processes the data in data_prep.py before displaying it across a variety of graphs in main.py. This data preparation process takes a large amount of time due to having to change latitude and longitude into Forward Sortation Area (the first 3 digits of postal code), which is a annoying process and involves querying a web API for five hours due to limits on how many requests they are willing to process per second.

The end result of my analysis found little correlation between restaurant location, density, or health record with COVID-19 cases, which I suppose is a relief.
