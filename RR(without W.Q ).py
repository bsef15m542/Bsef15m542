#!/usr/bin/python

total = int(raw_input("Enter Number of Processes: "))
array = [ [0 for j in range(3)] for i in range(int(total))]

i=0
t=0
timeSlice = int(raw_input("Enter Time Slice: "))
for i in range(total):
	array[i][0] = raw_input("Enter Name of processes: ")
	array[i][1] = int(raw_input("Enter Arrival Time of processes: "))			
	array[i][2] = int(raw_input("Enter Burst Time of processes: "))

array.sort(key = lambda array:array[1])

import Queue
q = Queue
q = q.Queue()

q.put(array[0])
temp = []
a=[0 for i in range(total)]
b=[0 for i in range(total)]
store=1
i=0
print '\n',"After Roubin Round Algo, Arrangment of Processes in Ready Queue is:",'\n'
while not q.empty():
	temp=q.get()	
	if temp[2] > (timeSlice):
		t=t+(timeSlice)
		print temp
		temp[2] = temp[2]-(timeSlice)
		if (store < (total)):
			while t>= array[store][1]:
				q.put(array[store])
				store+=1
				if store == (total):
					break
		q.put(temp)
	else:
		print temp
		t=t+temp[2]
		a[i] = t-temp[1]
		b[i] = temp[0]
		i+=1
		if(store < (total)):
			while (t>array[store][1]):
				q.put(array[store])
				store+=1
				if store == (total):
					break
i=0
for i in range(total):	
	print "Turnaround Time For ",b[i],": ",a[i],'\n'	
