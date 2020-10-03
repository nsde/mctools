import requests

url = "https://raw.githubusercontent.com/FaithfulTeam/Faithful/releases/1.14.zip"

tgt = 'C:\\Users\\xitzf\\Desktop\\file.zip'


import urllib3, shutil


c = urllib3.PoolManager()


with c.request('GET', url, preload_content=False) as res, open(tgt, 'wb') as out_file:

	shutil.copyfileobj(res, out_file)