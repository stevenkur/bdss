from tempfile import NamedTemporaryFile
import shutil
import csv
import geopy.distance
count= 0
update = 0

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
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        ######### first time matched
        trajid = row['TRAJ_ID']
        with open('traj2.csv','r',newline='') as timefile:
            readtime = csv.DictReader(timefile)
            for roww in readtime:
                if (trajid == roww['TRAJ_ID']):
                    timestamp = roww['TIMESTAMP']
                    row['TIMESTAMP'] = timestamp
        partitionkey_split = trajid.split("_")
        row['TRAJ_ID'] = partitionkey_split[2]+partitionkey_split[3]
        row['TAXI'] = partitionkey_split[0]
        row['DATE'] = partitionkey_split[1]
        ##################
        coords_1 = (float(row['MATCHED_EDGE_S_LAT']), float(row['MATCHED_EDGE_S_LNG']))
        coords_2 = (float(row['MATCHED_EDGE_E_LAT']),float(row['MATCHED_EDGE_E_LNG']))
        distance = geopy.distance.vincenty(coords_1,coords_2).m
        row['DISTANCE'] = distance
        row = {
        'TRAJ_ID': row['TRAJ_ID'], 
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
    	
shutil.move(tempfile.name, filename)