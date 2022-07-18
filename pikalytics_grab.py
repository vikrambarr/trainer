import requests
from requests.exceptions import JSONDecodeError
import math

sugar = requests.session()
print("\nBeginning download.")

# Get ranked list of mons from pikalytics api
list_of_mons = sugar.get("https://www.pikalytics.com/api/l/2022-05/gen8nationaldexag-1760").json()
num_mons = len(list_of_mons)

mon_info = {}
to_remove = []

# For every mon on the ranked list, grab its complete info set, including mons without one
for pos, mon in enumerate(list_of_mons):
	
    progress = math.floor(40*((pos+1)/num_mons))
    
    print("\r", end = "")
    print("(" + str(pos+1) + " "*(4-len(str(pos+1))) + "/" + str(num_mons) + ")  " + "█"*progress + "_"*(40-progress) + "  " + mon["name"] + " "*10, end = "")
    
    new_mon = sugar.get("https://www.pikalytics.com/api/p/2022-05/gen8nationaldexag-1760/" + mon["name"])
    
    try:
        _name = new_mon.json()['name']
        mon_info.update({_name: new_mon.json()})
        #print(f"{_name}{(30-len(_name))*' '}DATA FOUND")

    except JSONDecodeError:
        #print(f"{list_of_mons[pos]['name']}{(30-len(list_of_mons[pos]['name']))*' '}NO DATA")
        pass

    
print(f"\n\nFound data on {len(mon_info)} mons out of {num_mons}.")

with open("pikalytics.stats", "w") as wf:
        
        wf.write(str(mon_info))
        
        