import quiztest as qt
import sys
import sqlite3
import config

nusers = 0
nspawn = 0
tspawn = 0
max_time = 0

def validate_args():
	if len(sys.argv) == 5:
		nusers = (int) (sys.argv[1].split("=")[1])
		nspawn = (int) (sys.argv[2].split("=")[1])
		tspawn = (int) (sys.argv[3].split("=")[1])
		max_time = (int) (sys.argv[4].split("=")[1])

		#args validation
		if nusers > len(config.STUDENTS):
			print "There is not enough usernames"
			sys.exit(0)
		elif nspawn > nusers:
			print "Is not posible to create groups greater than nusers"
			sys.exit(0)

	elif len(sys.argv) == 2 and sys.argv[1] == "--help":
		print '''
HOW TO EXECUTE
----------------
Script needs four parameters which are listed here:

	--nusers: Amount of users to simulate.
	--nspawn: number of users per group launched
	--tspawn: time between two groups launched (seconds)
	--max_time: max time that a user can stay on Quiz (seconds)

For example to simulate 100 users in groups of 20 every 5 seconds limiting his time on Quiz to one minute:

python main.py --nusers=100 --nspwan=20 --tspawn=5 --max_time=60
'''
		sys.exit(0)
	else:
		print '''Incorrect syntax, please type "python main.py --help" to see more options''', 'red'
		sys.exit(0)

	return nusers, nspawn, tspawn, max_time

def main():
	#Validating arguments from terminal
	nusers, nspawn, tspawn, max_time = validate_args()

	#creating database structure
	qt.create_database_structure()

	#launching the test
	qt.executeTestOverQuiz(nusers,nspawn,tspawn, max_time)

if __name__== "__main__":
	main()