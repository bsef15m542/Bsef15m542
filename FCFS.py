#!/usr/bin/python

total = int(raw_input  ("Enter Number of Processes: "))
array = [ [0 for j in range(3)] for i in range((total))]
t=0
i=0
for i in range((total)):
	array[i][0] = raw_input("Enter Name of processes: ")
	array[i][1] = int(raw_input("Enter Arrival Time of processes: "))			
	array[i][2] = int(raw_input("Enter Burst Time of processes: "))

array.sort(key=lambda array:array[1])
a=[0 for i in range(total)]
i=0
print '\n',"After FCFS Scheduling Algo, Arrangment of Processes is:",'\n'
print "Pro\tA.T\tB.T\n"
for i in range(total):
	print array[i][0],'\t',array[i][1],'\t',array[i][2],'\n'
	t+=array[i][2]
	a[i]=t-array[i][1]
i=0
for i in range(total):	
	print "Turnaround Time For ",array[i][0],": ",a[i],'\n'	

