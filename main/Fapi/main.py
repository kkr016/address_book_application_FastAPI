# Import the required library

from fastapi import FastAPI 
from pydantic import BaseModel
from geopy.geocoders import Nominatim
import requests

#creating instance
app = FastAPI()

db = []

#creating object for the addressBook
class addressBook(BaseModel):
    name: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    emails: str
    phonenumbers: str

#root node/page
@app.get('/')
def index():
    return {"Welcome": "to Address Book"}   #returning Welcome note

#function using app() to Get all the users
@app.get('/addresses')
def get_User():
    return db

#function using app() to Get particular user using Id
@app.get('/addresses/{address_id}')
def get_User_1(address_id: int):
    return db[address_id-1]

#function using app() to Get particular user location
@app.get('/addresses/{address_Location}')
def get_User_Locations(address_Location: str):
    
    # Initialize Nominatim API
    #geolocator = Nominatim(user_agent="MyApp")
    #location = geolocator.geocode(db[address_id-1].get("city"))
    results = []
    for i in db:
        if {i["city"]}==address_Location:
            results.append({'name' : i['name'], 'address1' : i['address1'], 'address2' : i['address2'], 'city' : i['city'], 'state' : i['state'], 'zip' : i['zip'], 'emails': i['emails'], 'phonenumbers': i['phonenumbers']})
    return results


#function using app() to Upadte/Create addressBook of the users
@app.post('/addresses')
def create_User(address: addressBook):
    db.append(address.dict())
    return db[-1]

#function using app() to Delete the single User w.r. to the ID.
@app.delete('/addresses/{address_id}')
def delete_User(address_id: int):
    db.pop(address_id-1)
    return {}
