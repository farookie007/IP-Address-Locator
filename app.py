from functions import getPublicIP


IP = getPublicIP()

# Getting the Details
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Displaying the Extracted Details
print("Your City : ".ljust(20) + city.ljust(20))
print("Your Region : ".ljust(20) + region.ljust(20))
print("Your Country : ".ljust(20) + country.ljust(20))
print("Your Location : ".ljust(20) + location.ljust(20))
print("Your IP Address: ".ljust(20) + IP.ljust(20))
