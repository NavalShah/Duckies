import requests
from bs4 import BeautifulSoup

'''Home screen'''
url = "https://parents.sbschools.org/genesis/sis/view?gohome=true"

'''url for password entry?'''
url2 = "https://parents.sbschools.org/genesis/sis/j_security_check?parents=Y"

studentID = ""

r = requests.post(url2,data={'username': 'value', 'password': 'value'})
print(r)