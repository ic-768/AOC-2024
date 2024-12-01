x=open("input.txt").read().split("\n")[:-1]

l1=[]
l2=[]
for i in x:
	temp=i.split("   ")
	l1.append(int(temp[0]))
	l2.append(int(temp[1]))


l1=sorted(l1)
l2=sorted(l2)


diffsum=0

l1=[i.split() for i in x]

print(l1,l2)

for i in range(len(l1)): # l1 and l2 are of equal length
	diff=abs(l1[i]-l2[i])
	diffsum+=diff

print(diffsum)



# part 2

relative_sum=0
for i in l1:
	relative_sum+=i*l2.count(i)

print(relative_sum)