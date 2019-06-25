from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from tempfile import NamedTemporaryFile
import shutil
import csv
from more_itertools import unique_everseen


filename = 'edge_connect.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')

fields = [
'TAXI',
'DATE_EDGE',
'EDGE',
'PREVIOUS',
'NEXT'
]

with open(filename,'r',newline='') as csvfile, open('111.csv','w',newline='') as out_file:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    for row in reader:
        out_file.writelines(unique_everseen(csvfile))







