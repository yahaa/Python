import urllib2
import urllib

values={"username":"yahaa","password":"Asd147258"}
data=urllib.urlencode(values)
url="ftp://115.29.146.79"
req=urllib2.Request(url,data)
resp=urllib2.urlopen(req)
print resp.read()