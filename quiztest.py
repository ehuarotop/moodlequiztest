#moodle admin pass --> iXoh$ng8Aipe
import mechanize as mech
import config
import random
import time
import sqlite3
import multiprocessing

def doQuiz(student):
	#Inititing browser simulatoe
	browser = mech.Browser()
	browser.set_handle_robots(False)
	browser.open(config.MOODLE_SITE_LOGIN_URL)

	#Logging on the moodle site
	login_form = list(browser.forms())[0]
	
	#pointing to the form
	browser.form = login_form
	browser['username'] = student
	browser['password'] = 'S-tudent0'
	browser.submit()

	#Simulating click on 'Site home' link.
	browser.follow_link(text_regex='Site home')

	#Simulating click on course link based on course name.
	browser.follow_link(text_regex=config.COURSE_NAME)

	#Simulating click on Quiz link based on Quiz name
	browser.follow_link(text_regex=config.QUIZ_NAME)

	#Simulating click on "Attempt quiz now"
	browser.select_form(nr=0)
	browser.submit()

	#Simulating student asnwering questions, taking form number 0
	answer_form = list(browser.forms())[0]
	#Declaring nextpage variable for control
	nextpage = str(answer_form['nextpage'])

	#control variable for stopping iteration over question pages.
	have_unanswered_questions = True

	#answering quiz page by page automatically
	while (have_unanswered_questions):
		
		for control in answer_form.controls:
			control_name = str(control.name)
			control_type = str(control.type)

			if "answer" in control_name:
				#only questions with multiple answers controlled.
				if control_type == "radio":
					answer_form[control_name] = [str(random.choice(control.items))]

		#clicking on the next page button or Finish attempt button
		browser.form = answer_form
		browser.submit(name='next', label=str(answer_form['next']))

		#validating if there is more pages with unanswered questions.
		if nextpage == "-1":
			have_unanswered_questions = False
		else:
			answer_form = list(browser.forms())[0]
			nextpage = str(answer_form['nextpage'])


	#Submitting answers
	submit_answer_form = list(browser.forms())[1]
	browser.form = submit_answer_form
	browser.submit()

	#Closing browser object
	browser.close()

def create_database_structure():
	#creating database if not exists
	conn = sqlite3.connect("quiztest.db")

	if conn is not None:
		c = conn.cursor()
		qry = open('create_database_structure.sql', 'r').read()
		c.executescript(qry)
		conn.commit()
	else:
		print("Error!! Cannot connect to the database")


def executeTestOverQuiz(nusers, nspawn, tspawn, max_time):
	#getting the users
	students = config.STUDENTS[0:nusers]

	#forming the groups
	remainder = nusers % nspawn

	if remainder == 0:
		groups = nusers / nspawn
	else:
		groups = (nusers / nspawn) + 1


	#control variables
	init = 0
	end = nspawn

	for i in range(groups):
		#Getting students in groups of nspawn students
		students_to_spawn = students[init:end]

		if i == (groups - 1):
			#Getting students in the last group
			students_to_spawn = students[init:]


		#Launching independent processes per user
		for student in students_to_spawn:
			process = multiprocessing.Process(target=doQuiz, args=(student,))
			process.start()

		#updating control variables
		init = end
		end += nspawn

		time.sleep(max_time)