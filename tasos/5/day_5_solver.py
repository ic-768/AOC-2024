sections=open("input.txt").read()

sections=sections.split("\n\n")

rules=sections[0].split("\n")
manuals=sections[1].split("\n")[:-1]

kind={}

for rule in rules:
	i,y=rule.split("|")
	if not i in kind.keys():
		kind[i]=[]
	kind[i].append(y)

middles=0
for manual in manuals:
	pages=manual.split(",")
	
	isValid=True
	for index,page in enumerate(pages):
		for page2 in pages[:index]:
			if not page in list(kind.keys()):
				continue
			if page2 in kind[page]:
				isValid=False
				print("INVALID {} BECAUSE {} AFTER {}".format(manual,page2,page))
				break
		if not isValid:
			break

	if isValid:
		print("VALID {}".format(manual))
		offset=(len(pages)-1)/2
		offset=int(offset)
		middles+=int(pages[offset])