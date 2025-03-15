#!/usr/bin/python3
from app import db

# Table d'association entre Place et Amenity
place_amenity_association = db.Table(
    'place_amenity', db.Model.metadata,
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)
