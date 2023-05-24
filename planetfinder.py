import pyvo
from astropy.io.votable import parse

service = pyvo.dal.TAPService("http://voparis-tap-planeto.obspm.fr/tap")
while True:
	req_info = input("Required info: ")
	cond = input("Conditions: ")
	query = "SELECT TOP 20" + req_info + " FROM exoplanet.epn_core WHERE " + cond
	query2 = "SELECT " + req_info + " FROM exoplanet.epn_core WHERE " + cond
	results = service.search(query)
	results2 = service.search(query2)
	plan = str(len(results2))
	print("There are  " + plan + " planets fulfilling those conditions.")
	print(results)
	newresults = str(results)
	print("--------------------")
	print("\n")
	
	f = open("planetfinder.txt", "a")
	f.write(cond)
	f.write("\n")
	f.write(inout)
	f.write("\n")
	f.write(newresults)
	f.write("\n")
	f.write("\n")
	f.close()
