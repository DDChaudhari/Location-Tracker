print("*********************************")
print("        LOCATION TRACKER         ")
print("*********************************")
import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
key = "8e94651695e4492986201e9f3f86b102"
Dnumber = phonenumbers.parse(number)
myLocation = geocoder.description_for_number(Dnumber,"en")
print(myLocation)

#Name of service provider
from phonenumbers import  carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(myLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

location = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=myLocation).add_to((location))

#save location in html
location.save("Location.html")
