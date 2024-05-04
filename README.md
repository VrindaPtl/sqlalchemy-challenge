# sqlalchemy-challenge
This project leverages Python and SQLAlchemy for conducting elementary data exploration and analysis on an SQLite climate database. The analysis is performed using SQLAlchemy (via ORM queries), Pandas, and Matplotlib. Additionally, the project offers an API, which is designed using Flask, to facilitate queries on this climate data.

# Part 1: Analyse and Explore the Climate Data
This segment of the project undertakes the analysis of Hawaii precipitation and weather station data, subsequently generating visualizations that depict patterns in rainfall and temperature. It further aids in planning trips to Hawaii by providing:

Summaries of local precipitation for each weather station, and
Daily temperature data for a flexible range of trip dates.

It consists of:
- a SQLite database (Resources/Hawaii.sqlite)
- a Jupyter notebook (sqlalchemy-challenge/climate_analysis.ipnyb) that uses SQLAlchemy, Python Pandas and MatPlotlib to analyze and visualize this data.
- Bar charts, a histogram and an area chart that are visible within the notebook and also stored as .png files in the sqlalchemy-challenge folder.

**Analysis:**
1. Precipitation analysis: The graph is a precipitation analysis from August 23, 2016, to August 17, 2017. It shows the amount of rainfall (in inches) recorded on each day during this period. The precipitation levels vary significantly throughout the year, with some days experiencing much higher rainfall than others. Notable spikes in precipitation occur around September 5, 2016, and May 14, 2017. The data provides valuable insights into the rainfall patterns in this location, which can be useful for planning activities based on historical weather patterns. Overall, the graph illustrates the variability and unpredictability of precipitation over time.

2. Temperature observation: The histogram illustrates that 24 degrees is the most commonly recorded temperature, providing valuable insights into the temperature patterns. There are smaller frequencies noted at temperatures of approximately 18 and 26 degrees.

## Part 2: Climate App
This part of the project surfaces several SQLAlchemy precipitation and temperature queries in an API using a Python Flask app:
- / 
    - Home page
- /api/v1.0/precipitation
    - Daily precipitation totals for last year
- /api/v1.0/stations
    - Active weather stations
- /api/v1.0/tobs
    - Daily temperature observations for the WAIHEE weather station
- /api/v1.0/trip/yyyy-mm-dd
    - Min, average & max temperatures for the range beginning with the provided start date through 08/23/17
- /api/v1.0/trip/yyyy-mm-dd/yyyy-mm-dd
    - Min, average & max temperatures for the range beginning with the provided start - end date range

It consists of:
- a SQLite database (Resources/Hawaii.sqlite)
- a Flask app (sqlalchemy-challenge/app.py).



