import requests
import json
import re
import webbrowser
import time
#######此处设置配置
Price = 10
ram = 500
cpu = 1
location = "LOS ANGELES, CA"
#######
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
while True:
	response = requests.get("https://billing.virmach.com/modules/addons/blackfriday/new_plan.json",params ="" , headers = headers)
	res = response.json()
	print(res) 
	if float(re.search(r"\d+\.?\d*",res["price"]).group()) < Price:
		if int(res["ram"]) >= ram:
			if int(res["cpu"]) >= cpu:
				if res["location"] == location:
					webbrowser.open("https://billing.virmach.com/cart.php?a=add&pid=175&billingcycle=annually")
					break
	time.sleep(10)
