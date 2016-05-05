process_queue = []
total_wtime = 0
st = []
wt = []
a = 0
st.append(a)
n = int(raw_input('enter the total number of processes:'))
for i in xrange(n):
	process_queue.append([])
	process_queue[i].append(raw_input('enter p_name:'))
	process_queue[i].append(int(raw_input('enter p_arrival:')))
	process_queue[i].append(int(raw_input('enter p_burst:')))
	a = a + process_queue[i][2]
        st.append(a)
        process_queue[i].append(st) 
        w = st[i] - process_queue[i][1]
	wt.append(w)
	total_wtime += wt[i]
	print ' '


print 'ProcessName\tArrivalTime\tBurstTime'
for i in xrange(n):
	print process_queue[i][0] , '\t\t', process_queue[i][1] , '\t\t' , process_queue[i][2] , '\n'
print 'Total waiting time:' , total_wtime
print 'Average waiting time:' , (total_wtime/n)
	
