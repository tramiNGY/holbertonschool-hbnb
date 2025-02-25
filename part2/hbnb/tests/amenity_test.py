#!/usr/bin/python3
from app.models.amenity import Amenity

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi", description="it can wifi your life")
    assert amenity.name == "Wi-Fi"
    assert amenity.description == "it can wifi your life"
    print("Amenity creation test passed!")

test_amenity_creation()