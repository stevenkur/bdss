from map_match import *
from multiprocessing import cpu_count, Pool



def main_match(traj_input):
	traj_file = traj_input
	out_file = 'hasil_match.csv'
	trajectory = pd.read_csv(traj_file, usecols=['TRAJ_ID','LON','LAT'])
	trajectory = data_convert(trajectory)
	pool = Pool()
	match_results = pool.map(trajectory_matching, trajectory)
	pool.close()
	match_results = pd.concat(match_results, ignore_index=True)
	# timestamp = pd.read_csv(traj_file, usecols=['TIMESTAMP'])
	# match_results["TIMESTAMP"] = pd.Series(timestamp, index=match_results.index)
	match_results.to_csv(r'hasil_match.csv')

if __name__ == "__main__":
	main_match()
	
