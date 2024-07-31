soldunits = int( input("How many units did you sell?") )

totalprice = soldunits * 99


if soldunits >= 10 and soldunits <=19:
   totalprice = totalprice - (totalprice * .2) #20% off
elif soldunits >= 20 and soldunits <= 49:
   totalprice = totalprice - (totalprice * .3) #30% off
elif soldunits >= 50 and soldunits <= 99:
   totalprice = totalprice - (totalprice * .4) #40% off
elif soldunits >= 100:
   totalprice = totalprice - (totalprice * .5) #50% off

print( f"Your final total is ${totalprice}" ) 