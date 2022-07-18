import ast

with open("pikalytics.stats", "r") as rf:
		pokedict = ast.literal_eval(rf.read())

def search_dict(name, pokedict):
	matches = []
	name = name.replace("-*", "")
	for key in pokedict.keys():
		if name in key:
			matches.append(pokedict[key])

	return matches

if __name__ == "__main__":

	print(search_dict("Necrozma", pokedict)[0]["name"])