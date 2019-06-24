from tempfile import NamedTemporaryFile
import shutil
import csv
import pandas as pd


fields = ['TRAJ_ID',
'MATCHED_EDGE', 
# 'MATCHED_NODE',
'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT']
# 'MATCHED_NODE_LNG', 'MATCHED_NODE_LAT']

with open('hasil_match.csv', 'r') as in_file:
	rowses = []
	data = [row for row in csv.reader(in_file)]
	for rows in range(len(data)):
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
			s_lon = ''
			s_lat = ''
			e_lon = ''
			e_lat = ''
			
			with open('Edge.csv','r') as edge_file:
				reader = csv.DictReader(edge_file)
				for row in reader:
					if(row['edge'] == edges):
						s_lon = row['s_lng']
						s_lat = row['s_lat']
						e_lon = row['e_lng']
						e_lat = row['e_lat']
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
						print(s_lon,s_lat)
	
	with open('finalized.csv','w',newline='') as out_file:
		writer = csv.DictWriter(out_file, fieldnames=fields)
		writer.writerows(rowses)
		# for nodes in node_split:
		# 	with open('Point.csv','r') as node_file:
		# 		reader = csv.DictReader(node_file)
		# 		for row in reader:
		# 			if(row['node'] == nodes):
		# 				lng = row['lng']
		# 				lat = row['lat']
		

# filename = '2.csv'
# tempfile = NamedTemporaryFile(mode='w', delete=False)
# fields = ['TRAJ_ID','TIMESTAMP','LON', 'LAT']

# with open(filename, 'r') as csvfile, tempfile:
#     reader = csv.DictReader(csvfile, fieldnames=fields)
#     writer = csv.DictWriter(tempfile, fieldnames=fields)
#     for row in reader:
#     	print('updating row', row['TRAJ_ID'])
#     	row['TRAJ_ID'] = count
#     	count += 1
#     	row = {'TRAJ_ID': row['TRAJ_ID'], 'TIMESTAMP': row['TIMESTAMP'], 'LON': row['LON'], 'LAT': row['LAT']}
#     	writer.writerow(row)
	# print(matchedge)
	# for rows in csv.reader(in_file): 
	# 	with open('traj2.csv', 'w',newline='') as out_file:
	#         writer = csv.writer(out_file)
	#         writer.writerow(('TRAJ_ID','MATCHED_EDGE','MATCHED_NODE'))
	#         writer.writerows(lines)







# with open('hasil_match.csv', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     print((lines))
#     # with open('traj2.csv', 'w',newline='') as out_file:
#     #     writer = csv.writer(out_file)
#     #     writer.writerow(('TRAJ_ID','MATCHED_EDGE','MATCHED_NODE'))
#     #     writer.writerows(lines)