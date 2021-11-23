SET FOREIGN_KEY_CHECKS = 0;   
drop table  if exists firstProject.accounts_classroom ;
drop table if exists firstProject.accounts_department  ;
drop table if exists firstProject.accounts_course ;
drop table if exists firstProject.accounts_instructor ;
drop table if exists firstProject.accounts_section ;
drop table if exists firstProject.accounts_teaches ;
drop table if exists firstProject.accounts_student ;
drop table if exists firstProject.accounts_takes ;
drop table if exists firstProject.accounts_advisor ;
drop table if exists firstProject.accounts_time_slot ;
drop table if exists firstProject.accounts_prereq ;
SET FOREIGN_KEY_CHECKS = 1;
create table firstProject.accounts_classroom(
	building	varchar(15),
	room_number	varchar(7),
	capacity	numeric(4,0),
	primary key (building, room_number)
	);

create table firstProject.accounts_department(
	dept_name	varchar(20), 
	building	varchar(15), 
	budget		numeric(12,2) check (budget > 0),
	primary key (dept_name)
	);

create table firstProject.accounts_course(
	course_id		varchar(8), 
	title			varchar(50), 
	dept_name		varchar(20),
	credits		numeric(2,0) check (credits > 0),
	primary key (course_id),
	foreign key (dept_name) references firstProject.accounts_department(dept_name) on delete set null
	);

create table firstProject.accounts_instructor(
	ID varchar(5), 
	name varchar(20) not null, 
	dept_name varchar(20), 
	salary numeric(8,2) check (salary > 29000),
	primary key (ID),
	foreign key (dept_name) references firstProject.accounts_department(dept_name) on delete set null
	);

create table firstProject.accounts_section(
	course_id		varchar(8), 
    sec_id			varchar(8),
	semester		varchar(6) check (semester in ('Fall', 'Winter', 'Spring', 'Summer')), 
	year			numeric(4,0) check (year > 1701 and year < 2100), 
	building		varchar(15),
	room_number		varchar(7),
	time_slot_id		varchar(4),
	primary key (course_id, sec_id, semester, year),
	foreign key (course_id) references firstProject.accounts_course(course_id) on delete cascade,
	foreign key (building, room_number) references firstProject.accounts_classroom(building,room_number) on delete set null
	);

create table firstProject.accounts_teaches(
	ID			varchar(5), 
	course_id		varchar(8),
	sec_id			varchar(8), 
	semester		varchar(6),
	year			numeric(4,0),
	primary key (ID, course_id, sec_id, semester, year),
	foreign key (course_id,sec_id, semester, year) references firstProject.accounts_section(course_id,sec_id,semester,year) on delete cascade,
	foreign key (ID) references firstProject.accounts_instructor(ID) on delete cascade
	);

create table firstProject.accounts_student(
	ID			varchar(5), 
	name			varchar(20) not null, 
	dept_name		varchar(20), 
	tot_cred		numeric(3,0) check (tot_cred >= 0),
	primary key (ID),
	foreign key (dept_name) references firstProject.accounts_department(dept_name) on delete set null
	);

create table firstProject.accounts_takes(
	ID	varchar(5), 
	course_id varchar(8),
	sec_id varchar(8), 
	semester varchar(6),
	year numeric(4,0),
	grade varchar(2),
	primary key (ID, course_id, sec_id, semester, year),
	foreign key (course_id,sec_id, semester, year) references firstProject.accounts_section(course_id,sec_id,semester,year) on delete cascade,
	foreign key (ID) references firstProject.accounts_student(ID) on delete cascade
	);

create table firstProject.accounts_advisor(
	s_ID varchar(5),
	i_ID varchar(5),
	primary key(s_ID),
	foreign key(i_ID) references firstProject.accounts_instructor(ID) on delete set null,
	foreign key(s_ID) references firstProject.accounts_student (ID) on delete cascade
	);

create table firstProject.accounts_time_slot(
	time_slot_id varchar(4),
	day	varchar(1),
	start_hr numeric(2) check (start_hr >= 0 and start_hr < 24),
	start_min numeric(2) check (start_min >= 0 and start_min < 60),
	end_hr numeric(2) check (end_hr >= 0 and end_hr < 24),
	end_min	numeric(2) check (end_min >= 0 and end_min < 60),
	primary key (time_slot_id, day, start_hr, start_min)
	);
create table firstProject.accounts_prereq(
	course_id varchar(8), 
	prereq_id varchar(8),
	primary key (course_id, prereq_id),
	foreign key (course_id) references firstProject.accounts_course(course_id) on delete cascade,
	foreign key (prereq_id) references firstProject.accounts_course(course_id)
	);
