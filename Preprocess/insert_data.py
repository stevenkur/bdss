from insert_connection import *
from insert_matched import *
import time


# file_input = 'combined.csv'
# file_traj = 'traj.csv'

def main():

    insert_connection()
    insert_trajectory()
    print("inserted")
    
if __name__ == "__main__":
    main()