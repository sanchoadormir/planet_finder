import pyvo
from astropy.io.votable import parse

service = pyvo.dal.TAPService("http://voparis-tap-planeto.obspm.fr/tap")
while True:
	inf = input("Required info: ")
	inout = input("Conditions: ")
	query = "SELECT TOP 20" + inf + " FROM exoplanet.epn_core WHERE " + inout
	results = service.search(query)
	plan = str(len(results))
	print("There are  " + plan + " planets fulfilling those conditions.")
	print(results)
	newresults = str(results)
	print("-----------")
	f = open("planetfinder.txt", "a")
	f.write(inf)
	f.write("\n")
	f.write(inout)
	f.write("\n")
	f.write(newresults)
	f.write("\n")
	f.write("\n")
	f.close()

