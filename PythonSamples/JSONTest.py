
import urllib.request
import json

def getResult(data):
    
    # Convert str() instance containig JSON data to Python object
    ## if you use load() then it expect the parameter should have read() supported to read JSON from it
    theJSON = json.loads(data)
    
    # Print the "title" value present in "metadata" section
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
        print ("--------------------------------------------\n")
        
    #Get "count" from "metadata"
    eventCount = theJSON["metadata"]["count"]
    print("Total Earthquake Event Recorded", eventCount, "\n")
    
    for index, i in enumerate(theJSON["features"]):
        print(str(index+1) + " - " + i["properties"]["place"])
    print ("------------------------------------------------\n")
    
    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if(i["properties"]["mag"] >= 4):
            print(i["properties"]["mag"], i["properties"]["place"])
    print ("------------------------------------------------\n")

    # print only the events where at least 1 person reported feeling something
    for i in theJSON["features"]:
        felt = i["properties"]["felt"]
        ## Since felt value is null in JSON, it is type cased as NoneType in Python
        ## Got error - TypeError: '>=' not supported between instances of 'NoneType' and 'int'
        ## So first need to check if felt is not None before using it as int to compare 
        if( felt != None and felt >= 0):
            print(i["properties"]["felt"], "people reported event AT:", i["properties"]["place"])

## Below URL provides JSON response for earthquake data
## JSON defined by https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
url = urllib.request.urlopen("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")

status = url.getcode()
if(status == 200):
    print("HTTP 200 OK Response, proessing JSON data")
    print("-----------------------------------------\n")
    formData = url.read()
    #print(formData)
    getResult(formData)
else:
    print("HTTP Response NOT OK, exit program")
