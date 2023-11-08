import Adafruit_DHT
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'firebaseproject.com'
})

sensor = Adafruit_DHT.DHT11
pin = 7

ref = db.reference('/sensor_data')

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    data = {
        'humidity': humidity,
        'temperature': temperature
    }
    ref.set(data)

firebase_admin.delete_app(cred)
