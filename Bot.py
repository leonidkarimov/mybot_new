import urllib
try:
    stri = "api.telegram.me"
    data = urllib.urlopen(stri)
    print("Connected")
except:
    print("not connected")
