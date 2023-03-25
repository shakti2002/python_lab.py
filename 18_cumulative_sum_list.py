def cumSum(s):
   sm=0
   cum_list=[]
   for i in s:
      sm=sm+i
      cum_list.append(sm)
   return cum_list

a=[10,20,30,40,50]
print(cumSum(a))