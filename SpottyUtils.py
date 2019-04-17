import json
import requests
import base64
import os, fnmatch

import Constants
import SpottyWrapper

def getFiles(directory, ext):
	listOfFiles = os.listdir(directory) 
	pattern = "*" + ext
	for entry in listOfFiles:  
		if not fnmatch.fnmatch(entry, pattern):
			listOfFiles.remove(entry)
	return listOfFiles


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

# load files from dir instead of getting from spotify API calls
def loadAlbumTracks(basepath):
	# {trackID: [title, explicit, duration]}
	alltracks = dict()
	filenames = getFiles(basepath, '.txt')
	for filename in sorted(filenames):
		tracks = loadJson(basepath + filename)
		alltracks.update(tracks)
	return alltracks


def sortFormatSaveAlbums(output_filename, albums):
	srt = sorted(albums.items(), key=lambda kv: kv[1])

	printString = "{\n"
	for i in range(len(srt)):
		itm = srt[i]
		a_id = "\"" + itm[0] + "\""
		a_name = "\"" + itm[1] + "\""
		printString += "    " + a_id + ": " + a_name + "," + "\n"

	printString = printString[:-2] + "\n}"
	saveString(output_filename, printString)
	# list[tuple(str, str)]
	# [(albumID, albumName)]
	return srt

# sort dictionary by track_titles
# cannot return dict, as dict is unsorted
def sortFormatSaveTracks(output_filename, tracks):
	srt = sorted(tracks.items(), key=lambda kv: kv[1][0])
	if output_filename == None:
		return srt

	printString = "{\n"
	for i in range(len(srt)):
		itm = srt[i]
		t_id = "\"" + itm[0] + "\""
		t_meta = "[\"" + itm[1][0] + "\", " + str(itm[1][1]).lower() + ", " + str(itm[1][2]) + "]"
		printString += "    "+ t_id + ": " + t_meta + "," + "\n"

	printString = printString[:-2] + "\n}"
	saveString(output_filename, printString)
	# list[tuple(str, list[str, bool, int])]
	# [(titleID, [title, explicit, duration])]
	return srt


def stringToBase64(s: str):
	return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
	return base64.b64decode(b).decode('utf-8')

def jsonifyPairs(pairs: dict) -> str:
	result = '{\n'
	for k,v in pairs.items():
		result = result + '    \"' + k + '\": \"' + v + '\",\n'
	result = result[0:-2]+ '\n}'
	return result

def jsonifyTracks(tracks: dict) -> str:
	result = '{\n'
	for k,v in tracks.items():
		title = str(v[0])
		ex = str(v[1]).lower()
		dur = str(v[2])

		result = result + '    \"' + k + '\": [\"' + title + '\", ' + ex + ', ' + dur + '],\n'
	result = result[0:-2]+ '\n}'
	return result

def simpleWordMatch(a, b):
	# aa = a.lower().replace('\'','').replace('"','').replace(',', '').rstrip(ascii.)
	return a.lower() == b.lower()

def titleMatch(a, b):
	awords = a.split(" ", 3)
	bwords = b.split(" ", 3)

	match = True
	for i in range(min(len(awords), len(bwords), 2)):
		match = match and simpleWordMatch(awords[i], bwords[i])
	return match

