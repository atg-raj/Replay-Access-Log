import sys
import csv
import requests 
import time

def func(logfile):
	with open(logfile,'r') as csvfile:
		reader = csv.DictReader(csvfile)
		#ii=time.perf_counter()
		ii=0
		for row in reader:
			url='http://127.0.0.1'+ row['url']
			timer=int(row['epoch_time'])
			time.sleep(timer-ii)
			ii=timer
			r = requests.get(url)
			print(r)
			#print(r.content) 
			print(len(r.content))
			cip=row['host']

			# print(url,cip,time)

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print (__doc__)
        sys.exit(1)
    infile_name = sys.argv[1]
    func(infile_name)






# import sys
# import csv
# import requests 
# import time

# def func(logfile):
# 	with open(logfile,'r') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 		ii=time.perf_counter()
# 		for row in reader:
# 			url='http://127.0.0.1'+ row['url']
# 			timer=int(row['epoch_time'])+ii
# 			while(time.perf_counter()<timer):
# 			 	i=0
# 			r = requests.get(url)
# 			print(r)
# 			#print(r.content) 
# 			print(len(r.content))
# 			cip=row['host']

# 			# print(url,cip,time)

# if __name__ == "__main__":
#     if not len(sys.argv) > 1:
#         print (__doc__)
#         sys.exit(1)
#     infile_name = sys.argv[1]
#     func(infile_name)





# python 2
# import sys
# import csv
# import requests 
# import time

# def func(logfile):
# 	with open(logfile,'r') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 		ii=time.clock()
# 		for row in reader:
# 			url='http://127.0.0.1'+ row['url']
# 			timer=int(row['epoch_time'])+ii
# 			while(time.clock()<timer):
# 			 	i=0
# 			r = requests.get(url)
# 			print(r)
# 			#print(r.content) 
# 			print(len(r.content))
# 			cip=row['host']

# 			# print(url,cip,time)

# if __name__ == "__main__":
#     if not len(sys.argv) > 1:
#         print (__doc__)
#         sys.exit(1)
#     infile_name = sys.argv[1]
#     func(infile_name)
