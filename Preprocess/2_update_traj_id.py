from tempfile import NamedTemporaryFile
import shutil
import csv
count= 0
update = 0

filename = '2.csv'
outname= 'traj2.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

fields = ['TRAJ_ID','TIMESTAMP','LON', 'LAT', 'TAXI', 'DATE']

with open(filename, 'r',newline='') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        # print('updating row', row['TRAJ_ID'])
        taxiid = row['TAXI']
        datetime = row['TIMESTAMP']
        partitionkey = datetime.replace("-","")
        partitionkey_split = partitionkey.split(" ")
        splitkey = partitionkey_split[1].split(":")
        quarter = int(splitkey[1])//15
        if (quarter == 0):
            time = '15' 
        if (quarter == 1):
            time = '30' 
        if (quarter == 2):
            time = '45' 
        if (quarter == 3):
            time = '60' 
        trajid = taxiid +'_'+partitionkey_split[0]+"_"+ splitkey[0]+'_'+time
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

with open(filename, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open(outname, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('TRAJ_ID','TIMESTAMP','LON', 'LAT','TAXI','DATE'))
        writer.writerows(lines)