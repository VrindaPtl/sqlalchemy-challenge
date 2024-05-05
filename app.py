# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################


# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:////Users/vrindapatel/Desktop/Starter_Code/Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`

Mesurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation values"""
    # Convert the query results to a dictionary by using "date" as the key and "prcp" as the value
# Calculate the date 1 year ago from the last data point in the database
    last_date = session.query(Mesurement.date).order_by(Mesurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    year_ago = last_date - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Mesurement.date, Mesurement.prcp).filter(Mesurement.date >= year_ago).all()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    # Return a JSON list of stations from the dataset.
    stations = session.query(Station.station).all()
    stations_list = list(np.ravel(stations))
    return jsonify(stations_list)   

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of all temperature observations"""
    # Query the dates and temperature observations of the most active station for the last year of data.
    last_date = session.query(Mesurement.date).order_by(Mesurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    year_ago = last_date - dt.timedelta(days=365)
    most_active_station = session.query(Mesurement.station, func.count(Mesurement.station)).group_by(Mesurement.station).order_by(func.count(Mesurement.station).desc()).first()
    results = session.query(Mesurement.date, Mesurement.tobs).filter(Mesurement.date >= year_ago).filter(Mesurement.station == most_active_station[0]).all()

    # Convert the query results to a dictionary using date as the key and tobs as the value.
    tobs = []
    for date, tob in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tob
        tobs.append(tobs_dict)

    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    """Return a list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range"""
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    results = session.query(Mesurement.date, func.min(Mesurement.tobs), func.avg(Mesurement.tobs), func.max(Mesurement.tobs)).filter(Mesurement.date >= start).all()

    # Unravel results into a 1D array and convert to a list
    start_temp = list(np.ravel(results))
    return jsonify(start_temp)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return a list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range"""
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    results = session.query(Mesurement.date, func.min(Mesurement.tobs), func.avg(Mesurement.tobs), func.max(Mesurement.tobs)).filter(Mesurement.date >= start).filter(Mesurement.date <= end).all()
    
    # Unravel results into a 1D array and convert to a list
    start_end_temp = list(np.ravel(results))
    return jsonify(start_end_temp)  

