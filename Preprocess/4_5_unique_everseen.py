from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from tempfile import NamedTemporaryFile
import shutil
import csv
from more_itertools import unique_everseen


filename = 'matched_trajectory_backup latest.csv'
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

with open(filename,'r',newline='') as csvfile, open('222.csv','w',newline='') as out_file:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    for row in reader:
        out_file.writelines(unique_everseen(csvfile))







