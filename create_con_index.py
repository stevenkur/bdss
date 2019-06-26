from tempfile import NamedTemporaryFile
import shutil
import csv

count= 0
update = 0

fields = ['TRAJ_ID',
'EDGE_ID',
'MATCHED_EDGE', 
'MATCHED_EDGE_S_LNG', 'MATCHED_EDGE_S_LAT',
'MATCHED_EDGE_E_LNG', 'MATCHED_EDGE_E_LAT',
'TAXI',
'DATE',
'DISTANCE',
'TIMESTAMP'
]
fields2 = ['EDGE_ID',
'MATCHED_EDGE',
'PREVIOUS', 
'NEXT'
]

taxi_id = 0
date = 0

with open('matched_trajectory.csv','r',newline='') as csvfile, open('con_trajectory.csv','w') as out_file:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(out_file, fieldnames=fields2)
    for row in reader:
        if taxi_id==0 and date==0:
            previous = 0
            taxi_id = row['TAXI']
            date = row['DATE']

            current = row['MATCHED_EDGE']
            row = {
            'EDGE_ID': row['EDGE_ID'], 
            'MATCHED_EDGE': row['MATCHED_EDGE'], 
            'PREVIOUS': previous,
            'NEXT': next(reader)['MATCHED_EDGE']
            }
            previous = current
        elif taxi_id!=row['TAXI'] or date!=row['DATE']:
            previous = 0

            current = row['MATCHED_EDGE']
            row = {
            'EDGE_ID': row['EDGE_ID'], 
            'MATCHED_EDGE': row['MATCHED_EDGE'], 
            'PREVIOUS': previous,
            'NEXT': next(reader)['MATCHED_EDGE']
            }
            previous = current
        else:
            current = row['MATCHED_EDGE']
            row = {
            'EDGE_ID': row['EDGE_ID'], 
            'MATCHED_EDGE': row['MATCHED_EDGE'], 
            'PREVIOUS': previous,
            'NEXT': next(reader)['MATCHED_EDGE']
            }
            previous = current
        print(row)
        #writer.writerow(row)