def formula(x,y):
   return (3*x) + (5*y) 


result = formula(2,3)

# print( f"The calculated result is {result}" )



# Part 2

hourlyrate = int( input("How much do you get paid hourly?") )
hoursworked = int( input("How many hours have you worked this week?") )

regularpay = 40 * hourlyrate
totalpay = regularpay
overtime = 0

if(hoursworked > 40):
   overtime = (hoursworked - 40) * (hourlyrate * 1.5)

   totalpay = totalpay + overtime 

print(f"Regular pay {regularpay}")
print(f"Overtime pay {overtime}")
print(f"Total pay {totalpay}")



