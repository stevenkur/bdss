from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from tempfile import NamedTemporaryFile
import shutil
import csv
from more_itertools import unique_everseen

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)


filename = 'matched_trajectory.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')

fields = ['TAXI',
'EDGE_ID'
'CUR_EDGE', 
'PREVIOUS',
'NEXT'
]

with open('edge_connect.csv','r',newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    # writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        entity = Entity()
        entity.PartitionKey = row['TAXI']
        entity.RowKey = row['EDGE_ID']
        entity.Edge_id = row['CUR_EDGE']
        entity.Previous_edge = row['PREVIOUS']
        entity.Next_edge = row['NEXT']
        table_service.insert_entity('ConTrajectory', entity)







