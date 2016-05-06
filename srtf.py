at=[]
bt=[]
x=[]
tat=[]
wt = []
rt = []
finish = []
low = 0
n = input( "enter the number of Processes:\n")
print"enter arrival time\n"
for i in range(0 , n):
	at.append(input())
print "enter burst time\n"
for i in range(0 , n):
 	bt.append(input()) 
total = 0
twt = 0
ttat = 0
for i in range (0 , n):
	rt.append(bt[i])
	finish.append(0)
	wt.append(0)
	tat.append(0)
	total+=bt[i]
#selecting next process
for i in range(0,n):
	if finish == 0:
		low = i
for i in range(0,n):
	if finish[i] <> 1:
		if rt[i] < rt[low] and at[i] <= time:
			low = i


for time in range(0 , total):
	old = next
	next = low
	if  old <> next or time == 0:
		print "time|==p" , next+1
		rt[next] = rt[next] - 1
	if rt[next]== 0:
		finish[next] = 1
	for i in range (0 , n):
		if i<> next and at[i] <= time and finish[i] == 0:
			wt[i] = wt[i] + 1
#displaying data
for i in range(0 , n):
	twt+=wt[i]
	tat[i] = wt[i]+bt[i]
	ttat += tat[i]
	print "waiting time for p " , i+1 , "=" , wt[i] , "turnaround time for p " , i+1 , " = " , tat[i]
print "total waiting time = " , tat , "total turnaround time= " , ttat
