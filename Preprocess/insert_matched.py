from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from tempfile import NamedTemporaryFile
import shutil
import csv
from more_itertools import unique_everseen

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)


filename = 'trajectory_ready.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')

fields = ['TRAJ_ID',
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

seen = set() # set for fast O(1) amortized lookup
with open(filename,'r',newline='') as csvfile, open('223.csv','w') as out_file:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    # writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        out_file.writelines(unique_everseen(csvfile))
        
#         writer.writerow(row)
    	
# shutil.move(tempfile.name, filename)

with open('223.csv','r',newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    # writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        entity = Entity()
        entity.PartitionKey = row['TRAJ_ID']
        entity.RowKey = row['EDGE_ID']
        entity.Edge_id = row['MATCHED_EDGE']
        entity.S_long = row['MATCHED_EDGE_S_LNG']
        entity.S_lat = row['MATCHED_EDGE_S_LAT']
        entity.E_long = row['MATCHED_EDGE_E_LNG']
        entity.E_lat = row['MATCHED_EDGE_E_LAT']
        entity.Taxi_id = row['TAXI']
        entity.Date = row['DATE']
        entity.Distance = row['DISTANCE']
        entity.Time_spent = row['TIME_SPENT']
        table_service.insert_entity('STTrajectory', entity)







