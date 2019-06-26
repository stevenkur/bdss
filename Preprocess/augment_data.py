from tempfile import NamedTemporaryFile
import sys
import shutil
import csv
import geopy.distance
import math
import pandas as pd
from more_itertools import unique_everseen

file_ready = 'trajectory_ready.csv'
file_edge_out = 'edge_connect.csv'
file_look = 'lookup_file.csv'
file_output = 'matched_trajectory.csv'
file_edge_ready = 'edge_ready.csv'
file_input = 'hasil_match.csv'
file_edge = 'Edge.csv'
file_traj = 'traj.csv'


def ambil_data():
	fields = ['TRAJ_ID',
	'MATCHED_EDGE', 
	'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT']
	with open(file_input, 'r') as in_file:
		rowses = []
		data = [row for row in csv.reader(in_file)]
		for rows in range(1,len(data)):
			lng = ''
			lat = ''
			trajid = data[rows][1]
			matchedge = data[rows][2]
			edge = matchedge.replace("[","").replace("]","").replace(" ","")
			edge_split = edge.split(',')
			matchnode = data[rows][3]
			node = matchnode.replace("[","").replace("]","").replace(" ","")
			node_split = node.split(',')
			for edges in edge_split:
				# print(edges)
				if(int(edges) == -1):
					break
				reader = pd.read_csv(file_edge,index_col=[1])
				edge_row = reader.loc[int(edges)]
				s_lon = edge_row['s_lng']
				s_lat = edge_row['s_lat']
				e_lon = edge_row['e_lng']
				e_lat = edge_row['e_lat']
				# print(edges, s_lon, e_lat, e_lon , e_lat)
				rowses.append({
					'TRAJ_ID': trajid, 
					'MATCHED_EDGE': edges,
					'MATCHED_EDGE_S_LNG': s_lon,
					'MATCHED_EDGE_S_LAT': s_lat,
					'MATCHED_EDGE_E_LNG': e_lon,
					'MATCHED_EDGE_E_LAT': e_lat
					})
			print(rows,'/',len(data))
		with open(file_output, 'w',newline='') as out_file:
			writer = csv.DictWriter(out_file, fieldnames=fields)
			# writer.writerow(('TRAJ_ID', 'MATCHED_EDGE','s_lng','s_lat','e_lng','e_lat'))
			writer.writerows(rowses)

def merge_data():
	tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')
	fields = ['TRAJ_ID',
	'MATCHED_EDGE', 
	'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
	'TAXI',
	'DATE',
	'DISTANCE',
	'TIMESTAMP'
	]
	outfields = ['TRAJ_ID',
	'EDGE_ID',
	'MATCHED_EDGE', 
	'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
	'TAXI',
	'DATE',
	'DISTANCE',
	'TIMESTAMP'
	]
	with open(file_output,'r',newline='') as csvfile, tempfile:
	    reader = csv.DictReader(csvfile, fieldnames=fields)
	    writer = csv.DictWriter(tempfile, fieldnames=outfields)
	    for row in reader:
	        ######### first time matched
	        trajid = row['TRAJ_ID']
	        with open(file_traj,'r',newline='') as timefile:
	            readtime = csv.DictReader(timefile)
	            for roww in readtime:
	                if (trajid == roww['TRAJ_ID']):
	                    timestamp = roww['TIMESTAMP']
	                    row['TIMESTAMP'] = timestamp
	        partitionkey_split = trajid.split("_")
	        row['TRAJ_ID'] = partitionkey_split[2]+partitionkey_split[3]
	        row['TAXI'] = partitionkey_split[0]
	        row['DATE'] = partitionkey_split[1]
	        edgenya = row['MATCHED_EDGE']
	        taxi = row['TAXI']
	        row['EDGE_ID'] = edgenya+"_"+taxi+"_"+row['DATE']
	        ##################
	        coords_1 = (float(row['MATCHED_EDGE_S_LAT']), float(row['MATCHED_EDGE_S_LNG']))
	        coords_2 = (float(row['MATCHED_EDGE_E_LAT']),float(row['MATCHED_EDGE_E_LNG']))
	        distance = geopy.distance.vincenty(coords_1,coords_2).m
	        row['DISTANCE'] = distance
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
	        'TIMESTAMP': row['TIMESTAMP']
	        }
	        writer.writerow(row)
	shutil.move(tempfile.name, file_output)


def add_header():
	with open(file_look, 'w', newline='') as out_file:
		writer = csv.writer(out_file)
		writer.writerow(['TRAJ_ID',
				'EDGE_ID',
				'MATCHED_EDGE', 
				'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
				'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
				'TAXI',
				'DATE',
				'DISTANCE',
				'TIMESTAMP',
				'TIME_SPENT'])
		with open(file_ready, 'r') as in_file:
			reader = csv.reader(in_file)
			writer.writerows(row[0:] + [0.0] for row in reader)

