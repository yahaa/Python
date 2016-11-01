import urllib
import urllib2
url='http://www.baidu.com'
values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }    
data=urllib.urlencode(values)
print data
req=urllib2.Request(url,data)
response=urllib2.urlopen(req)
html=response.read()
print html

