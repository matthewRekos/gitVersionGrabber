#Matthew Rogers
#Currently configured for openSSL

from bs4 import BeautifulSoup
import httplib2
import re
import time
import subprocess
names = []
page = "https://github.com/openssl/openssl/releases"
while len(names) < 247:
	http= httplib2.Http()
	content = str(http.request(page))
	soup = BeautifulSoup(content,'html.parser')
	tags = soup.find_all('span', attrs={'class':'tag-name'})
	names+= [tag.text for tag in tags]
	if len(names)>0:
		page = "https://github.com/openssl/openssl/releases?after=" + names[-1]

for name in names:
	cmd = "wget https://github.com/openssl/openssl/archive/" + name +".zip"
	subprocess.check_output(cmd,shell=True,stderr = subprocess.PIPE)