def time_spent_data():
	tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')
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
	with open(file_ready,'r',newline='') as csvfile, tempfile:
	    reader = csv.DictReader(csvfile, fieldnames=outfields)
	    writer = csv.DictWriter(tempfile, fieldnames=outfields)
	    # reader.next()
	    data = pd.read_csv(file_look,index_col=[0,7,8])
	    for row in reader:
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
	shutil.move(tempfile.name, file_ready)

def cocokin_data_conn():
	fields = [
	'TAXI',
	'DATE_EDGE',
	'EDGE',
	'PREVIOUS',
	'NEXT'
	]
	with open(file_edge_out,'r',newline='') as csvfile, open(file_edge_ready,'w',newline='') as out_file:
	    reader = csv.DictReader(csvfile, fieldnames=fields)
	    for row in reader:
	        out_file.writelines(unique_everseen(csvfile))

def cocokin_data():
	tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')

	fields = ['TRAJ_ID',
	'EDGE_ID'
	'MATCHED_EDGE', 
	'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
	'TAXI',
	'DATE',
	'DISTANCE',
	'TIMESTAMP'
	]
	with open(file_output,'r',newline='') as csvfile, open(file_ready, 'w',newline='') as out_file:
	    reader = csv.DictReader(csvfile, fieldnames=fields)
	    for row in reader:
	        out_file.writelines(unique_everseen(csvfile))


def edge_con_data():

	infields = ['TRAJ_ID',
	'EDGE_ID',
	'MATCHED_EDGE', 
	'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
	'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
	'TAXI',
	'DATE',
	'DISTANCE',
	'TIMESTAMP',
	'TIME_EDGE'
	]
	outfields =[
	'TAXI',
	'DATE_EDGE',
	'EDGE',
	'PREVIOUS',
	'NEXT'
	]
	taxi = 0
	date = 0
	with open(file_ready,'r',newline='') as csvfile, open(file_edge_out,'w',newline='') as outfile:
	    reader = csv.DictReader(csvfile, fieldnames=infields)
	    writer = csv.DictWriter(outfile, fieldnames=outfields)
	    # reader.next()
	    data = pd.read_csv(file_look,index_col=[7,8])
	    for row in reader:
	    	if taxi==0 and date==0:
	    		taxi = row['TAXI']
	    		date = row['DATE']
	    		traj = row['TRAJ_ID']
	    		edge_list = data.loc[int(row['TAXI']),int(row['DATE'])]['MATCHED_EDGE']
	    		# print(edge_list)
	    		edge_each = edge_list.values.tolist()
	    		for edges in range(len(edge_each)):
	    			current_edge = edge_each[edges]
	    			if(edges == 0): 
	    				next_edge = edge_each[edges+1]
	    				previous_edge = 0
	    			elif(edges == len(edge_each)-1):
	    				next_edge = 0
	    				previous_edge = edge_each[edges-1]
	    			else:
	    				next_edge = edge_each[edges+1]
	    				previous_edge = edge_each[edges-1]
	    			row = {
	    			'TAXI': taxi,
	    			'DATE_EDGE': str(taxi)+"_"+str(date)+"_"+str(current_edge)+"_"+str(previous_edge)+"_"+str(next_edge),
	    			'EDGE': current_edge,
	    			'PREVIOUS': previous_edge,
	    			'NEXT': next_edge
	    			}
	    			writer.writerow(row)
	    	elif taxi!=row['TAXI'] or date!=row['DATE']:
	    		taxi = row['TAXI']
	    		date = row['DATE']
	    		traj = row['TRAJ_ID']
	    		edge_list = data.loc[int(row['TAXI']),int(row['DATE'])]['MATCHED_EDGE']
	    		# print(edge_list)
	    		edge_each = edge_list.values.tolist()
	    		for edges in range(len(edge_each)):
	    			current_edge = edge_each[edges]
	    			if(edges == 0): 
	    				next_edge = edge_each[edges+1]
	    				previous_edge = 0
	    			elif(edges == len(edge_each)-1):
	    				next_edge = 0
	    				previous_edge = edge_each[edges-1]
	    			else:
	    				next_edge = edge_each[edges+1]
	    				previous_edge = edge_each[edges-1]
	    			row = {
	    			'TAXI': taxi,
	    			'DATE_EDGE': str(taxi)+"_"+str(date)+"_"+str(current_edge)+"_"+str(previous_edge)+"_"+str(next_edge),
	    			'EDGE': current_edge,
	    			'PREVIOUS': previous_edge,
	    			'NEXT': next_edge
	    			}
	    			writer.writerow(row)



