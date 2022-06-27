from geopy.geocoders import Nominatim
from geopy import distance
geolocater=Nominatim(user_agent="sample")
geocoder=Nominatim(user_agent="sample")
geolocater=Nominatim(user_agent="sample")

location1=input("Enter location1:")
location2=input("Enter location2:")
print()

name1=geolocater.geocode(location1)
name2=geolocater.geocode(location2)


print("The location1 name is",name1.address)
print("The location2 name is",name2.address)
print()


coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)

lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

place1=(lat1,long1)
place2=(lat2,long2)

print("The distance between location1 and location2 is",distance.distance(place1,place2).km,"kms")
