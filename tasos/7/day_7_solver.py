x=open("input.txt").read().split("\n")[:-1]
praxeis={}
for i in x:
	i=i.split(":")
	praxeis[i[0]]=[]
	for i2 in i[1].split():
		praxeis[i[0]].append(i2)

endresult=0

for praxi in praxeis:
	print("here",praxi)
	operands=[int(i) for i in praxeis[praxi]]
	len_operators=len(operands)-1

	operators_combos=2**(len(operands)-1)

	operations=[]
	for i in range(operators_combos):
		bin_i=bin(i)
		bin_i=bin_i.replace("0b","").zfill(len_operators)

		operations.append(bin_i)

	print(operands)
	for operation in operations:

		result=0

		for i in range(1,len(operands)):
			curr_op=operation[i-1]
			if curr_op=="0":
				if result==0:
					result+=operands[i-1]*operands[i]
				else:
					result=result*operands[i]
			else:
				if result==0:
					result+=operands[i-1]+operands[i]
				else:
					result+=operands[i]


		if result==int(praxi):
			print("FOUND")
			endresult+=result
			break

print(endresult)