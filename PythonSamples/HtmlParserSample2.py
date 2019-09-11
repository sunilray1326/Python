
import urllib.request
from html.parser import HTMLParser

seqAttrFound = 0
statusAttrFound = 0
amtAttrFound = 0
headDataFound = 0
sharePrice = ""
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global seqAttrFound
        global statusAttrFound
        global headDataFound
        global amtAttrFound
        ## Below line print each start tag found
        #print("Start Tag:", tag)
        # Attritubute is name value pair, 
        for attr in attrs:
            ## Below line prints each attritubte found inside each Tag
            #print("Attribute name:",  attr[0], "Attribute Value:", attr[1])
            ## we can compare attribute name or value to make some decision
            if (headDataFound == 1 and attr[0] == "data-col-seq" and attr[1] == "1"):
                seqAttrFound = 1
    
            #if ((headDataFound == 1) and (attr[0] == "data-col-seq") and (attr[1] == "2" or attr[1] == "3" or attr[1] =="4" or attr[1] =="5")):
            if ((headDataFound == 1) and (attr[0] == "data-col-seq") and (attr[1] in ["2","3","4","5"])):
                statusAttrFound = 1

            if (seqAttrFound == 0 and attr[0] == "class" and attr[1] == "fa fa-dollar"):
                amtAttrFound = 1
            
    def handle_data(self, data):
        global sharePrice
        global seqAttrFound
        global headDataFound
        global amtAttrFound
        global statusAttrFound
        
        if (data == "EPAM Systems, Inc Stock Price Forecast for 2020"):
            headDataFound = 1
            
        if (seqAttrFound == 1 and headDataFound == 1):
            sharePrice = sharePrice + data + "\n" + "----------------------"
            seqAttrFound = 0
            
        if (statusAttrFound == 1 and headDataFound == 1):
            #print("LENGTH -", len(data.strip()))
            sharePrice = sharePrice + data
            sharePrice = sharePrice.replace('\n', '')
            statusAttrFound = 0
        if (headDataFound == 1 and amtAttrFound == 1):
            #print("AMT LEN - ", len(data.strip()))
            sharePrice = sharePrice + data
            sharePrice = sharePrice.replace('\n', '')
            amtAttrFound = 0
        if (headDataFound == 1 and statusAttrFound == 0 and amtAttrFound == 0):
            print(sharePrice)
            sharePrice = ""
        if (data == "EPAM Systems, Inc Stock Price Forecast for 2021"):
            headDataFound = 0


# open a connection to a URL
url = urllib.request.urlopen("https://walletinvestor.com/stock-forecast/epam-stock-prediction")
  
# get the result code and print it
print ("\nResult code: " + str(url.getcode()) + "\n")

status = url.getcode()
if (status == 200):
    print("HTTP 200 OKAY response, processing the page")
    print("-------------------------------------------\n")
    # read the data from the URL and print it
    fData = url.read()
    parser = MyHTMLParser()
    formData = fData.decode('UTF-8')
    parser.feed(formData)
    
else:
    print("HTTP Response is NOT OKAY, not processing file")
