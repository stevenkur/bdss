from tempfile import NamedTemporaryFile
import sys
import shutil
import csv
import pandas as pd


fields = ['_','edge',
's_node',
'e_node', 
's_lng', 's_lat',
'e_lng', 'e_lat'
]
out_fields =[
'edge',
'edge_neighbour'
]
file_input = 'Edge.csv'
# file_edge = 'Edge.csv'
file_output = 'edge_neighbour.csv'

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
            edgeid = data[rows][1]
            startedge = data[rows][2]
            endedge = data[rows][3]
            for edges in range(1,len(data)):
                # print(edges)
                if(startedge == data[edges][2]):
                    rowses.append({
                    'edge': edgeid, 
                    'edge_neighbour': data[edges][1],
                    })
                if(endedge == data[edges][2]):
                    rowses.append({
                    'edge': edgeid, 
                    'edge_neighbour': data[edges][1],
                    })
            print(rows,'/',len(data))
        with open(file_output, 'w',newline='') as out_file:
            writer = csv.DictWriter(out_file, fieldnames=out_fields)
            # writer.writerow(('TRAJ_ID', 'MATCHED_EDGE','s_lng','s_lat','e_lng','e_lat'))
            writer.writerows(rowses)
ambil_data()
    #       for row in reader:
    #           if(row['edge'] == edges):
    #               s_lon = row['s_lng']
    #               s_lat = row['s_lat']
    #               e_lon = row['e_lng']
    #               e_lat = row['e_lat']
    #               rowses.append({
    #               'TRAJ_ID': trajid, 
    #               'MATCHED_EDGE': edges,
    #               # 'MATCHED_NODE': node_split,
    #               'MATCHED_EDGE_S_LNG': s_lon,
    #               'MATCHED_EDGE_S_LAT': s_lat,
    #               'MATCHED_EDGE_E_LNG': e_lon,
    #               'MATCHED_EDGE_E_LAT': e_lat
    #               # 'MATCHED_NODE_LNG': lng,
    #               # 'MATCHED_NODE_LAT': lat
    #               })
    #               print(s_lon,s_lat)

    # with open('finalized.csv','w',newline='') as out_file:
    #   writer = csv.DictWriter(out_file, fieldnames=fields)
    #   writer.writerows(rowses)




                    # writer.writerow(row)
#             writer = csv.DictWriter(tempfile, fieldnames=out_fields)
#             readtime = csv.DictReader(timefile)
#             for roww in readtime:
        # edge_start = row['s_node']
        # reader_edge = pd.read_csv(filename,index_col=[2])
        # edge_n = reader_edge.loc[int(edge_start)]
        # print(edge_n['edge'])
        # for val in range(len(edge_n)):
        #         out_edge = edge_n['edge'].values[val]
        #         print(out_edge)
#         with open(out_file,'r',newline='') as timefile:
#             writer = csv.DictWriter(tempfile, fieldnames=out_fields)
#             readtime = csv.DictReader(timefile)
#             for roww in readtime:
#                 if (trajid == roww['TRAJ_ID']):
#                     timestamp = roww['TIMESTAMP']
#                     row['TIMESTAMP'] = timestamp
#         partitionkey_split = trajid.split("_")
#         row['TRAJ_ID'] = partitionkey_split[2]+partitionkey_split[3]
#         row['TAXI'] = partitionkey_split[0]
#         row['DATE'] = partitionkey_split[1]
#         ##################
#         coords_1 = (float(row['MATCHED_EDGE_S_LAT']), float(row['MATCHED_EDGE_S_LNG']))
#         coords_2 = (float(row['MATCHED_EDGE_E_LAT']),float(row['MATCHED_EDGE_E_LNG']))
#         distance = geopy.distance.vincenty(coords_1,coords_2).m
#         row['DISTANCE'] = distance
#         row = {
#         'TRAJ_ID': row['TRAJ_ID'], 
#         'MATCHED_EDGE': row['MATCHED_EDGE'], 
#         'MATCHED_EDGE_S_LNG': row['MATCHED_EDGE_S_LNG'] , 
#         'MATCHED_EDGE_S_LAT': row['MATCHED_EDGE_S_LAT'] ,
#         'MATCHED_EDGE_E_LNG': row['MATCHED_EDGE_E_LNG'], 
#         'MATCHED_EDGE_E_LAT':row['MATCHED_EDGE_E_LAT'] ,
#         'TAXI': row['TAXI'],
#         'DATE': row['DATE'],
#         'DISTANCE': row['DISTANCE'],
#         'TIMESTAMP': row['TIMESTAMP']
#         }
#         writer.writerow(row)
    	
# shutil.move(tempfile.name, filename)