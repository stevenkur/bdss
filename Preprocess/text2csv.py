import csv

with open('2.csv', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('traj2.csv', 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('TRAJ_ID','TIMESTAMP','LON', 'LAT','TAXI','DATE'))
        writer.writerows(lines)