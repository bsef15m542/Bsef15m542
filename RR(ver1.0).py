#!/usr/bin/python

total_pro = int(raw_input("Enter Number of Processes: "))
pro_array = [ [0 for j in range(3)] for i in range(total_pro)]

i=0
time=0
timeSlice = int(raw_input("Enter Time Slice: "))

#input
def input():
	for i in range(total_pro):
		pro_array[i][0] = raw_input("Enter Name of processes: ")
		pro_array[i][1] = int(raw_input("Enter Arrival Time of processes: "))			
		pro_array[i][2] = int(raw_input("Enter Burst Time of processes: "))

input()
pro_array.sort(key = lambda pro_array:pro_array[1])

import Queue
que = Queue
que = que.Queue()

que.put(pro_array[0])
temp = []
pro_turntime=[0 for i in range(total_pro)]
pro_id=[0 for i in range(total_pro)]
store=1
i=0

#insertion in Queue
def insert():
	if(store < (total_pro)):
		while (time > pro_array[store][1]):
			que.put(pro_array[store])
			store+=1
			if store == (total_pro):
				break


print '\n',"After Roubin Round Algo, Arrangment of Processes in Ready Queue is:",'\n'
while not que.empty():
	temp=que.get()	
	if temp[2] > (timeSlice):
		time=time+(timeSlice)
		print temp
		temp[2] = temp[2]-(timeSlice)
		insert()
		que.put(temp)
	else:
		print temp
		time=time+temp[2]
		pro_turntime[i] = time-temp[1]
		pro_id[i] = temp[0]
		i+=1
		insert()
i=0
for i in range(total_pro):	
	print "Turnaround Time For ",pro_id[i],": ",pro_turntime[i],'\n'	
