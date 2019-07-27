##########################
## check account blance ##
## author: Yudi Xu      ##
## version: v0.0.1      ##
## data: 2019 July 16th ##
## project: mini evec   ##
##########################



import requests
import re

url = 'http://localhost:8080/'

# check balance
def chkBalance(accountNum, pvtKey):
	""" Check balance of a hedera account
		Parameters
		------------
		accountNum : String
			In the format "<ShardNum>.<Realm Number> . <Account Number>"
			Example: '0.0.4032'
		pvtKey : String
			private key
		Returns
		------------
		balance : int
	"""
	body = {"accountNum": accountNum, "pvtKey": pvtKey }
	response = requests.post(url+'balance', json=body)
	#print(device_name, accountNum, currBalance)
	regex = "^[-+]?[0-9]+$"
	if re.search(regex,response.content.decode('utf-8')) == None:
	#if response.status_code != 200 or response.content.decode('utf-8')=="-1":
		raise Exception("Check that you have enough funds")
	return int(response.content.decode('utf-8'))

# this info should be taken from the web user input. code needs to be updated by full stack developer
device_name = 'Sensor X'
accountNum = '0.0.34756' #device A:  B: 0.0.32932
#pvtKey = '302e020100300506032b657004220420a2b7dcd80b799f05447605de448e3cd962d2a45672c12ebfa92f2aae6dc0f48d' # account: 0.0.32932
pvtKey = '302e020100300506032b6570042204201727a1006f15c43902b372111e28c72087fbdaad53624814f70bf59a68f7352e' # account: 0.0.34756
currBalance = chkBalance(accountNum,pvtKey)

print(device_name, accountNum, currBalance)


