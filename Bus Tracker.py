import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()


daves_latitude = 41.98062
daves_longitude = -87.668452


from xml.etree.ElementTree import parse

doc = parse('rt22.xml')


for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    
    if lat > daves_latitude:
        direction = bus.findtext('d')
        
        if direction.startswith('North'):
            busid = bus.findtext('id')
            print(busid, lat)


    
