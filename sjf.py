
p=[]
wt=[]
tat=[]
total=0
bt = []    
n =  input("Enter number of process:")
print("\nEnter Burst Time:\n")

for i in range(0 , n):
	print("p:",i+1)
	a =input()
        bt.append(a)
        p.append(i+1)                   
    
 

for i in range(0 , n):
       
	j = i+1
        for j in xrange(n):
            if bt[j]>bt[i]:
           	 temp=bt[j]
           	 bt[j]=bt[i]
           	 bt[i]=temp
 
            	 temp=p[j]
            	 p[j]=p[i]
              	 p[i]=temp
    
 
wt.append(0)          
 
i = 1
for i in xrange(n):
        wt.append(0)
	j = 0
        for j in xrange(i):
            wt[i]+=bt[j]
 
        total+=wt[i]
    
 
avg_wt=total/n  
total=0
 
print'\nProcess\t    Burst Time    \tWaiting Time\tTurnaround Time'
i = 0
for i in xrange(n):
        tat.append(bt[i]+wt[i])
        total+=tat[i]
        print'       ',p[i] ,  '       ' , bt[i]  , '  	',wt[i] , '	' ,tat[i]
    
 
avg_tat=total/n
print'\n\nAverage Waiting Time=',avg_wt
print'\nAverage Turnaround Time=\n',avg_tat






