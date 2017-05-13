#!/usr/bin/python

total_pro = int(raw_input  ("Enter Number of Processes: "))
pro_array = [ [0 for j in range(4)] for i in range((total_pro))]

i=0
#input Method
def input():
	for i in range((total_pro)):
		pro_array[i][0] = raw_input("Enter Name of processes: ")
		pro_array[i][1] = int(raw_input("Enter Arrival Time of processes: "))			
		pro_array[i][2] = int(raw_input("Enter Priority of processes: "))
		pro_array[i][3] = int(raw_input("Enter Burst Time of processes: "))

input()
pro_array.sort(key=lambda pro_array:pro_array[1])

i=0
next_ind=0
temp_pro=0
temp_index=0
start_ind=0
priority=0
time=0
flag=0
turnarnd_time=[0 for i in range(total_pro)]
print '\n',"After Priority Scheduling Algo, Arrangment of Processes is:",'\n'

for i in range((total_pro-1)):
	print pro_array[i]
	next_ind = i+1
	time += pro_array[i][3]
	turnarnd_time[i] = time-pro_array[i][1]
	if (time < pro_array[next_ind][1]):
		time=time+(pro_array[next_ind][1]-time)
	while (next_ind<total_pro and time >= pro_array[next_ind][1]):
		next_ind += 1
	start_ind=i+1
	priority=pro_array[start_ind][2]
	while start_ind < next_ind:
		if pro_array[start_ind][2] < priority:
			priority = pro_array[start_ind][2]
			temp_index = start_ind
			flag = 1
		start_ind+=1
	if flag == 1:	
		temp_pro = pro_array[i+1]
		pro_array[i+1]=pro_array[temp_index]
		pro_array[temp_index] = temp_pro
		flag=0
print pro_array[total_pro-1],'\n'
time+=pro_array[total_pro-1][3]
turnarnd_time[total_pro-1] = time-pro_array[total_pro-1][1]	

i=0
for i in range(total_pro):	
	print "Turnaround Time For ",pro_array[i][0],": ",turnarnd_time[i],'\n'	
