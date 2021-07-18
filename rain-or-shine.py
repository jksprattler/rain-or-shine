# coding: utf-8
import requests
import schedule
import time

params = {
  'access_key': '20632cae552122179bc1cf711773820a',
  'query': 'fetch:ip'
}

api_result = requests.get('http://api.weatherstack.com/forecast', params)

api_response = api_result.json()

rain = api_response['current']['precip']
shine = api_response['current']['uv_index']
description = api_response['current']['weather_descriptions'][0]

def job():
    if rain > 5:
      print(u'Today\'s precipitation forecast: ', rain)
      print(u'Greater than 5% chance of rain today, better grab your umbrella!')
    elif shine > 3:
      print(u'Today\'s UV Index forecast: ', shine)
      print(u'UV Index greater than 3 today, better grab your sunscreen!')
    else:
      print(u'Today\'s weather description forecast: ', description)
      print(u'Should be a pleasant day, no need for umbrella or sunscreen!')
schedule.every(3).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)