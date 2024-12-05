import re


regexp="mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"

data=open("input.txt").read()

muls=re.findall(regexp,data)

sum=0
sum_do=0

for mul in muls:
	sum+=int(mul[0])*int(mul[1])

print(sum)

data=data.split("do()")

for d in data:
	if "don't()" in d:
		d=d[:d.index("don't()")]
	muls=re.findall(regexp,d)
	for mul in muls:
		sum_do+=int(mul[0])*int(mul[1])

print(sum_do)