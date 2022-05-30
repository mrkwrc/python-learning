#! python3
# DateDetection.py - detect date from input text.
import re, pyperclip, calendar # I used a calendar to make shorter the leap year condition

dateRegex = re.compile(r'''(
	(\d+)                   # alternativly (\d|[0-2]\d|3[0-1])
	/
	(\d+)                   # alternativly (\d|0[1-2])
	/
	(\d{4})
    )''', re.VERBOSE)

def DateValidation(date):
  month_range_30=['04','06','09','11']
  
  for date in dateRegex.findall(txt):
    dateRegex.group(1)
    valid_date=True
    day = int(date[1])
    month = int(date[2])
    year = int(date[3])
    
    if day>31 or month>12 or 2999<year<1000:
        valid_date=False
        print("invalid date")       
        continue
    elif day==0 or month==0 or year==0:
        valid_date=False
        print("invalid date")
        continue
    elif day<10 and month>10:
        day = '0'+str(day)
    elif month<10 and day>10:
        month = '0'+str(month)
    elif day<10 and month<10:
        day = '0'+str(day)
        month = '0'+str(month)
        
    if month in month_range_30 and day>30:
        valid_date=False   
        
    if not calendar.isleap(year) and month=='02' and day>28:
        valid_date=False
    elif calendar.isleap(year) and month =='02' and day>29:
        valid_date=False
     
    print(str(day)+'/'+str(month)+'/'+str(year)+' is', valid_date)

txt=pyperclip.paste()
DateValidation(dateRegex)