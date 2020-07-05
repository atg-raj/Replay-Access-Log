import sys
import numpy
import pandas as pd
import argparse
import re
from datetime import datetime,timedelta
import fnmatch
import os

def parser(log_file):
	parser = argparse.ArgumentParser()
	parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'))
	parts = [
		r'(?P<host>\S+)',                   # host %h
		r'\S+',                             # indent %l (unused)
		r'(?P<user>\S+)',                   # user %u
		r'\[(?P<time>.+)\]',                # time %t
		r'"(?P<request>.*)"',               # request "%r"
		r'(?P<status>[0-9]+)',              # status %>s
		r'(?P<size>\S+)',                   # size %b (careful, can be '-')
		r'"(?P<referrer>.*)"',              # referrer "%{Referer}i"
		r'"(?P<useragent>.*)"',                 # user agent "%{User-agent}i"
		r'\S+',                             # indent %l (unused)
	]
	pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
	args = parser.parse_args()
	log_data = []

	for line in args.log_file:
		k = pattern.match(line)
		if k is not None:
			log_data.append(pattern.match(line).groupdict())

	return log_data

def get_All_Attributes(log_data, log_file):
	web_access_log_df = pd.DataFrame(columns=['host','user','time','request','request_type','url','http_version','status','size','referrer','useragent','epoch_time'])
	columns = ['host','port','user','time','request','request_type','url','http_version','status','size','referrer','useragent','epoch_time']
	full_data = []
	portn = 3000
	i=1
	Dict = {}
	for data in log_data:
		request = data['request']
		k = request.split()
		#print(len(k))
		if len(k) > 0:
			data['request_type'] = k[0] 
		if len(k) > 1:
			data['url'] = k[1]
		if len(k) > 2:
			data['http_version'] = k[2]
		s = data['time']
		# ss=data['host'].replace('.','')
		# #print(Dict.get(ss))
		if Dict.get(data['host']) == None:
			data['port'] = portn
			Dict[data['host']] = portn
			# print(Dict.get(data['host']))
			# print(Dict[data['host']],ss)
			portn = portn+1
		else:
			# print(Dict[data['host']],ss)
			data['port'] = Dict[data['host']]
		epoch = datetime.strptime(s[:20], '%d/%b/%Y:%H:%M:%S') + timedelta(hours=int(s[21:23]), minutes=int(s[24:])) * (-1 if s[20] == '+' else 1) 
		epoch = epoch.strftime('%s')
		epoch = int(epoch)
		
		if i==1:
			ii=epoch
			i=i+1

		data['epoch_time']=epoch-ii
		full_data.append(data)

	web_access_log_df = pd.DataFrame(full_data)
	web_access_log_df = web_access_log_df.reindex(columns=columns)
	#web_access_log_df.columns = columns
#		web_access_log_df = web_access_log_df.append(data, ignore_index=True)
	web_access_log_df.to_csv(log_file+'.csv')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('please provide a log file name in the dir as argument')
	log_file = sys.argv[1]
	print('starting to parse the log file %s' % (log_file))
	log_data = parser(log_file)
	get_All_Attributes(log_data, log_file)
	print('parsing for file %s is done' % (log_file))
