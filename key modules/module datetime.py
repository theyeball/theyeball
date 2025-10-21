import datetime
# datetime is a module to use, you guessed it, the date and time

# using the current date and time
right_now = datetime.datetime.now()
print(right_now)

# you could also use specific information about the current date and time
x = datetime.datetime.now()

print(x.month)
print(x.minute)
print(x.microsecond)

# using a specific date and time
someguys_birthday = datetime.datetime(2006,2,14) # 3 to 6 parameters (year/month/day/hour/minute/second)
print(someguys_birthday)
print(someguys_birthday.year)

# you could input just the date or the time and output it as well
somedate = datetime.date(2013,7,8) # must include 3 parameters with year/month/day
print(somedate)
print(somedate.day)

sometime = datetime.time(13,45,2) # up to 3 parameters with hour/minute/second
print(sometime)

# strftime()
# this function allows you to convert the numerical information(month 11 date 13) to readable strings(November 13th)

print(someguys_birthday.strftime("%B")) # this will print the guys birthmonth

# you could also use multiple codes to show different parts of a date and time
print(someguys_birthday.strftime("%H:%M:%S %A %d")) # this will print hour:minute:second, weekday, then day of month
# all codes for strftime()

# %a	Weekday, short version	    Sun
# %A	Weekday, full version	    Sunday	
# %w	Weekday as a number         0-6 
# %d	Day of month                01-31
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number           01-12
# %y	Year, short version, without century	
# %Y	Year, full version	
# %H	Hour                        00-23	
# %I	Hour                        00-12	
# %p	AM/PM		
# %M	Minute                      00-59		
# %S	Second                      00-59		
# %f	Microsecond                 000000-999999	
# %z	UTC offset	                
# %Z	Timezone	
# %j	Day number of year          001-366	
# %U	Week number of year, Sunday as the first day of week 00-53
# %W	Week number of year, Monday as the first day of week 00-53
# %c	Local version of date and time Mon Dec 31 17:41:00 2018	
# %C	Century
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	
# %u	ISO 8601 weekday 
# %V	ISO 8601 weeknumber 
