from tempfile import NamedTemporaryFile
import shutil
import csv
count= 0
update = 0

filename = 'matched_trajectory.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['TRAJ_ID','TIMESTAMP','LON', 'LAT', 'TAXI', 'DATE']

with open(filename, 'r',newline='') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        # print('updating row', row['TRAJ_ID'])
        taxiid = row['TRAJ_ID']
        datetime = row['TIMESTAMP']
        partitionkey = datetime.replace("-","")
        partitionkey_split = partitionkey.split(" ")
        splitkey = partitionkey_split[1].split(":")
        quarter = int(splitkey[1])//15
        trajid = splitkey[0]+'_'+str(quarter)
        # trajid = taxiid+splitkey[0]
        # split = datetime.split(" ")
        # date = split[0]
        # times = split[1].split(":")
        # hour = times[0]
    	
        row['TRAJ_ID'] = trajid
        row['TAXI'] = taxiid
        row['DATE'] = partitionkey_split[0]
        count += 1
        row = {
        'TRAJ_ID': row['TRAJ_ID'], 
        'TIMESTAMP': row['TIMESTAMP'], 
        'LON': row['LON'], 
        'LAT': row['LAT'],
        'TAXI': row['TAXI'],
        'DATE': row['DATE']}
        writer.writerow(row)
    	

shutil.move(tempfile.name, filename)