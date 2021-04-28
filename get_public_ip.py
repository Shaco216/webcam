import requests

def get_ip():
    f = requests.request('GET', 'http://myip.dnsomatic.com') #http://whatismyip.org
    ip = f.text
    return ip
#print(ip)
if __name__ == '__main__':
    get_ip()