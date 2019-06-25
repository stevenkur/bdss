from tempfile import NamedTemporaryFile
import sys
import shutil
import csv
import geopy.distance
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
file_output = 'matched_trajectory.csv'

def ambil_data():
	# input_file = file_input
	# edge_file = file_edge
	# output_file = file_output
	with open(file_input, 'r') as in_file:
		rowses = []
		data = [row for row in csv.reader(in_file)]
		# reader = pd.read_csv('Edge.csv',index_col=[1])
		# print(reader.loc[1]['s_lng'])
		# print(reader.loc['1'])
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
					# 'MATCHED_NODE': node_split,
					'MATCHED_EDGE_S_LNG': s_lon,
					'MATCHED_EDGE_S_LAT': s_lat,
					'MATCHED_EDGE_E_LNG': e_lon,
					'MATCHED_EDGE_E_LAT': e_lat
					# 'MATCHED_NODE_LNG': lng,
					# 'MATCHED_NODE_LAT': lat
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
	    # next(reader)
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

def main():
	ambil_data()
	merge_data()


if __name__ == "__main__":
	main()



		