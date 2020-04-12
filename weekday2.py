
# Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

import datetime
import calendar


L={0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday",6:"Sunday"}

todaydate = datetime.datetime.today().weekday()

print("Today is", L[todaydate])

if todaydate<5:
    print ( "unfortunately not weekend")

else:
    print ("finally weekend!")