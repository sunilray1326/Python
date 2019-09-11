
import urllib.request
from html.parser import HTMLParser

seqAttrFound = 0
amtAttrFound = 0
headDataFound = 0
sharePrice = ""
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global seqAttrFound
        global headDataFound
        global amtAttrFound
        ## Below line print each start tag found
        #print("Start Tag:", tag)
        # Attritubute is name value pair, 
        for attr in attrs:
            ## Below line prints each attritubte found inside each Tag
            #print("Attribute name:",  attr[0], "Attribute Value:", attr[1])
            ## we can compare attribute name or value to make some decision
            if (headDataFound == 1 and attr[0] == "data-col-seq") and (attr[1] == "1"):
                seqAttrFound = 1
                #print("EPAM 2020 Forecast")
                #dummy = input()
            if (seqAttrFound == 1 and attr[0] == "class" and attr[1] == "fa fa-dollar"):
                amtAttrFound = 1
            
    def handle_data(self, data):
        global sharePrice
        global seqAttrFound
        global headDataFound
        global amtAttrFound
        if (data == "EPAM Systems, Inc Stock Price Forecast for 2020"):
            #print("Data     :", data)
            headDataFound = 1
        if (seqAttrFound == 1 and headDataFound == 1 and data != "Open: " and amtAttrFound == 0):
            #print("DATA:", data)
            sharePrice = sharePrice + data + ", "     
        if (seqAttrFound == 1 and headDataFound == 1 and data == "Open: "):
            #print("Open Found", data)
            sharePrice = sharePrice + "Open Price"
        if (amtAttrFound == 1):
            sharePrice = sharePrice + data
            headDataFound = 0
            seqAttrFound = 0
            amtAttrFound = 0
            print(sharePrice)
            sharePrice = ""

# open a connection to a URL
url = urllib.request.urlopen("https://walletinvestor.com/stock-forecast/epam-stock-prediction")
  
# get the result code and print it
print ("\nResult code: " + str(url.getcode()))
print("\n HTTP Header")
print("------------------------------------------------")
print(str(url.info()))
print("------------------------------------------------")

# read the data from the URL and print it
print("\nForm Data\n")
fData = url.read()
parser = MyHTMLParser()

## parser.feed(str(fData)) was giving incorrect result while parsing below 2 lines
## The starttag() method printed Start Tag as td\nclass="w4" incorrectly
#class="w4" data-key="3"><td
#class="w4 kv-grid-group" data-col-seq="0" data-group-key="23920167"
## parser.feed(str(fData))

# To resolve starttag issues, converted all form data to UTF-8 and then 
# feed this to parser to parse startag correctly
formData = fData.decode('UTF-8')
parser.feed(formData)


## Code read HTML file from a saved disk file and process it
#file = open("EPAM.html", "r")
#content = ''
#for line in file:
#    content += line
#parser.feed(content)