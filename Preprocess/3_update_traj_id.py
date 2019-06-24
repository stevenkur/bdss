from tempfile import NamedTemporaryFile
import shutil
import csv
count= 0
update = 0

filename = '2.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['TRAJ_ID','TIMESTAMP','LON', 'LAT']

with open(filename, 'r',newline='') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        print('updating row', row['TRAJ_ID'])
        taxiid = row['TRAJ_ID']
        datetime = row['TIMESTAMP']
        partitionkey = datetime.replace("-","").replace(" ","")
        splitkey = partitionkey.split(":")
        trajid = taxiid+splitkey[0]
        split = datetime.split(" ")
        date = split[0]
        times = split[1].split(":")
        hour = times[0]
    	
        row['TRAJ_ID'] = trajid
        count += 1
        row = {'TRAJ_ID': row['TRAJ_ID'], 'TIMESTAMP': row['TIMESTAMP'], 'LON': row['LON'], 'LAT': row['LAT']}
        writer.writerow(row)
    	

shutil.move(tempfile.name, filename)