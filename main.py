import time
import requests

while True:
    r = requests.get("https://www.abv.bg/")
    print r.headers["Date"]
    r.close()
    time.sleep(5)
