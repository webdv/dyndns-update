import urllib, urllib2, yaml, sys


try:
    currentip = urllib.urlopen('http://www.whatismyip.org').read()
except:
    print "Error trying to hit whatismyip.org.  The site is flaky at times -- Try it again..."
    sys.exit(1)

config = yaml.load(open("config.yaml").read())
try:
    username = config["username"]
    password = config["password"]
    hostname = config["hostname"]
except:
    print "Error parsing yaml file.  Did you read the README?"
    sys.exit(1)
#build url parameters
params = urllib.urlencode({'hostname': hostname, "myip": currentip})
url = 'http://members.dyndns.org/nic/update?%s' % params

def updateip():
    try: 
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None,url , username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(url)
    except:
        print "Error during authentication.  Likely bad username."
        sys.exit(1)
        
if __name__ == "__main__":
    updateip()
