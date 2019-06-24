from map_match import *
from multiprocessing import cpu_count, Pool


def main():
	trajectory = pd.read_csv('traj2.csv', usecols=['TRAJ_ID','LON','LAT'])
	trajectory = data_convert(trajectory)
	pool = Pool()
	match_results = pool.map(trajectory_matching, trajectory)
	pool.close()
	match_results = pd.concat(match_results, ignore_index=True)

	match_results.to_csv(r'hasil_match.csv')

if __name__ == "__main__":
	main()
	
