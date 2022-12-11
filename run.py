import requests
import json
import time
import os

def run_damominer(address):
	os.system('./damominer.sh '+ address)

def check_solution(address):
	solution = 0
	while solution == 0:
		response = requests.get("https://explorer.damominer.hk/address_solution?dt=json&a={}".format(address))
		solution = int(json.loads(response.content)["total_solution"])
		if solution == 0:
			time.sleep(300)
		else:
			print('address -> ' + address + 'is ok')

if __name__ == '__main__':
	f = open("address.txt","r")
	lines = f.readlines()
	for value in lines:
		address = value.strip()
		run_damominer(address)
		check_solution(address)

