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

print("Connecting",server+"...",end="",flush=True)
conn=HTTPConnection(server)
conn.request('GET',url)
print("connected",flush=True)
resp=conn.get_response()
print("Checking if the response is valid...",end="",flush=True)
if resp.status != 200:
    print("invalid",flush=True)
    print("OK bye!",flush=True)
    quit()
print("valid",flush=True)

print("Fetching page content...",end="",flush=True)
content=resp.read().decode('utf-8')
print("done",flush=True)

print("Closing connection...",end="",flush=True)
conn.close()
print("done",flush=True)

print("Fetching temperatures from the page...",end="",flush=True)
result=re.findall(re_temp,content,re.S)
print("done",flush=True)

print("Today: highest="+result[0][1]+", lowest="+result[0][2],flush=True)
highest.append(int(result[0][1]))
lowest.append(int(result[0][2]))
for elem in result[1:]:
    print("Day",elem[0]+": highest="+elem[1]+", lowest="+elem[2],flush=True)
    highest.append(int(elem[1]))
    lowest.append(int(elem[2]))

print("Calculating average...",end="",flush=True)
avg_highest=average(highest)
avg_lowest=average(lowest)
print("highest="+str(avg_highest)+", lowest="+str(avg_lowest),flush=True)

print("Calculating variance...",end="",flush=True)
var_highest=variance(highest)
var_lowest=variance(lowest)
print("highest="+str(var_highest)+", lowest="+str(var_lowest),flush=True)
