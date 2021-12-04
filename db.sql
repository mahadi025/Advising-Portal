--
-- Create model Classroom
--
CREATE TABLE `accounts_classroom` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `building` varchar(15) NOT NULL, `room_number` varchar(7) NOT NULL, `capacity` numeric(4, 0) NULL);
--
-- Create model Course
--
CREATE TABLE `accounts_course` (`course_id` varchar(8) NOT NULL PRIMARY KEY, `title` varchar(50) NULL, `credits` numeric(2, 1) NULL);
--
-- Create model Department
--
CREATE TABLE `accounts_department` (`dept_name` varchar(20) NOT NULL PRIMARY KEY, `building` varchar(15) NULL);
--
-- Create model Instructor
--
CREATE TABLE `accounts_instructor` (`instructorId` varchar(13) NOT NULL PRIMARY KEY, `firstName` varchar(50) NOT NULL, `lastName` varchar(20) NULL, `email` varchar(254) NULL, `bloodGroup` varchar(3) NULL, `presentAddress` varchar(60) NULL, `i_dept_name` varchar(20) NULL, `user_id` integer NULL UNIQUE);
--
-- Create model Section
--
CREATE TABLE `accounts_section` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `secId` varchar(8) NOT NULL, `semester` varchar(6) NOT NULL, `year` numeric(4, 0) NOT NULL, `classroom_id` bigint NOT NULL, `course_id` varchar(8) NOT NULL, `instructor_id` varchar(13) NOT NULL);
--
-- Create model Student
--
CREATE TABLE `accounts_student` (`studentId` varchar(13) NOT NULL PRIMARY KEY, `firstName` varchar(20) NOT NULL, `lastName` varchar(20) NULL, `img` varchar(100) NULL, `email` varchar(254) NULL, `tot_cred` numeric(3, 1) NULL, `bloodGroup` varchar(3) NULL, `presentAddress` varchar(60) NULL, `phoneNumber` varchar(14) NULL, `dept_name` varchar(20) NULL, `user_id` integer NULL UNIQUE);
--
-- Create model TimeSlot
--
CREATE TABLE `accounts_timeslot` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `time_slot_id` varchar(10) NOT NULL, `day` varchar(2) NOT NULL, `start_hr` varchar(2) NOT NULL, `start_min` varchar(2) NOT NULL, `end_hr` varchar(2) NOT NULL, `end_min` varchar(2) NOT NULL);
--
-- Create model Takes
--
CREATE TABLE `accounts_takes` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `grade` varchar(2) NULL, `section_id` bigint NOT NULL UNIQUE, `studentId` varchar(13) NOT NULL);
--
-- Add field timeSlot to section
--
ALTER TABLE `accounts_section` ADD COLUMN `timeSlot_id` bigint NOT NULL , ADD CONSTRAINT `accounts_section_timeSlot_id_d023920d_fk_accounts_timeslot_id` FOREIGN KEY (`timeSlot_id`) REFERENCES `accounts_timeslot`(`id`);
--
-- Add field dept_name to course
--
ALTER TABLE `accounts_course` ADD COLUMN `dept_name` varchar(20) NULL , ADD CONSTRAINT `accounts_course_dept_name_c6b5f929_fk_accounts_` FOREIGN KEY (`dept_name`) REFERENCES `accounts_department`(`dept_name`);
--
-- Alter unique_together for section (5 constraint(s))
--
ALTER TABLE `accounts_section` ADD CONSTRAINT `accounts_section_secId_course_id_semester_year_4cd521be_uniq` UNIQUE (`secId`, `course_id`, `semester`, `year`);
ALTER TABLE `accounts_section` ADD CONSTRAINT `accounts_section_course_id_secId_semester_7198b09b_uniq` UNIQUE (`course_id`, `secId`, `semester`, `year`, `timeSlot_id`);
accounts_student` (`studentId`);ALTER TABLE `accounts_prereq` ADD CONSTRAINT `accounts_prereq_course_id_prereq_id_4e2c797b_uniq` UNIQUE (`course_id`, `prereq_id`);
ALTER TABLE `accounts_prereq` ADD CONSTRAINT `accounts_prereq_course_id_4b764e9e_fk_accounts_course_course_id` FOREIGN KEY (`course_id`) REFERENCES `accounts_course` (`course_id`);
ALTER TABLE `accounts_prereq` ADD CONSTRAINT `accounts_prereq_prereq_id_39dab4e4_fk_accounts_course_course_id` FOREIGN KEY (`prereq_id`) REFERENCES `accounts_course` (`course_id`);
ALTER TABLE `accounts_advisor` ADD CONSTRAINT `accounts_advisor_s_ID_fbc3a6af_fk_accounts_student_studentId` FOREIGN KEY (`s_ID`) REFERENCES `accounts_student` (`studentId`);
ALTER TABLE `accounts_advisor` ADD CONSTRAINT `accounts_advisor_i_ID_e168348b_fk_accounts_` FOREIGN KEY (`i_ID`) REFERENCES `accounts_instructor` (`instructorId`);