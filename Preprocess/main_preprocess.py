from prepare_traj_id import *
from map_matching_main import *
from augment_data import *
from insert_connection import *
from inser_matched import *
import time


file_input = 'combined.csv'
file_traj = 'traj.csv'

def main():
	time_detail = []
	start_time_init = time.time()
	
	start_time = time.time()
	prepare_traj(file_input)
	elapsed_time = time.time() - start_time
	print('prepare_traj done in:', elapsed_time)
	time_detail.append(elapsed_time)

	main_match(file_traj)
	elapsed_time = time.time() - start_time
	print('matching done in: ', elapsed_time)
	time_detail.append(elapsed_time)

	start_time = time.time()
	ambil_data()
	elapsed_time = time.time() - start_time
	print('ambil_data done in: ', elapsed_time)
	time_detail.append(elapsed_time)

	start_time = time.time()
	merge_data()
	elapsed_time = time.time() - start_time
	print('merge_data done in: ', elapsed_time)
	time_detail.append(elapsed_time)

	start_time = time.time()
	cocokin_data()
	elapsed_time = time.time() - start_time
	print('cocokin_data done in: ', elapsed_time)
	time_detail.append(elapsed_time)

	start_time = time.time()
	add_header()
	elapsed_time = time.time() - start_time
	print('add_header done in: ', elapsed_time)

	start_time = time.time()
	time_spent_data()
	print('time_spent_data done in: ', elapsed_time)
	time_detail.append(elapsed_time)

	start_time = time.time()
	edge_con_data()
	print('edge_con_data done in: ', elapsed_time)
	time_detail.append(elapsed_time)

	cocokin_data_conn()
	elapsed_time_all = time.time() - start_time_init
	print('finish in: ', elapsed_time_all)
	print(time_detail)

	insert_connection()
	insert_trajectory()
	
if __name__ == "__main__":
	main()