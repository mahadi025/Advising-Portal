insert into accounts_department (dept_name,building) values ('CSE','Main Building');
insert into accounts_department (dept_name,building) values ('EEE','Main Building');
insert into accounts_department (dept_name,building) values ('MPS','AB2');
insert into accounts_department (dept_name,building) values ('ENG','Main Building');
insert into accounts_department (dept_name,building) values ('ECO','AB1');
insert into accounts_department (dept_name,building) values ('SOC','Main Building');

insert into accounts_classroom (id,building,room_number,capacity) values (1,'AB1',303,35);
insert into accounts_classroom (id,building,room_number,capacity) values (2,'AB1',304,35);
insert into accounts_classroom (id,building,room_number,capacity) values (3,'AB1',305,35);
insert into accounts_classroom (id,building,room_number,capacity) values (4,'AB1',403,35);
insert into accounts_classroom (id,building,room_number,capacity) values (5,'AB1',404,35);
insert into accounts_classroom (id,building,room_number,capacity) values (6,'AB1',405,35);
insert into accounts_classroom (id,building,room_number,capacity) values (7,'AB2',303,35);
insert into accounts_classroom (id,building,room_number,capacity) values (8,'AB2',304,35);
insert into accounts_classroom (id,building,room_number,capacity) values (9,'AB2',305,35);
insert into accounts_classroom (id,building,room_number,capacity) values (10,'AB2',403,35);
insert into accounts_classroom (id,building,room_number,capacity) values (11,'AB2',404,35);
insert into accounts_classroom (id,building,room_number,capacity) values (12,'AB2',405,35);

insert into accounts_course (course_id,title,credits,dept_name) values('CSE103','Structured Programming',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE106','Discrete Mathematics',3.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE110','Object Oriented Programming',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE200','Computer-Aided Engineering Drawing',1.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE209','Electrical Circuits',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE207','Data Structures',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE251','Electronic Circuits',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE246','Algorithms',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE302','Database Systems',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE325','Operating Systems',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE345','Digital Logic Design',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE347','Information System Analysis and Design',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE360','Computer Architecture',3.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE405','Computer Networks',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE407','Green Computing',3.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE487','Cyber Security, Ethics and Law',3.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE495','IT Project Management and Entrepreneurship',3.0,'CSE');



--TimeSlot
--ST
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(1,'ST1','ST','08','30','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(2,'ST2','ST','10','10','11','40');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(3,'ST3','ST','11','50','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(4,'ST4','ST','01','30','03','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(5,'ST5','ST','03','10','04','40');
--MW
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(6,'MW1','MW','08','30','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(7,'MW2','MW','10','10','11','40');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(8,'MW3','MW','11','50','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(9,'Mw4','MW','01','30','03','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(10,'Mw5','MW','03','10','04','40');
--SR
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(11,'SR1','SR','08','30','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(12,'SR2','SR','10','10','11','40');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(13,'SR3','SR','11','50','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(14,'SR4','SR','01','30','03','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(15,'SR5','SR','03','10','04','40');
--TR
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(16,'TR1','TR','08','30','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(17,'TR2','TR','10','10','11','40');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(18,'TR3','TR','11','50','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(19,'TR4','TR','01','30','03','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(20,'TR5','TR','03','10','04','40');

--LAB
--2H
--S
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(21,'SL1','S','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(22,'SL2','S','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(23,'SL3','S','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(24,'SL4','S','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(25,'SL4','S','03','40','05','40');
--M
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(26,'ML1','M','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(27,'ML2','M','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(28,'ML3','M','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(29,'ML4','M','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(30,'ML4','M','03','40','05','40');
--T
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(31,'TL1','T','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(32,'TL2','T','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(33,'TL3','T','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(34,'TL4','T','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(35,'TL4','T','03','40','05','40');
--W
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(36,'WL1','W','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(37,'WL2','W','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(38,'WL3','W','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(39,'WL4','W','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(40,'WL4','W','03','40','05','40');
--R
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(41,'RL1','R','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(42,'RL2','R','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(43,'RL3','R','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(44,'RL4','R','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(45,'RL4','R','03','40','05','40');

--section
--CSE 103
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(1,1,'Summer',2019,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(2,1,'Spring',2019,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(3,1,'Fall',2019,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(4,2,'Summer',2019,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(5,2,'Spring',2019,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(6,2,'Fall',2019,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(7,3,'Summer',2019,1,'CSE103','OVI',2);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(8,3,'Spring',2019,1,'CSE103','OVI',2);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(9,3,'Fall',2019,1,'CSE103','OVI',2);

insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(10,1,'Summer',2020,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(11,1,'Spring',2020,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(12,1,'Fall',2020,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(13,2,'Summer',2020,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(14,2,'Spring',2020,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(15,2,'Fall',2020,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(16,3,'Summer',2020,1,'CSE103','OVI',2);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(17,3,'Spring',2020,1,'CSE103','OVI',2);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(18,3,'Fall',2020,1,'CSE103','OVI',2);

insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(19,1,'Summer',2021,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(20,1,'Spring',2021,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(21,1,'Fall',2021,10,'CSE103','MIE',3);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(22,2,'Summer',2021,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(23,2,'Spring',2021,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(24,2,'Fall',2021,1,'CSE103','MMSU',1);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(25,3,'Summer',2021,1,'CSE103','OVI',2);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(26,3,'Spring',2021,1,'CSE103','OVI',2);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(27,3,'Fall',2021,1,'CSE103','OVI',2);

--CSE 106
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id) values(1,3,'Summer',2019,10,'CSE106','MIE',5);