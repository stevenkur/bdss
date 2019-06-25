from map_match import *
from multiprocessing import cpu_count, Pool

traj_file = 'traj.csv'
out_file = 'hasil_match.csv'
def main():
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
	main()
	
