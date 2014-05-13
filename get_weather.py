#!/usr/bin/env python

import json
import sys
import urllib
import urllib2

# credit due: http://openweathermap.org/

# convert kelvin to fahrenheit degrees
def kelvin_to_fahrenheit(kelvins):
    return (kelvins - 273.15) * 1.8 + 32

# grab the weather from open weather map api, quoting url if needed
def grab_weather(query):
    city = urllib.quote_plus(query)
    query = 'http://api.openweathermap.org/data/2.5/weather?q={}'.format(city)

    resp = urllib2.urlopen(query)
    weather = json.loads(resp.read())
    resp.close()
    degrees = kelvin_to_fahrenheit(int(weather['main']['temp']))

    print 'City : {}'.format(weather['name'])
    print 'Temp : {}'.format(degrees)
    print 'Humidity : {}'.format(weather['main']['humidity'])

def main():
    if len(sys.argv) < 2:
        print 'Must supply city, country as argument'
        print 'Use quotes as such:'
        print '\t\'San Francisco, US\''
        sys.exit(1)
    else:
        grab_weather(sys.argv[1])

if __name__ == '__main__':
    main()
