from tempfile import NamedTemporaryFile
import sys
import shutil
import csv
import geopy.distance
import math
import pandas as pd
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from more_itertools import unique_everseen

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)


fields = ['TRAJ_ID',
'MATCHED_EDGE', 
# 'MATCHED_NODE',
'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT']
# 'MATCHED_NODE_LNG', 'MATCHED_NODE_LAT']
file_input = '222.csv'
file_edge = 'Edge.csv'
file_traj = 'traj.csv'
file_output = 'edge_connect.csv'




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
	with open(file_input,'r',newline='') as csvfile, open(file_output,'w',newline='') as outfile:
	    reader = csv.DictReader(csvfile, fieldnames=infields)
	    writer = csv.DictWriter(outfile, fieldnames=outfields)
	    next(reader)
	    data = pd.read_csv('222_see.csv',index_col=[7,8])
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
	    			# entity = Entity()
	    			# entity.PartitionKey = str(taxi)
	    			# entity.RowKey = str(date) + "_" +str(traj)+ "_" + str(current_edge)
	    			# entity.Edge_id = str(current_edge)
	    			# entity.Previous = str(previous_edge)
	    			# entity.Next = str(next_edge)
	    			# table_service.insert_entity('ConTrajectory', entity)
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
	    			# entity = Entity()
	    			# entity.PartitionKey = str(taxi)
	    			# entity.RowKey = str(date) + "_" +str(traj)+ "_" + str(current_edge)
	    			# entity.Edge_id = str(current_edge)
	    			# entity.Previous = str(previous_edge)
	    			# entity.Next = str(next_edge)
	    			# table_service.insert_entity('ConTrajectory', entity)

	        ######### first time matched
	        # trajid = row['TRAJ_ID']
	        # with open(file_traj,'r',newline='') as timefile:
	        #     readtime = csv.DictReader(timefile)
	        #     for roww in readtime:
	        #         if (trajid == roww['TRAJ_ID']):
	        #             timestamp = roww['TIMESTAMP']
	        #             row['TIMESTAMP'] = timestamp
	        # partitionkey_split = trajid.split("_")
	        # row['TRAJ_ID'] = partitionkey_split[2]+partitionkey_split[3]
	        # row['TAXI'] = partitionkey_split[0]
	        # row['DATE'] = partitionkey_split[1]
	        # edgenya = row['MATCHED_EDGE']
	        # taxi = row['TAXI']
	        # row['EDGE_ID'] = edgenya+"_"+taxi
	        ##################
	        # coords_1 = (float(row['MATCHED_EDGE_S_LAT']), float(row['MATCHED_EDGE_S_LNG']))
	        # coords_2 = (float(row['MATCHED_EDGE_E_LAT']),float(row['MATCHED_EDGE_E_LNG']))
	        # distance = geopy.distance.vincenty(coords_1,coords_2).m
	        # row['DISTANCE'] = distance
	        
		        # writer.writerow(row)
	        
	#         total = total_distance.sum()
	#         time_spent = round(15*(float(row['DISTANCE'])/total),3)
	#         row['TIME_EDGE'] = time_spent
	#         row = {
	#         'TRAJ_ID': row['TRAJ_ID'],
	#         'EDGE_ID' : row['EDGE_ID'], 
	#         'MATCHED_EDGE': row['MATCHED_EDGE'], 
	#         'MATCHED_EDGE_S_LNG': row['MATCHED_EDGE_S_LNG'] , 
	#         'MATCHED_EDGE_S_LAT': row['MATCHED_EDGE_S_LAT'] ,
	#         'MATCHED_EDGE_E_LNG': row['MATCHED_EDGE_E_LNG'], 
	#         'MATCHED_EDGE_E_LAT':row['MATCHED_EDGE_E_LAT'] ,
	#         'TAXI': row['TAXI'],
	#         'DATE': row['DATE'],
	#         'DISTANCE': row['DISTANCE'],
	#         'TIMESTAMP': row['TIMESTAMP'],
	#         'TIME_EDGE': row['TIME_EDGE']
	#         }
	#         writer.writerow(row)
	# shutil.move(tempfile.name, file_output)
merge_data()