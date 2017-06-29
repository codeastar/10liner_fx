import sys, requests
if (len(sys.argv) < 4):
    print("Usage: python fx_tool_single.py <From Currency> <To Currency> <Amount> ")
    sys.exit()
from_curr = sys.argv[1].upper()
to_curr = sys.argv[2].upper()
amount = float(sys.argv[3])
response = requests.get("http://api.fixer.io/latest?base="+from_curr+"&symbols="+to_curr) 
rate = response.json()['rates'][to_curr] 
print("Exchange rate: "+ str(round(rate,4))+", "+str(amount)+" "+from_curr+" = " + str(round((rate * amount), 2))  + " " +to_curr)