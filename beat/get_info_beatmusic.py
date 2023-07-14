import requests
from bs4 import BeautifulSoup as bs
import lxml.html

# TODO
protein = "5uv8_binary"
trj_num = "trj08"

url_path = f"/mnt/c/users/komad/documents/url_result/beatmusic/{protein}/beatmusic_url_{protein}_{trj_num}.txt"
result_path = f"/mnt/c/users/komad/documents/ppi_result/beatmusic/{protein}/{trj_num}.txt"


fw = open(result_path,"w")
fw.write("")
fw.close()

with open(url_path) as f:
  lines = f.readlines()

size = len(lines)
print(size)

for j in range(size):
  lines[j] = lines[j].replace('\n', '')

for i in range(size):
  url = lines[i]
  res_mcsm = requests.get(url)
  soup_mcsm = bs(res_mcsm.text,'html.parser')
  pred = soup_mcsm.find_all("b")
  result = pred[3].text
  print(result)
  
  fa = open(result_path,"a" )
  result = result + "\n"
  fa.write(result)
  fa.close()
  
