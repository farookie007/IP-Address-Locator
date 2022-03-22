import requests
import re


def getPublicIP():
    """Function to get the IP Address from 'http://checkip.dyndns.com/'"""
    data = requests.get('http://checkip.dyndns.com/')
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data.text).group(1)
