#Moodle site URL for login to the course
MOODLE_SITE_LOGIN_URL='http://localhost/moodle/login/index.php'

#range of students available
FIRST_STUDENT=1
LAST_STUDENT=15000
STUDENTS = ['username' + str(i) for i in range(FIRST_STUDENT, LAST_STUDENT + 1)]

#course name
COURSE_NAME='Quiztest'

#Quiz name
QUIZ_NAME='Quiztest'