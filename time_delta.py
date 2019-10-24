#!/usr/bin/env python3.6

# Developed by forest-man
# https://github.com/forest-man

import os
import sys
import argparse
import datetime
import numpy as np
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

lst = []

def time_convert(d):
	if d > 0:
		lst.append(str(datetime.timedelta(seconds=d)))
	else:
		try:
			lst.append('-' + str(datetime.timedelta(seconds=abs(d))))
		except ValueError:
			pass
def time_calc(past, cur):
	date1 = pd.to_datetime(pd.Series(cur))
	date2 = pd.to_datetime(pd.Series(past))
	df = pd.DataFrame(dict(PAST = date2, CUR = date1))
	df1 = pd.DataFrame(dict(PAST_C = date2, CUR_C = date1))
	df1[p] = df['PAST'].dt.strftime('%H:%M:%S.%f')
	df1[c] = df['CUR'].dt.strftime('%H:%M:%S.%f')
	df['diff_seconds'] = df['CUR'] - df['PAST']
	df['diff_seconds'] = df['diff_seconds']/np.timedelta64(1,'s')
	for i in df['diff_seconds']:
		time_convert(i)
	df_t = pd.DataFrame(dict(TimeDelta = lst))
	df3 = df1.merge(df, left_index=True, right_index=True)
	df_f = df_t.merge(df3, left_index=True, right_index=True)
	cols = df_f.columns.tolist()
	cols = [p, c, 'TimeDelta']
	df_f = df_f[cols]
	print(df_f)
	ts = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')
	df_f.to_csv('{}_{}_vs_{}.csv'.format(ts, p, c), sep='|', encoding='utf-8', index=False)
        
def time_gun(p, c):
	time_p = []
	time_c = []
	p=open(p, "r")
	c=open(c, "r")  
	line_p = p.readline()
	line_c = c.readline()   
	cnt = 1
	while line_p:
		past = line_p.strip()
		cur = line_c.strip()    
		time_p.append(past)
		time_c.append(cur)      
		line_p = p.readline()
		line_c = c.readline()
		cnt += 1
	p.close()
	c.close()
	time_calc(time_p, time_c)

def args():
	try:
		global p, c
		p = sys.argv[1]
		c = sys.argv[2]
		time_gun(p, c)
	except (IndexError, IOError):
		print("Usage: ./time_delta.py timestamp_file1 timestamp_file2")

args()

