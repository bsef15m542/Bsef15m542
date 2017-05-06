#!/usr/bin/python

total = int(raw_input  ("Enter Number of Processes: "))
array = [ [0 for j in range(4)] for i in range((total))]

i=0
for i in range((total)):
	array[i][0] = raw_input("Enter Name of processes: ")
	array[i][1] = int(raw_input("Enter Arrival Time of processes: "))			
	array[i][2] = int(raw_input("Enter Priority of processes: "))
	array[i][3] = int(raw_input("Enter Burst Time of processes: "))

array.sort(key=lambda array:array[1])

i=0
c=0
temp=0
k=0
l=0
t=0
flag=0
a=[0 for i in range((total))]
print '\n',"After Priority Scheduling Algo, Arrangment of Processes is:",'\n'

for i in range((total-1)):
	print array[i]
	j=i+1
	t+=array[i][3]
	a[i] = t-array[i][1]
	if (t<array[j][1]):
		t=t+(array[j][1]-t)
	while (j<total and t >= array[j][1]):
		j+=1
	k=i+1
	l=array[k][2]
	while k<j:
		if array[k][2]<l:
			l=array[k][2]
			temp = k
			flag = 1
		k+=1
	if flag == 1:	
		c=array[i+1]
		array[i+1]=array[temp]
		array[temp]=c
		flag=0
print array[total-1],'\n'
t+=array[total-1][3]
a[total-1] = t-array[total-1][1]	

i=0
for i in range(total):	
	print "Turnaround Time For ",array[i][0],": ",a[i],'\n'	