insert into firstproject.accounts_classroom values ('Packard', '101', '500');
insert into firstproject.accounts_classroom values ('Painter', '514', '10');
insert into firstproject.accounts_classroom values ('Taylor', '3128', '70');
insert into firstproject.accounts_classroom values ('Watson', '100', '30');
insert into firstproject.accounts_classroom values ('Watson', '120', '50');
insert into firstproject.accounts_department values ('Biology', 'Watson', '90000');
insert into firstproject.accounts_department values ('Comp. Sci.', 'Taylor', '100000');
insert into firstproject.accounts_department values ('Elec. Eng.', 'Taylor', '85000');
insert into firstproject.accounts_department values ('Finance', 'Painter', '120000');
insert into firstproject.accounts_department values ('History', 'Painter', '50000');
insert into firstproject.accounts_department values ('Music', 'Packard', '80000');
insert into firstproject.accounts_department values ('Physics', 'Watson', '70000');
insert into firstproject.accounts_course values ('BIO-101', 'Intro. to Biology', 'Biology', '4');
insert into firstproject.accounts_course values ('BIO-301', 'Genetics', 'Biology', '4');
insert into firstproject.accounts_course values ('BIO-399', 'Computational Biology', 'Biology', '3');
insert into firstproject.accounts_course values ('CS-101', 'Intro. to Computer Science', 'Comp. Sci.', '4');
insert into firstproject.accounts_course values ('CS-190', 'Game Design', 'Comp. Sci.', '4');
insert into firstproject.accounts_course values ('CS-315', 'Robotics', 'Comp. Sci.', '3');
insert into firstproject.accounts_course values ('CS-319', 'Image Processing', 'Comp. Sci.', '3');
insert into firstproject.accounts_course values ('CS-347', 'Database System Concepts', 'Comp. Sci.', '3');
insert into firstproject.accounts_course values ('EE-181', 'Intro. to Digital Systems', 'Elec. Eng.', '3');
insert into firstproject.accounts_course values ('FIN-201', 'Investment Banking', 'Finance', '3');
insert into firstproject.accounts_course values ('HIS-351', 'World History', 'History', '3');
insert into firstproject.accounts_course values ('MU-199', 'Music Video Production', 'Music', '3');
insert into firstproject.accounts_course values ('PHY-101', 'Physical Principles', 'Physics', '4');
insert into firstproject.accounts_instructor values ('10101', 'Srinivasan', 'Comp. Sci.', '65000');
insert into firstproject.accounts_instructor values ('12121', 'Wu', 'Finance', '90000');
insert into firstproject.accounts_instructor values ('15151', 'Mozart', 'Music', '40000');
insert into firstproject.accounts_instructor values ('22222', 'Einstein', 'Physics', '95000');
insert into firstproject.accounts_instructor values ('32343', 'El Said', 'History', '60000');
insert into firstproject.accounts_instructor values ('33456', 'Gold', 'Physics', '87000');
insert into firstproject.accounts_instructor values ('45565', 'Katz', 'Comp. Sci.', '75000');
insert into firstproject.accounts_instructor values ('58583', 'Califieri', 'History', '62000');
insert into firstproject.accounts_instructor values ('76543', 'Singh', 'Finance', '80000');
insert into firstproject.accounts_instructor values ('76766', 'Crick', 'Biology', '72000');
insert into firstproject.accounts_instructor values ('83821', 'Brandt', 'Comp. Sci.', '92000');
insert into firstproject.accounts_instructor values ('98345', 'Kim', 'Elec. Eng.', '80000');
insert into firstproject.accounts_section values ('BIO-101', '1', 'Summer', '2009', 'Painter', '514', 'B');
insert into firstproject.accounts_section values ('BIO-301', '1', 'Summer', '2010', 'Painter', '514', 'A');
insert into firstproject.accounts_section values ('CS-101', '1', 'Fall', '2009', 'Packard', '101', 'H');
insert into firstproject.accounts_section values ('CS-101', '1', 'Spring', '2010', 'Packard', '101', 'F');
insert into firstproject.accounts_section values ('CS-190', '1', 'Spring', '2009', 'Taylor', '3128', 'E');
insert into firstproject.accounts_section values ('CS-190', '2', 'Spring', '2009', 'Taylor', '3128', 'A');
insert into firstproject.accounts_section values ('CS-315', '1', 'Spring', '2010', 'Watson', '120', 'D');
insert into firstproject.accounts_section values ('CS-319', '1', 'Spring', '2010', 'Watson', '100', 'B');
insert into firstproject.accounts_section values ('CS-319', '2', 'Spring', '2010', 'Taylor', '3128', 'C');
insert into firstproject.accounts_section values ('CS-347', '1', 'Fall', '2009', 'Taylor', '3128', 'A');
insert into firstproject.accounts_section values ('EE-181', '1', 'Spring', '2009', 'Taylor', '3128', 'C');
insert into firstproject.accounts_section values ('FIN-201', '1', 'Spring', '2010', 'Packard', '101', 'B');
insert into firstproject.accounts_section values ('HIS-351', '1', 'Spring', '2010', 'Painter', '514', 'C');
insert into firstproject.accounts_section values ('MU-199', '1', 'Spring', '2010', 'Packard', '101', 'D');
insert into firstproject.accounts_section values ('PHY-101', '1', 'Fall', '2009', 'Watson', '100', 'A');
insert into firstproject.accounts_teaches values ('10101', 'CS-101', '1', 'Fall', '2009');
insert into firstproject.accounts_teaches values ('10101', 'CS-315', '1', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('10101', 'CS-347', '1', 'Fall', '2009');
insert into firstproject.accounts_teaches values ('12121', 'FIN-201', '1', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('15151', 'MU-199', '1', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('22222', 'PHY-101', '1', 'Fall', '2009');
insert into firstproject.accounts_teaches values ('32343', 'HIS-351', '1', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('45565', 'CS-101', '1', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('45565', 'CS-319', '1', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('76766', 'BIO-101', '1', 'Summer', '2009');
insert into firstproject.accounts_teaches values ('76766', 'BIO-301', '1', 'Summer', '2010');
insert into firstproject.accounts_teaches values ('83821', 'CS-190', '1', 'Spring', '2009');
insert into firstproject.accounts_teaches values ('83821', 'CS-190', '2', 'Spring', '2009');
insert into firstproject.accounts_teaches values ('83821', 'CS-319', '2', 'Spring', '2010');
insert into firstproject.accounts_teaches values ('98345', 'EE-181', '1', 'Spring', '2009');
insert into firstproject.accounts_student values ('00128', 'Zhang', 'Comp. Sci.', '102');
insert into firstproject.accounts_student values ('12345', 'Shankar', 'Comp. Sci.', '32');
insert into firstproject.accounts_student values ('19991', 'Brandt', 'History', '80');
insert into firstproject.accounts_student values ('23121', 'Chavez', 'Finance', '110');
insert into firstproject.accounts_student values ('44553', 'Peltier', 'Physics', '56');
insert into firstproject.accounts_student values ('45678', 'Levy', 'Physics', '46');
insert into firstproject.accounts_student values ('54321', 'Williams', 'Comp. Sci.', '54');
insert into firstproject.accounts_student values ('55739', 'Sanchez', 'Music', '38');
insert into firstproject.accounts_student values ('70557', 'Snow', 'Physics', '0');
insert into firstproject.accounts_student values ('76543', 'Brown', 'Comp. Sci.', '58');
insert into firstproject.accounts_student values ('76653', 'Aoi', 'Elec. Eng.', '60');
insert into firstproject.accounts_student values ('98765', 'Bourikas', 'Elec. Eng.', '98');
insert into firstproject.accounts_student values ('98988', 'Tanaka', 'Biology', '120');
insert into firstproject.accounts_takes values ('00128', 'CS-101', '1', 'Fall', '2009', 'A');
insert into firstproject.accounts_takes values ('00128', 'CS-347', '1', 'Fall', '2009', 'A-');
insert into firstproject.accounts_takes values ('12345', 'CS-101', '1', 'Fall', '2009', 'C');
insert into firstproject.accounts_takes values ('12345', 'CS-190', '2', 'Spring', '2009', 'A');
insert into firstproject.accounts_takes values ('12345', 'CS-315', '1', 'Spring', '2010', 'A');
insert into firstproject.accounts_takes values ('12345', 'CS-347', '1', 'Fall', '2009', 'A');
insert into firstproject.accounts_takes values ('19991', 'HIS-351', '1', 'Spring', '2010', 'B');
insert into firstproject.accounts_takes values ('23121', 'FIN-201', '1', 'Spring', '2010', 'C+');
insert into firstproject.accounts_takes values ('44553', 'PHY-101', '1', 'Fall', '2009', 'B-');
insert into firstproject.accounts_takes values ('45678', 'CS-101', '1', 'Fall', '2009', 'F');
insert into firstproject.accounts_takes values ('45678', 'CS-101', '1', 'Spring', '2010', 'B+');
insert into firstproject.accounts_takes values ('45678', 'CS-319', '1', 'Spring', '2010', 'B');
insert into firstproject.accounts_takes values ('54321', 'CS-101', '1', 'Fall', '2009', 'A-');
insert into firstproject.accounts_takes values ('54321', 'CS-190', '2', 'Spring', '2009', 'B+');
insert into firstproject.accounts_takes values ('55739', 'MU-199', '1', 'Spring', '2010', 'A-');
insert into firstproject.accounts_takes values ('76543', 'CS-101', '1', 'Fall', '2009', 'A');
insert into firstproject.accounts_takes values ('76543', 'CS-319', '2', 'Spring', '2010', 'A');
insert into firstproject.accounts_takes values ('76653', 'EE-181', '1', 'Spring', '2009', 'C');
insert into firstproject.accounts_takes values ('98765', 'CS-101', '1', 'Fall', '2009', 'C-');
insert into firstproject.accounts_takes values ('98765', 'CS-315', '1', 'Spring', '2010', 'B');
insert into firstproject.accounts_takes values ('98988', 'BIO-101', '1', 'Summer', '2009', 'A');
insert into firstproject.accounts_takes values ('98988', 'BIO-301', '1', 'Summer', '2010', null);
insert into firstproject.accounts_advisor values ('00128', '45565');
insert into firstproject.accounts_advisor values ('12345', '10101');
insert into firstproject.accounts_advisor values ('23121', '76543');
insert into firstproject.accounts_advisor values ('44553', '22222');
insert into firstproject.accounts_advisor values ('45678', '22222');
insert into firstproject.accounts_advisor values ('76543', '45565');
insert into firstproject.accounts_advisor values ('76653', '98345');
insert into firstproject.accounts_advisor values ('98765', '98345');
insert into firstproject.accounts_advisor values ('98988', '76766');
insert into firstproject.accounts_time_slot values ('A', 'M', '8', '0', '8', '50');
insert into firstproject.accounts_time_slot values ('A', 'W', '8', '0', '8', '50');
insert into firstproject.accounts_time_slot values ('A', 'F', '8', '0', '8', '50');
insert into firstproject.accounts_time_slot values ('B', 'M', '9', '0', '9', '50');
insert into firstproject.accounts_time_slot values ('B', 'W', '9', '0', '9', '50');
insert into firstproject.accounts_time_slot values ('B', 'F', '9', '0', '9', '50');
insert into firstproject.accounts_time_slot values ('C', 'M', '11', '0', '11', '50');
insert into firstproject.accounts_time_slot values ('C', 'W', '11', '0', '11', '50');
insert into firstproject.accounts_time_slot values ('C', 'F', '11', '0', '11', '50');
insert into firstproject.accounts_time_slot values ('D', 'M', '13', '0', '13', '50');
insert into firstproject.accounts_time_slot values ('D', 'W', '13', '0', '13', '50');
insert into firstproject.accounts_time_slot values ('D', 'F', '13', '0', '13', '50');
insert into firstproject.accounts_time_slot values ('E', 'T', '10', '30', '11', '45 ');
insert into firstproject.accounts_time_slot values ('E', 'R', '10', '30', '11', '45 ');
insert into firstproject.accounts_time_slot values ('F', 'T', '14', '30', '15', '45 ');
insert into firstproject.accounts_time_slot values ('F', 'R', '14', '30', '15', '45 ');
insert into firstproject.accounts_time_slot values ('G', 'M', '16', '0', '16', '50');
insert into firstproject.accounts_time_slot values ('G', 'W', '16', '0', '16', '50');
insert into firstproject.accounts_time_slot values ('G', 'F', '16', '0', '16', '50');
insert into firstproject.accounts_time_slot values ('H', 'W', '10', '0', '12', '30');
insert into firstproject.accounts_prereq values ('BIO-301', 'BIO-101');
insert into firstproject.accounts_prereq values ('BIO-399', 'BIO-101');
insert into firstproject.accounts_prereq values ('CS-190', 'CS-101');
insert into firstproject.accounts_prereq values ('CS-315', 'CS-101');
insert into firstproject.accounts_prereq values ('CS-319', 'CS-101');
insert into firstproject.accounts_prereq values ('CS-347', 'CS-101');
insert into firstproject.accounts_prereq values ('EE-181', 'PHY-101');
commit;