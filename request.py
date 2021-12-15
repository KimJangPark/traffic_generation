import requests
import sys

elapsed_time_total = 0
img_links = sys.argv[1]
file = open(img_links, 'r')
NUM_FILES = 40

for i in range (NUM_FILES):
	l = file.readline()
	print(l)
	r = requests.get("http://127.0.0.1:5000/?input_URI=%s"%l)
	roundtrip = r.elapsed.total_seconds()
	print()
	print("Result : " + str(r.json()))
	print("Round Trip Time : "+str(roundtrip))
	print()
	elapsed_time_total += roundtrip

print("total_seconds: ", elapsed_time_total)
print("average_rtt: ", elapsed_time_total/NUM_FILES)
