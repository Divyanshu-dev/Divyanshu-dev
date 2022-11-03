dailyTemp=[11.4,33.2,44.3]
days=input("Enter the days:")
if days==sun:
    temp=dailyTemp[0]
elif days==mon:
    temp=dailyTemp[1]
elif days==tue:
    temp=dailyTemp[2]
else:
    dailyTemp.setdefault(days,33.5)

print("the temp for:",days,"was",dailyTemp,"degree celcius")


