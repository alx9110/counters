from datetime import datetime
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()


class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    geo = db.Column(db.String(64))
    adress = db.Column(db.String(250), nullable=False)

    def __init__(self, description, geo, adress):
        self.description = description
        self.geo = geo
        self.adress = adress

class Counters(db.Model):
    __tablename__ = 'counters'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(64))
    unit_of_measurement = db.Column(db.String(32), nullable=False)
    place_id = db.Column(db.Integer)

    def __init__(self, description, name, unit_of_measurement, place_id):
        self.description = name
        self.name = name
        self.unit_of_measurement = unit_of_measurement
        self.place_id = place_id
