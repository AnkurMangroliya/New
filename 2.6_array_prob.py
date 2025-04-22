days = int(input("How many day's temperature? "))
temp = []
total=0
for i in range(days):
    d = int(input("Day"+str(i+1)+"'shigh temp:"))
    temp.append(d)
    total += temp[i]
avg = round(total/days,2)
print("\n Average= ",avg)

above =0
for i in range(1,len(temp)):
    if temp[i]>avg:
        above+=1

print(str(above)+" Day(s) above average.")
    