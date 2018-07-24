from hyper import HTTPConnection
import re

def average(array):
	avg=0
	for i in array:
		avg+=i
	avg/=len(array)
	return round(avg,2)

def variance(array):
	avg=average(array)
	var=0
	for i in array:
		var+=(i-avg)**2
	var/=len(array)
	return round(var,2)

re_temp=r'<li class="sky skyid.*?">.*?<h1>(\d+).*?<span>(\d+).*?(\d+)'
server='www.weather.com.cn:80'
url='/weather/101010100.shtml'
highest=[]
lowest=[]
avg_highest=0
avg_lowest=0
var_highest=0
var_lowest=0

print("Connecting to",server)
conn=HTTPConnection(server)
conn.request('GET',url)
resp=conn.get_response()
print("Checking if the response is valid")
if resp.status != 200:
	print("Failed to fetch temperatures from server")
	quit()
content=resp.read().decode('utf-8')
print("Now finding the temperature from the page")
result=re.findall(re_temp,content,re.S)
print("Printing the temperature")

print("Today: highest="+result[0][1]+", lowest="+result[0][2])
highest.append(int(result[0][1]))
lowest.append(int(result[0][2]))
for elem in result[1:]:
	print("Day",elem[0]+": highest="+elem[1]+", lowest="+elem[2])
	highest.append(int(elem[1]))
	lowest.append(int(elem[2]))

avg_highest=average(highest)
avg_lowest=average(lowest)

var_highest=variance(highest)
var_lowest=variance(lowest)

print("Average: highest="+str(avg_highest)+", lowest="+str(avg_lowest))
print("Variance: highest="+str(var_highest)+", lowest="+str(var_lowest))
