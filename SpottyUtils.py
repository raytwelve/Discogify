import json
import requests
import Constants
import SpottyWrapper

def failedExe(url: str, resp: requests.models.Response):
	global user 
	print("resp="+ str(type(resp)))
	print('Failed to execute ' + url)
	print(resp.text)

def getItemsFromRequest(req_type: str, url: str, headers: dict, body: dict, params:dict, return_field:str=None):
	resp = ''
	items = {}
	if(req_type == Constants.GET):
		resp = requests.get(url, headers=headers, data=body, params=params)
	elif(req_type == Constants.POST):
		resp = requests.post(url, headers=headers, data=body, params=params)

	success = resp.status_code in Constants.SUCCESS_CODES
	if(success):
		jason = json.loads(resp.text)
		items = jason if req_type == Constants.POST else jason.get(return_field)
	else:
		failedExe(url, resp)
	return items, success

def saveJson(filename: str, jason: dict):
	with open(filename, 'w') as handle:
		handle.write(json.dumps(jason, sort_keys=True, indent=4))

def saveString(filename: str, s: str):
	with open(filename, 'w') as handle:
		handle.write(s)

def loadJson(filename: str) -> dict:
	jason = None
	with open(filename, 'r') as handle:
		contents = handle.read()
		jason = json.loads(contents)
	return jason

def loadString(filename: str) -> str:
	contents=None
	with open(filename, 'r') as handle:
		contents = handle.read()
	return contents

def jsonifyPairs(pairs: dict) -> str:
	result = '{\n'
	for k,v in pairs:
		result = result + '    \"' + k+ '\": \"' + v + '\",\n'
	result = result[0:-2]+ '\n}'
	return result