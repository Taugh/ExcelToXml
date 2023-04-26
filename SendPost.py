import requests

def sendPost(xml):
    url = 'https://xmlpo.brucknersupply.com/cgi/ALNXMLIN'
    poFile = xml
    #print(y) for testing purposes
    headers = {'Content-Type': 'text/xml'}

    with open(poFile, 'r') as x:
        z=x.read()
        r = requests.post(url, data=z, headers=headers, verify = False)
    #print(z) for testing purposes
    print(r.status_code)