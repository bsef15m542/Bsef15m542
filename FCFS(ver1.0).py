#!/usr/bin/python

total_pro = int(raw_input  ("Enter Number of Processes: "))
pro_array = [ [0 for j in range(3)] for index in range((total_pro))]
time=0
index=0
#input function
def input():
	for index in range((total_pro)):
		pro_array[index][0] = raw_input("Enter Name of processes: ")
		pro_array[index][1] = int(raw_input("Enter Arrival Time of processes: "))			
		pro_array[index][2] = int(raw_input("Enter Burst Time of processes: "))

input()

pro_array.sort(key=lambda pro_array:pro_array[1])
turnarnd_time=[0 for index in range(total_pro)]
index=0
print '\n',"After FCFS Scheduling Algo, Arrangment of Processes is:",'\n'
print "Pro\tA.T\tB.T\n"
for index in range(total_pro):
	print pro_array[index][0],'\t',pro_array[index][1],'\t',pro_array[index][2],'\n'
	time+=pro_array[index][2]
	turnarnd_time[index]=time-pro_array[index][1]
index=0
for index in range(total_pro):	
	print "Turnaround Time For ",pro_array[index][0],": ",turnarnd_time[index],'\n'	

