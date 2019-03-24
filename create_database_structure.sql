CREATE TABLE IF NOT EXISTS quiztest (
									testid integer PRIMARY KEY,
									testdate text NOT NULL,
									nusers integer,
									nspawn integer,
									tspawn integer,
									max_time integer
							);

CREATE TABLE IF NOT EXISTS results (
									testid integer,
									active_users integer,
									html_error_503 integer,
									html_error_404 integer,
									undef_html_error integer,
									network_error_104 integer,
									network_error_110 integer,
									network_error_111 integer,
									successful_users integer,
									total_users integer,
									FOREIGN KEY (testid) REFERENCES quiztest(testid)
							);

CREATE TABLE IF NOT EXISTS user_progress_time (
									testid integer,
									moodle_site real,
									login real,
									site_home real,
									course real,
									quiz real,
									submit_answers real,
									FOREIGN KEY (testid) REFERENCES quiztest(testid)
							);