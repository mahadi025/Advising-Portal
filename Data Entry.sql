insert into accounts_department (dept_name,building) values ('CSE','Main Building');
insert into accounts_department (dept_name,building) values ('EEE','Main Building');
insert into accounts_department (dept_name,building) values ('MPS','AB2');
insert into accounts_department (dept_name,building) values ('ENG','Main Building');
insert into accounts_department (dept_name,building) values ('ECO','AB1');
insert into accounts_department (dept_name,building) values ('SOC','Main Building');

insert into accounts_classroom (id,building,room_number) values (1,'AB1',303);
insert into accounts_classroom (id,building,room_number) values (2,'AB1',304);
insert into accounts_classroom (id,building,room_number) values (3,'AB1',305);
insert into accounts_classroom (id,building,room_number) values (4,'AB1',403);
insert into accounts_classroom (id,building,room_number) values (5,'AB1',404);
insert into accounts_classroom (id,building,room_number) values (6,'AB1',405);
insert into accounts_classroom (id,building,room_number) values (7,'AB2',303);
insert into accounts_classroom (id,building,room_number) values (8,'AB2',304);
insert into accounts_classroom (id,building,room_number) values (9,'AB2',305);
insert into accounts_classroom (id,building,room_number) values (10,'AB2',403);
insert into accounts_classroom (id,building,room_number) values (11,'AB2',404);
insert into accounts_classroom (id,building,room_number) values (12,'AB2',405);

--Courses
insert into accounts_course (course_id,title,credits,dept_name) values('CSE103','Structured Programming',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE103L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE106','Discrete Mathematics',3.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE110','Object Oriented Programming',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE110L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE200','Computer-Aided Engineering Drawing',1.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE209','Electrical Circuits',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE209L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE207','Data Structures',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE207L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE251','Electronic Circuits',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE251L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE246','Algorithms',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE246L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE302','Database Systems',4.5,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE302L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE325','Operating Systems',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE325L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE345','Digital Logic Design',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE345L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE347','Information System Analysis and Design',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE347L','LAB',0.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE360','Computer Architecture',3.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE405','Computer Networks',4.0,'CSE');
insert into accounts_course (course_id,title,credits,dept_name) values('CSE405L','LAB',0.0,'CSE');
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
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(9,'MW4','MW','01','30','03','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(10,'MW5','MW','03','10','04','40');
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
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(21,'SL2H-1','S','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(22,'SL2H-2','S','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(23,'SL2H-3','S','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(24,'SL2H-4','S','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(25,'SL2H-5','S','03','40','05','40');
--M
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(26,'ML2H-1','M','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(27,'ML2H-2','M','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(28,'ML2H-3','M','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(29,'ML2H-4','M','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(30,'ML2H-5','M','03','40','05','40');
--T
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(31,'TL2H-1','T','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(32,'TL2H-2','T','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(33,'TL2H-3','T','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(34,'TL2H-4','T','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(35,'TL2H-5','T','03','40','05','40');
--W
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(36,'WL2H-1','W','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(37,'WL2H-2','W','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(38,'WL2H-3','W','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(39,'WL2H-4','W','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(40,'WL2H-5','W','03','40','05','40');
--R
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(41,'RL2H-1','R','08','00','10','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(42,'RL2H-2','R','10','10','12','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(43,'RL2H-3','R','12','20','01','20');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(44,'RL2H-4','R','01','30','03','30');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(45,'RL2H-5','R','03','40','05','40');


--LAB
--3H
--S
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(46,'SL3H-1','S','08','00','11','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(47,'SL3H-2','S','10','10','01','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(48,'SL3H-3','S','11','50','02','50');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(49,'SL3H-4','S','03','10','06','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(50,'SL3H-5','S','04','50','07','50');
--M
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(51,'ML3H-1','M','08','00','11','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(52,'ML3H-2','M','10','10','01','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(53,'ML3H-3','M','11','50','02','50');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(54,'ML3H-4','M','03','10','06','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(55,'ML3H-5','M','04','50','07','50');
--T
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(56,'TL3H-1','T','08','00','11','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(57,'TL3H-2','T','10','10','01','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(58,'TL3H-3','T','11','50','02','50');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(59,'TL3H-4','T','03','10','06','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(60,'TL3H-5','T','04','50','07','50');
--W
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(61,'WL3H-1','W','08','00','11','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(62,'WL3H-2','W','10','10','01','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(63,'WL3H-3','W','11','50','02','50');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(64,'WL3H-4','W','03','10','06','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(65,'WL3H-5','W','04','50','07','50');
--T
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(65,'RL3H-1','R','08','00','11','00');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(66,'RL3H-2','R','10','10','01','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(67,'RL3H-3','R','11','50','02','50');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(68,'RL3H-4','R','03','10','06','10');
insert into accounts_timeslot(id,time_slot_id,day,start_hr,start_min,end_hr,end_min) values(69,'RL3H-5','R','04','50','07','50');
--section
--CSE 103
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(1,1,'Summer',2019,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(2,1,'Summer',2019,10,'CSE103L','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(2,1,'Spring',2019,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(3,1,'Fall',2019,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(4,2,'Summer',2019,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(5,2,'Spring',2019,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(6,2,'Fall',2019,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(7,3,'Summer',2019,1,'CSE103','OVI',2,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(8,3,'Spring',2019,1,'CSE103','OVI',2,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(9,3,'Fall',2019,1,'CSE103','OVI',2,35);

insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(10,1,'Summer',2020,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(11,1,'Spring',2020,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(12,1,'Fall',2020,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(13,2,'Summer',2020,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(14,2,'Spring',2020,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(15,2,'Fall',2020,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(16,3,'Summer',2020,1,'CSE103','OVI',2,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(17,3,'Spring',2020,1,'CSE103','OVI',2,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(18,3,'Fall',2020,1,'CSE103','OVI',2,35);

insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(19,1,'Summer',2021,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(20,1,'Spring',2021,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(21,1,'Fall',2021,10,'CSE103','MIE',3,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(22,2,'Summer',2021,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(23,2,'Spring',2021,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(24,2,'Fall',2021,1,'CSE103','MMSU',1,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(25,3,'Summer',2021,1,'CSE103','OVI',2,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(26,3,'Spring',2021,1,'CSE103','OVI',2,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(27,3,'Fall',2021,1,'CSE103','OVI',2,35);

--CSE 106
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(28,1,'Summer',2019,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(29,1,'Spring',2019,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(30,1,'Fall',2019,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(31,2,'Summer',2019,7,'CSE106','DSU',5,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(32,2,'Spring',2019,7,'CSE106','DSU',5,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(33,2,'Fall',2019,7,'CSE106','DSU',5,35);

insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(34,1,'Summer',2020,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(35,1,'Spring',2020,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(36,1,'Fall',2020,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(37,2,'Summer',2020,7,'CSE106','DSU',5,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(38,2,'Spring',2020,7,'CSE106','DSU',5,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(39,2,'Fall',2020,7,'CSE106','DSU',5,35);

insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(40,1,'Summer',2021,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(41,1,'Spring',2021,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(42,1,'Fall',2021,10,'CSE106','MIE',4,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(43,2,'Summer',2021,7,'CSE106','DSU',5,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(44,2,'Spring',2021,7,'CSE106','DSU',5,35);
insert into accounts_section (id,secId,semester,year,classroom_id,course_id,instructor_id,timeSlot_id,capacity) values(45,2,'Fall',2021,7,'CSE106','DSU',5,35);