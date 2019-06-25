from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from tempfile import NamedTemporaryFile
import shutil
import csv
import geopy.distance

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)


filename = 'matched_trajectory.csv'
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

with open(filename,'r',newline='') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    # writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        # ######### first time matched
        # trajid = row['TRAJ_ID']
        # with open('traj2.csv','r',newline='') as timefile:
        #     readtime = csv.DictReader(timefile)
        #     for roww in readtime:
        #         if (trajid == roww['TRAJ_ID']):
        #             timestamp = roww['TIMESTAMP']
        #             row['TIMESTAMP'] = timestamp
        # partitionkey_split = trajid.split("_")
        # row['TRAJ_ID'] = partitionkey_split[2]+partitionkey_split[3]
        # row['TAXI'] = partitionkey_split[0]
        # row['DATE'] = partitionkey_split[1]
        # ##################
        # coords_1 = (float(row['MATCHED_EDGE_S_LAT']), float(row['MATCHED_EDGE_S_LNG']))
        # coords_2 = (float(row['MATCHED_EDGE_E_LAT']),float(row['MATCHED_EDGE_E_LNG']))
        # distance = geopy.distance.vincenty(coords_1,coords_2).m
        # row['DISTANCE'] = distance
        # row = {
        # 'TRAJ_ID': row['TRAJ_ID'], 
        # 'MATCHED_EDGE': row['MATCHED_EDGE'], 
        # 'MATCHED_EDGE_S_LNG': row['MATCHED_EDGE_S_LNG'] , 
        # 'MATCHED_EDGE_S_LAT': row['MATCHED_EDGE_S_LAT'] ,
        # 'MATCHED_EDGE_E_LNG': row['MATCHED_EDGE_E_LNG'], 
        # 'MATCHED_EDGE_E_LAT':row['MATCHED_EDGE_E_LAT'] ,
        # 'TAXI': row['TAXI'],
        # 'DATE': row['DATE'],
        # 'DISTANCE': row['DISTANCE'],
        # 'TIMESTAMP': row['TIMESTAMP']
        # }
        entity = Entity()
		entity.PartitionKey = row['TRAJ_ID']
		entity.RowKey = row['MATCHED_EDGE']
		entity.s_long = row['MATCHED_EDGE_S_LNG']
		entity.s_lat = row['MATCHED_EDGE_S_LAT']
		entity.e_long = row['MATCHED_EDGE_E_LNG']
		entity.e_lat = row['MATCHED_EDGE_E_LAT']
		entity.taxi_id = row['TAXI']
		entity.date = row['DATE']
		entity.distance = row['DISTANCE']
		table_service.insert_entity('dataset', entity)
#         writer.writerow(row)
    	
# shutil.move(tempfile.name, filename)










