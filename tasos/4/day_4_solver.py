
data=open("input.txt").read().split("\n")
print(len(data))


data=[list(i) for i in data]

limit_i=len(data)
limit_j=len(data[0])

def check_coords(i,j):
	if i<0 or j<0 or i>=limit_i or j >= limit_j:
		return False
	return True


def check_M(i,j):


	for step_2_i_offset in range(-1,2): # -1,0,1
		step_2_i=i+step_2_i_offset
		for step_2_j_offset in range(-1,2):

			step_2_j=j+step_2_j_offset

			if not check_coords(step_2_i,step_2_j):
				continue
			if data[step_2_i][step_2_j]=="M":
				check_A(step_2_i,step_2_j,step_2_i_offset,step_2_j_offset)
			


def check_A(i,j,step_2_i_offset,step_2_j_offset):
	step_2_i=i+step_2_i_offset
	step_2_j=j+step_2_j_offset


	if not check_coords(step_2_i,step_2_j):
		return

	if data[step_2_i][step_2_j]=="A":
		check_S(step_2_i,step_2_j,step_2_i_offset,step_2_j_offset)


ssum=0

def check_S(i,j,step_2_i_offset,step_2_j_offset):
	global ssum


	step_2_i=i+step_2_i_offset

	step_2_j=j+step_2_j_offset

	if not check_coords(step_2_i,step_2_j):
		return
	if data[step_2_i][step_2_j]=="S":
		ssum+=1


for i in range(len(data)):
	for j in range(len(data[i])):
		candidate=data[i][j]
		if candidate=="X":
			check_M(i,j)
			
print(ssum)
