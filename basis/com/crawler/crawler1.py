import urllib2
request=urllib2.Request("http://www.baidu.com")
rep=urllib2.urlopen(request)

output=open("baidu.html","w")
output.write(rep.read())


