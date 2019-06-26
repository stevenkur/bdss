import csv

combined_file = 'combined.csv'
traj_folder = './raw_traj/'
with open(combined_file,'w',newline='') as out_file:
	for num in range(1,16):
		with open(traj_folder+str(num)+'.txt','r',newline='') as input_file: 
		    for line in input_file:
		         out_file.write(line)