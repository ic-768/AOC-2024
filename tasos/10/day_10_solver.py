
c=open("input.txt").read().split("\n")
c=[list(i) for i in c]

l_y=len(c)
l_x=len(c[0])

starting_points=[]

global_metavliti=[]

def get_neighbors(point,value,returned):

	global c

	global global_metavliti

	x=point["x"]
	y=point["y"]

	points=[{"x":x+1,"y":y},{"x":x-1,"y":y},{"x":x,"y":y+1},{"x":x,"y":y-1}]
	points=[i for i in points if 0<=i["x"]<l_x and 0<=i["y"]<l_y]
	points=[i for i in points if int(c[i["y"]][i["x"]])==value+1]
	
	
	
	if len(points)==0:
		pass
	if value==8:
		points=[i for i in points if i not in global_metavliti]
		global_metavliti.extend(points)
	else:	
		[get_neighbors(p,value+1,returned) for p in points]



	



ssum=0



for y,line in enumerate(c):
	for x,char in enumerate(line):
		if char=="0":
			point={"x":x,"y":y}
			starting_points.append(point)
			global_metavliti=[]
			get_neighbors(point,0,[])
			ssum+=len(global_metavliti)
			
			global_metavliti=[]


print(c[2][7])

print(ssum)
