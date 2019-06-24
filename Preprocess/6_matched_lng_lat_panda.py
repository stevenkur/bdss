from tempfile import NamedTemporaryFile
import sys
import shutil
import csv
import pandas as pd


fields = ['TRAJ_ID',
'MATCHED_EDGE', 
# 'MATCHED_NODE',
'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT']
# 'MATCHED_NODE_LNG', 'MATCHED_NODE_LAT']
file_input = 'hasil_match.csv'
file_edge = 'Edge.csv'
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
			writer.writerow('TRAJ_ID', 'MATCHED_EDGE','s_lng','s_lat','e_lng','e_lat')
			writer.writerows(rowses)
ambil_data()
	# 		for row in reader:
	# 			if(row['edge'] == edges):
	# 				s_lon = row['s_lng']
	# 				s_lat = row['s_lat']
	# 				e_lon = row['e_lng']
	# 				e_lat = row['e_lat']
	# 				rowses.append({
	# 				'TRAJ_ID': trajid, 
	# 				'MATCHED_EDGE': edges,
	# 				# 'MATCHED_NODE': node_split,
	# 				'MATCHED_EDGE_S_LNG': s_lon,
	# 				'MATCHED_EDGE_S_LAT': s_lat,
	# 				'MATCHED_EDGE_E_LNG': e_lon,
	# 				'MATCHED_EDGE_E_LAT': e_lat
	# 				# 'MATCHED_NODE_LNG': lng,
	# 				# 'MATCHED_NODE_LAT': lat
	# 				})
	# 				print(s_lon,s_lat)

	# with open('finalized.csv','w',newline='') as out_file:
	# 	writer = csv.DictWriter(out_file, fieldnames=fields)
	# 	writer.writerows(rowses)



		