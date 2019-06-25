from tempfile import NamedTemporaryFile
import sys
import shutil
import csv
import geopy.distance
import math
import pandas as pd


fields = ['TRAJ_ID',
'MATCHED_EDGE', 
# 'MATCHED_NODE',
'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT']
# 'MATCHED_NODE_LNG', 'MATCHED_NODE_LAT']
file_input = 'hasil_match.csv'
file_edge = 'Edge.csv'
file_traj = 'traj.csv'
file_output = '222.csv'




def merge_data():

	tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')
	# fields = ['TRAJ_ID',
	# 'MATCHED_EDGE', 
	# 'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	# 'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
	# 'TAXI',
	# 'DATE',
	# 'DISTANCE',
	# 'TIMESTAMP'
	# ]
	outfields = ['TRAJ_ID',
	'EDGE_ID',
	'MATCHED_EDGE', 
	'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
	'TAXI',
	'DATE',
	'DISTANCE',
	'TIMESTAMP',
	'TIME_SPENT'
	]
	with open(file_output,'r',newline='') as csvfile, tempfile:
	    reader = csv.DictReader(csvfile, fieldnames=outfields)
	    writer = csv.DictWriter(tempfile, fieldnames=outfields)
	    next(reader)
	    data = pd.read_csv('matched_trajectory_backup latest.csv',index_col=[0,7,8])
	    for row in reader:
	        ######### first time matched
	        # trajid = row['TRAJ_ID']
	        # partitionkey_split = trajid.split("_")
	        # row['TRAJ_ID'] = partitionkey_split[2]+partitionkey_split[3]
	        # row['TAXI'] = partitionkey_split[0]
	        # row['DATE'] = partitionkey_split[1]
	        # edgenya = row['MATCHED_EDGE']
	        # taxi = row['TAXI']
	        # row['EDGE_ID'] = edgenya+"_"+taxi + "_" + row['DATE']
	        ##################
	        # coords_1 = (float(row['MATCHED_EDGE_S_LAT']), float(row['MATCHED_EDGE_S_LNG']))
	        # coords_2 = (float(row['MATCHED_EDGE_E_LAT']),float(row['MATCHED_EDGE_E_LNG']))
	        # distance = geopy.distance.vincenty(coords_1,coords_2).m
	        # row['DISTANCE'] = distance

	        ###########################
	        total_distance = data.loc[int(row['TRAJ_ID']),int(row['TAXI']),int(row['DATE'])]['DISTANCE']
	        total = total_distance.sum()
	        time_spent = round(15*(float(row['DISTANCE'])/total),3)
	        # print(time_spent)
	        row['TIME_SPENT'] = time_spent
	        row = {
	        'TRAJ_ID': row['TRAJ_ID'],
	        'EDGE_ID' : row['EDGE_ID'], 
	        'MATCHED_EDGE': row['MATCHED_EDGE'], 
	        'MATCHED_EDGE_S_LNG': row['MATCHED_EDGE_S_LNG'] , 
	        'MATCHED_EDGE_S_LAT': row['MATCHED_EDGE_S_LAT'] ,
	        'MATCHED_EDGE_E_LNG': row['MATCHED_EDGE_E_LNG'], 
	        'MATCHED_EDGE_E_LAT':row['MATCHED_EDGE_E_LAT'] ,
	        'TAXI': row['TAXI'],
	        'DATE': row['DATE'],
	        'DISTANCE': row['DISTANCE'],
	        'TIMESTAMP': row['TIMESTAMP'],
	        'TIME_SPENT': row['TIME_SPENT']
	        }
	        writer.writerow(row)
	        ##########################################
	shutil.move(tempfile.name, file_output)
merge_data()