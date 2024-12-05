reports=open("input.txt").read().split("\n")[:-1]

sum_safe=0
sum_safe_with_errors=0

def check_diff(x,y):

	return True if 1<=abs(x-y)<=3 else False

def check_level(levels):
	plusmin=1
	valid=True
	errors=0
	error_index=-1
	

	for index,level in enumerate(levels):
		if index==0:
			continue
		elif index==1:
			if levels[index]-levels[index-1]>0:
				plusmin=1
			else:
				plusmin=-1
		else:
			diff=levels[index]-levels[index-1]
			
			if diff*plusmin<0:
				valid=False
				error_index=index
				break
				

		if not check_diff(levels[index],levels[index-1]):
			valid=False
			error_index=index
			break
			
	return valid,error_index


for i in reports:

	level=[int(j) for j in i.split()]
	result=check_level(level)

	if result[0]:
		sum_safe+=1
		sum_safe_with_errors+=1

	else:
		if result[1]==1:
			l=level.copy()
			l.pop(1)
			result=check_level(l)
			if result[0]:
				sum_safe_with_errors+=1
				print(i)
				
			else:
				l=level.copy()
				l.pop(0)
				result=check_level(l)
				if result[0]:
					sum_safe_with_errors+=1
					print(i)
		else:
			l=level.copy()
			l.pop(result[1])
			result=check_level(l)
			if result[0]:
				sum_safe_with_errors+=1
				print(i)

					




print(sum_safe)

print(sum_safe_with_errors)
