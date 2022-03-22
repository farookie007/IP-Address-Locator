import requests

from functions import getPublicIP

if __name__ == '__main__':
	IP_addr = getPublicIP()

	# Sending the request and getting the json
	url = f'http://ipinfo.io/{IP_addr}/json'
	response = requests.get(url)
	data = response.json()

	# Extracting the Results
	print('###############################################')
	print("Your City : ".ljust(20) + data['city'].ljust(20))
	print("Your Region : ".ljust(20) + data['region'].ljust(20))
	print("Your Country : ".ljust(20) + data['country'].ljust(20))
	print("Your Location : ".ljust(20) + data['loc'].ljust(20))
	print("Your IP Address: ".ljust(20) + data['ip'].ljust(20))
	print("Your ISP:".ljust(20) + data['org'].ljust(20))
	print("Your Timezone: ".ljust(20) + data['timezone'].ljust(20))
	print('###############################################')
