from numpy import cos, sin, arcsin, sqrt, radians
from numpy import random

def haversine(lat_query, lon_query, lat_ref, lon_ref):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) *in kms*
    """
    # convert decimal degrees to radians 
    lon_query, lat_query, lon_ref, lat_ref = map(radians, [lon_query, lat_query, lon_ref, lat_ref])
    # haversine formula 
    dlon = lon_query - lon_ref 
    dlat = lat_query - lat_ref 
    a = sin(dlat/2)**2 + cos(lat_query) * cos(lat_ref) * sin(dlon/2)**2
    c = 2 * arcsin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


print(haversine(48.8566, 2.3522, 48.8566, 2.3522)) # Distance Paris - Paris
print(haversine(35.6762, 139.6503, 48.8566, 2.3522)) # Distance Paris - Tokyo
print(haversine(52.5200, 13.4050, 48.8566, 2.3522)) # Distance Paris Berlin = 878km approx.


lat_query = random.uniform(low=-90.0, high=90.0, size=100)
lon_query = random.uniform(low=-90.0, high=90.0, size=100)
lat_ref = random.uniform(low=-90.0, high=90.0, size=300)
lon_ref = random.uniform(low=-90.0, high=90.0, size=300)

print(haversine(lat_query, lon_query, lat_ref, lon_ref).size) # Does not work because of the size of the arrays