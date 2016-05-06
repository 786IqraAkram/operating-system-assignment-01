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


dec = 0
q = input("enter the time quantum= ")
for time in range(0 , total ):
	for i in range (0 , n):
		if at[i] <= time and finish [i] == 0:
			print " time |==p" , i+1 
			if rt[i] < q:
				dec = rt[i]
			else:
				dec = q
			rt[i] = rt[i] - dec
			if rt[i] == 0:
				finish[i] = 1
			for j in range (0, n):
				if j<>1 and finish[j] == 0 and at[j]<=time:
					wt[j] == dec
			time = time + dec
                        wt[i] = wt[i] + 1
#displaying data
for i in range(0 , n):
        twt+=wt[i]
        tat[i] = wt[i]+bt[i]
        ttat += tat[i]
        print "waiting time for p " , i+1 , "=" , wt[i] , "turnaround time for p " , tat[i]
print "total waiting time = " , tat , "total turnaround time= " , ttat




