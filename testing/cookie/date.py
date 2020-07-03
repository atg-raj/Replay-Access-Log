from datetime import datetime 
#can use timezone instead

# returns current date and time  Sun, 26-Jul-2020 19:44:29 GMT        
#SIDCC=AJi4QfF1kGJSP1eLOrivNIENyUz48E0v6f--X1Kx8HhjjwuX9oeiuP1GbpPv2nIgC7Ner2ZjaA; expires=Thu, 01-Jul-2021 12:22:58 GMT; path=/; domain=.google.com; priority=high
#india 5hr 30 mins ahead of GMT , GMT=12:30 PM In=6 pm
def month_conv(argument): 
    switcher = { 
        "Jan": 1, 
        "Feb": 2, 
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }  
    return switcher.get(argument, 0)

def check_expiry(argument):
	co_date=argument.split(' ')
	date=co_date[1].split('-')
	date[0]=int(date[0])
	date[2]=int(date[2])
	date[1]=month_conv(date[1])
	time=co_date[2].split(':')
	time[0]=int(time[0])
	time[1]=int(time[1])
	time[2]=int(time[2])
	time[1]+=30
	time[0]+=5+(time[1]//60)
	if time[0]//24 == 1:
		date[0]+=1
		if (date[1]%2 == 1 and date[1] < 8) or (date[1]%2 == 0 and date[1] > 7):
			if date[0]==32:
				date[0]=1
				date[2]+=date[1]//12
				date[1]%=12
				date[1]+=1
		elif date[1] != 2:
			if date[0]==31:
				date[0]=1
				date[1]+=1
		elif date[2]%4 != 0 and date[0]==29:
			date[0]=1
			date[1]+=1
		elif date[0]==30:
			date[0]=1
			date[1]+=1		
	time[0]%=24
	time[1]%=60
	now = datetime.now() 
	m=str(now.month)
	if now.month<10:
		m='0'+str(now.month)
	d=str(now.day)
	if now.day<10:
		d='0'+str(now.day)
	h=str(now.hour)
	if now.hour<10:
		h='0'+str(now.hour)
	mi=str(now.minute)
	if now.minute<10:
		mi='0'+str(now.minute)
	s=str(now.second)
	if now.second<10:
		s='0'+str(now.second)
	curr=str(now.year)+m+d+h+mi+s
	m=str(date[1])
	if date[1]<10:
		m='0'+str(date[1])
	d=str(date[0])
	if date[0]<10:
		d='0'+str(date[0])
	h=str(time[0])
	if time[0]<10:
		h='0'+str(time[0])
	mi=str(time[1])
	if time[1]<10:
		mi='0'+str(time[1])
	s=str(time[2])
	if time[2]<10:
		s='0'+str(time[2])
	exp=str(date[2])+m+d+h+mi+s
	if exp > curr:
		return False
	return True


print(check_expiry('Sun, 01-Jul-2020 21:29:29 GMT'))