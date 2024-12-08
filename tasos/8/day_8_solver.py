grid=open("input.txt").read().split("\n")[:-1]

antennas="".join(grid)
antennas=set(antennas)
antennas.remove(".")

grid=[list(i) for i in grid]

limit_i=len(grid)
limit_j=len(grid[0])


def get_coords(antenna):
	global grid
	coords=[]
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]==antenna:
				coords.append((i,j))
	return coords

def coords_correct(coord):
	global limit_i
	global limit_j
	i=coord[0]
	j=coord[1]
	if i <0 or j <0 or i>=limit_i or j>=limit_j:
		return False
	return True


antidotes=[]
antidotes_step2=[]

def step_2_antinodes(coord,diff):
	coords=[]
	new_i=coord[0]+diff

for antenna in antennas:
	coords=get_coords(antenna)
	
	for coord_1 in range(len(coords)):
		for coord_2 in range(coord_1+1,len(coords)):
			distance_i=coords[coord_2][0]-coords[coord_1][0]
			distance_j=coords[coord_2][1]-coords[coord_1][1]
			point_1=(coords[coord_2][0]+distance_i,coords[coord_2][1]+distance_j)
			point_2=(coords[coord_1][0]-distance_i,coords[coord_1][1]-distance_j)
			antidotes.append(point_1)
			antidotes.append(point_2)


			# part 2
			antidotes_step2.append(point_1)
			antidotes_step2.append(point_2)
			antidotes_step2.append(coords[coord_1])
			antidotes_step2.append(coords[coord_2])

			while 0<=point_1[0]<limit_i and 0<=point_1[1]<limit_j:
				point_1=(point_1[0]+distance_i,point_1[1]+distance_j)
				antidotes_step2.append(point_1)

			while 0<=point_2[0]<limit_i and 0<=point_2[1]<limit_j:

				point_2=(point_2[0]-distance_i,point_2[1]-distance_j)
				antidotes_step2.append(point_2)






antidotes=[i for i in antidotes if coords_correct(i)]
antidotes=set(antidotes)
print("ANTINODES {}".format(len(antidotes)))


antidotes_step2=[i for i in antidotes_step2 if coords_correct(i)]

antidotes_step2=set(antidotes_step2)
print("ANTINODES STEP 2 {}".format(len(antidotes_step2)))
