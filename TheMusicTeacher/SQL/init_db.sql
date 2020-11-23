DROP database IF EXISTS the_music_teacher;
CREATE database the_music_teacher;
use the_music_teacher;

CREATE table user(
                    u_id integer not null,
                    username varchar(25) not null,
                    email varchar(50) not null,
                    fname varchar(20) not null,
                    minit varchar(1),
                    lname varchar(20) not  null,
                    dob date,
                    gender char,
                    phone varchar(10),
                    date_created datetime,
                    last_login datetime,
                    verification boolean,
                    hashed_password varchar(40),
                    primary key (u_id));

INSERT INTO user VALUES(
                0, 'Skrillex', 'iheartdubstep32@email.edu', 'Sonny', 'J', 'Moore', '1988-01-15',
                'F', '0008675309', @user_date_created, @user_last_login, True, @user_password);
INSERT INTO user VALUES(
                1, 'Urgot', 'urgotTop@lol.edu', 'Pajama', 'S', 'Guardian', '1983-07-18',
                'M', '1111001111', @user_date_created, @user_last_login, True, @user_password);
INSERT INTO user VALUES(
                 2, 'Vel-koz', 'magesrule334@hotmail.net', 'Vee', 'L', 'Koz', '1997-03-22',
                 'F', '0123456789', @user_date_created, @user_last_login, True, @user_password);
INSERT INTO user VALUES(
                 3, 'Susan', 'suzluvsbeagles54@hotmail.net', 'Susan', 'R', 'Susan', '1962-06-24',
                 'F', '0123456789', @user_date_created, @user_last_login, True, @user_password);
INSERT INTO user VALUES(
                 4, 'ProfMD', 'profmd@email.edu', 'Professor', 'M', 'D', '1985-07-24',
                'F', '0113446788', @user_date_created, @user_last_login, True, @user_password);
INSERT INTO user VALUES(
                 5, 'Astley', 'rickroll@rickroll.edu', 'Richard', 'P', 'Astley', '1966-02-06',
                 'M', '0173426688', @user_date_created, @user_last_login, True, @user_password);

CREATE table course(
                    c_id integer,
                    c_name varchar(30) not null,
                    i_id integer not null,
                    active boolean,
                    primary key (c_id),
                    foreign key (i_id) references user(u_id)
                        on delete cascade);

INSERT INTO course VALUES(0, 'Intro to Dubstep', 0, True);
INSERT INTO course VALUES(1, 'Advanced Dubstep', 0, True);
INSERT INTO course VALUES(2, 'Really Advanced Dubstep', 0, True);
INSERT INTO course VALUES(3, 'Music for Gaming', 2, True);
INSERT INTO course VALUES(4, 'How to Make Lo-Fi', 2, False);
INSERT INTO course VALUES(5, 'Intro to Classical Music', 3, False);
INSERT INTO course VALUES(6, '80s Music', 5, Active);
INSERT INTO course VALUES(7, 'Pop Music Theory', 5, Active);

CREATE table section(
                    sec_id varchar(10),
                    c_id integer,
                    primary key (sec_id, c_id),
                    foreign key (c_id) references course(c_id)
                        on delete cascade);

INSERT INTO section VALUES('0', 0);
INSERT INTO section VALUES('1', 0);
INSERT INTO section VALUES('0', 1);
INSERT INTO section VALUES('0', 2);
INSERT INTO section VALUES('1', 2);
INSERT INTO section VALUES('sec-1', 3);
INSERT INTO section VALUES('sec-2', 3);
INSERT INTO section VALUES('sec-1', 4);
INSERT INTO section VALUES('S1', 5);
INSERT INTO section VALUES('S2', 5);
INSERT INTO section VALUES('S3', 5);
INSERT INTO section VALUES('class1', 6);
INSERT INTO section VALUES('class2', 6);
INSERT INTO section VALUES('class1', 7);
INSERT INTO section VALUES('class2', 7);
INSERT INTO section VALUES('class3', 7);

CREATE table enrolled(
                    s_id integer,
                    sec_id varchar(10),
                    c_id integer,
                    primary key (s_id, sec_id, c_id),
                    foreign key (s_id) references user(u_id)
                        on delete cascade,
                    foreign key (sec_id) references section(sec_id)
                        on delete cascade,
                    foreign key (c_id) references section(c_id)
                        on delete cascade);

INSERT INTO enrolled VALUES(0, 'S1', 5);
INSERT INTO enrolled VALUES(1, '0', 0);
INSERT INTO enrolled VALUES(1, 'S1', 5);
INSERT INTO enrolled VALUES(1, 'sec-1', 3);
INSERT INTO enrolled VALUES(2, '0', 0);
INSERT INTO enrolled VALUES(2, '1', 2);
INSERT INTO enrolled VALUES(3, '1', 2);
INSERT INTO enrolled VALUES(3, 'class1', 6);
INSERT INTO enrolled VALUES(3, 'class2', 7);
INSERT INTO enrolled VALUES(4, 'class1', 6);
INSERT INTO enrolled VALUES(5, '1', 2);

CREATE table gradebook(
                    gi_name varchar(30),
                    sec_id varchar(10),
                    c_id integer,
                    category varchar(20),
                    date_start datetime,
                    date_due datetime,
                    published boolean,
                    primary key (gi_name, sec_id, c_id),
                    foreign key (sec_id) references section(sec_id)
                        on delete cascade,
                    foreign key (c_id) references section(c_id)
                        on delete cascade);

INSERT INTO gradebook VALUES('Assignment 1', 'class1', 6, 'Assignments', '2020-11-01 14:30:00', '2020-11-10 14:30:59', True);
INSERT INTO gradebook VALUES('Assignment 2', 'class1', 6, 'Assignments', '2020-11-10 14:30:00', '2020-11-15 14:30:59', True);
INSERT INTO gradebook VALUES('Assignment 3', 'class1', 6, 'Assignments', '2020-11-15 14:30:00', '2020-11-20 14:30:59', True);
INSERT INTO gradebook VALUES('Assignment 4', 'class1', 6, 'Assignments', '2020-11-20 14:30:00', '2020-11-25 14:30:59', True);
INSERT INTO gradebook VALUES('Quiz 1', 'class1', 6, 'Quizzes', '2020-11-10 14:30:00', '2020-11-10 16:30:59', True);
INSERT INTO gradebook VALUES('Quiz 2', 'class1', 6, 'Quizzes', '2020-11-20 14:30:00', '2020-11-20 16:30:59', True);
INSERT INTO gradebook VALUES('Dubstep Review', '1', 2, 'Assignments', '2020-09-10 00:00:00', '2020-09-17 23:59:59', True);
INSERT INTO gradebook VALUES('Dubstep Theory Report', '1', 2, 'Assignments', '2020-09-24 00:00:00', '2020-10-01 23:59:59', True);
INSERT INTO gradebook VALUES('Dubstep Beats', '1', 2, 'Labs', '2020-09-10 00:00:00', '2020-9-24 23:59:59', True);
INSERT INTO gradebook VALUES('Dubstep Drops', '1', 2, 'Labs', '2020-09-24 00:00:00', '2020-10-08 23:59:59', True);
INSERT INTO gradebook VALUES('Classical Music Overview', 'S1', 5, 'Assignments', '2019-09-10 12:00:00', '2019-09-17 12:00:59', True);
INSERT INTO gradebook VALUES('Assignment 1', 'S1', 5, 'Assignments', '2019-09-17 12:00:00', '2019-09-24 12:00:59', True);
INSERT INTO gradebook VALUES('Assignment 2', 'S1', 5, 'Assignments', '2019-09-24 12:00:00', '2020-10-01 12:00:59', True);
INSERT INTO gradebook VALUES('Assignment 3', 'S1', 5, 'Assignments', '2019-10-01 12:00:00', '2019-10-08 12:00:59', True);

CREATE TABLE graded_item(
                    gi_name	varchar(30),
                    s_id integer,
                    sec_id varchar(10),
                    c_id integer,
                    grade varchar(2),
                    score real(5,2),
                    primary key (gi_name, s_id, sec_id, c_id),
                    foreign key (gi_name) references gradebook(gi_name)
                        on delete cascade,
                    foreign key (s_id) references enrolled(s_id)
                        on delete cascade,
                    foreign key (sec_id) references enrolled(sec_id)
                        on delete cascade,
                    foreign key (c_id) references enrolled(c_id)
                        on delete cascade);

INSERT INTO graded_item VALUES('Dubstep Beats', 2, '1', 2, 'A+', 99.9);
INSERT INTO graded_item VALUES('Dubstep Beats', 3, '1', 2, 'B-', 80.8);
INSERT INTO graded_item VALUES('Dubstep Beats', 5, '1', 2, 'B', 85.8);
INSERT INTO graded_item VALUES('Dubstep Drops', 2, '1', 2, 'A+', 98.7);
INSERT INTO graded_item VALUES('Dubstep Drops', 3, '1', 2, 'B-', 82.6);
INSERT INTO graded_item VALUES('Dubstep Drops', 5, '1', 2, 'B', 84.0);
INSERT INTO graded_item VALUES('Dubstep Review', 2, '1', 2, 'A+', 99.3);
INSERT INTO graded_item VALUES('Dubstep Review', 3, '1', 2, 'B', 85.6);
INSERT INTO graded_item VALUES('Dubstep Review', 5, '1', 2, 'B+', 88.3);
INSERT INTO graded_item VALUES('Dubstep Theory Report', 2, '1', 2, 'A', 95.0);
INSERT INTO graded_item VALUES('Dubstep Theory Report', 3, '1', 2, 'B', 84.6);
INSERT INTO graded_item VALUES('Dubstep Theory Report', 5, '1', 2, 'B+', 88.9);
INSERT INTO graded_item VALUES('Assignment 1', 0, 'S1', 5, 'A', 95.6);
INSERT INTO graded_item VALUES('Assignment 1', 1, 'S1', 5, 'B+', 88.9);
INSERT INTO graded_item VALUES('Assignment 2', 0, 'S1', 5, 'A+', 99.6);
INSERT INTO graded_item VALUES('Assignment 2', 1, 'S1', 5, 'A', 95.4);
INSERT INTO graded_item VALUES('Assignment 3', 0, 'S1', 5, 'A-', 90.7);
INSERT INTO graded_item VALUES('Assignment 3', 1, 'S1', 5, 'B', 85.5);
INSERT INTO graded_item VALUES('Classical Music Overview', 0, 'S1', 5, 'A', 95.6);
INSERT INTO graded_item VALUES('Classical Music Overview', 1, 'S1', 5, 'C+', 79.4);
INSERT INTO graded_item VALUES('Assignment 1', 3, 'class1', 6, 'A+', 100.0);
INSERT INTO graded_item VALUES('Assignment 1', 4, 'class1', 6, 'A+', 100.0);
INSERT INTO graded_item VALUES('Assignment 2', 3, 'class1', 6, 'A', 95.0);
INSERT INTO graded_item VALUES('Assignment 2', 4, 'class1', 6, 'A-', 90.0);
INSERT INTO graded_item VALUES('Assignment 3', 3, 'class1', 6, 'A-', 90.0);
INSERT INTO graded_item VALUES('Assignment 3', 4, 'class1', 6, 'A+', 100.0);
INSERT INTO graded_item VALUES('Assignment 4', 3, 'class1', 6, 'A', 95.0);
INSERT INTO graded_item VALUES('Assignment 4', 4, 'class1', 6, 'A-', 90.0);
INSERT INTO graded_item VALUES('Quiz 1', 3, 'class1', 6, 'A', 95.0);
INSERT INTO graded_item VALUES('Quiz 1', 4, 'class1', 6, 'A-', 90.0);
INSERT INTO graded_item VALUES('Quiz 2', 3, 'class1', 6, 'A+', 100.0);
INSERT INTO graded_item VALUES('Quiz 2', 4, 'class1', 6, 'A+', 100.0);

CREATE TABLE lib(
                    lib_id integer,
                    u_id integer,
                    lib_name varchar(30) not null,
                    view varchar(10),
                    primary key (lib_id, u_id),
                    foreign key (u_id) references user(u_id)
                        on delete cascade);

INSERT INTO lib VALUES (0, 0, 'Advanced Dubstep', 'My courses');
INSERT INTO lib VALUES (1, 0, 'Dubstep Projects', 'Only me');
INSERT INTO lib VALUES (2, 1, 'Personal Projects', 'Only me');
INSERT INTO lib VALUES (3, 1, 'League of Legends Music', 'Public');
INSERT INTO lib VALUES (4, 3, 'Classical Guitar', 'My courses');
INSERT INTO lib VALUES (5, 3, 'Classical Piano', 'My courses');
INSERT INTO lib VALUES (6, 3, 'Classical History', 'My courses');
INSERT INTO lib VALUES (7, 5, 'Rick Roll', 'My courses');
INSERT INTO lib VALUES (8, 5, 'Everything 80s', 'My courses');

CREATE TABLE uses_lib(
                    c_id integer,
                    lib_id integer,
                    primary key (c_id, lib_id),
                    foreign key (c_id) references course(c_id)
                        on delete cascade,
                    foreign key (lib_id) references lib(lib_id)
                        on delete cascade);

INSERT INTO uses_lib VALUES(1, 0);
INSERT INTO uses_lib VALUES(2, 0);
INSERT INTO uses_lib VALUES(5, 4);
INSERT INTO uses_lib VALUES(5, 5);
INSERT INTO uses_lib VALUES(5, 6);
INSERT INTO uses_lib VALUES(6, 7);
INSERT INTO uses_lib VALUES(6, 8);

CREATE TABLE material(
                    m_name varchar(30),
                    lib_id integer,
                    date_created datetime,
                    last_modified datetime,
                    type varchar(15),
                    primary key (m_name, lib_id),
                    foreign key (lib_id) references lib(lib_id)
                        on delete cascade);

INSERT INTO material VALUES('Lecture 1', 0, '2020-08-10 12:33:45', '2020-08-10 12:33:45', 'slides');
INSERT INTO material VALUES('Lecture 2', 0, '2020-08-10 12:45:36', '2020-08-10 12:45:36', 'slides');
INSERT INTO material VALUES('Lecture 3', 0, '2020-08-10 13:01:27', '2020-08-10 13:01:27', 'slides');
INSERT INTO material VALUES('Lecture 4', 0, '2020-08-10 13:35:15', '2020-08-10 13:35:15', 'slides');
INSERT INTO material VALUES('Lecture 1 Video', 0, '2020-09-10 12:35:27', '2020-09-10 12:35:27', 'videos');
INSERT INTO material VALUES('Lecture 2 Video', 0, '2020-09-17 12:24:33', '2020-08-10 12:24:33', 'videos');
INSERT INTO material VALUES('Lecture 3 Video', 0, '2020-09-24 12:27:54', '2020-09-24 12:27:54', 'videos');
INSERT INTO material VALUES('Lecture 4 Video', 0, '2020-10-01 12:19:18', '2020-10-01 12:19:18', 'videos');
INSERT INTO material VALUES('Beats Guide', 0, '2020-08-11 09:24:16', '2020-08-11 09:24:16', 'files');
INSERT INTO material VALUES('How To Drop The Beat', 0, '2020-08-11 09:56:23', '2020-08-11 09:56:23', 'files');
INSERT INTO material VALUES('Bass Drops Of History', 0, '2020-08-11 10:18:37', '2020-08-11 10:18:37', 'files');
INSERT INTO material VALUES('Beats Study', 2, '2020-09-12 17:14:29', '2020-09-17 12:11:45', 'files');
INSERT INTO material VALUES('Rise', 3, '2020-10-01 15:29:18', '2020-10-01 15:29:18', 'videos');
INSERT INTO material VALUES('Legends Never Die', 3, '2020-10-07 14:57:23', '2020-10-07 14:57:23', 'videos');
INSERT INTO material VALUES('Pop/Stars', 3, '2020-10-14 11:14:47', '2020-10-14 11:14:47', 'videos');
INSERT INTO material VALUES('Take Over', 3, '2020-10-21 15:56:21', '2020-10-21 15:56:21', 'videos');
INSERT INTO material VALUES('Basic Strumming', 4, '2019-09-01 08:27:43', '2019-09-01 08:27:43', 'slides');
INSERT INTO material VALUES('Basic Strum Patterns', 4, '2019-09-01 08:33:27', '2019-09-01 08:33:27', 'slides');
INSERT INTO material VALUES('IntroSongs', 4, '2019-09-08 10:57:14', '2019-09-08 10:57:14', 'slides');
INSERT INTO material VALUES('Somewhere Over The Rainbow', 4, '2019-09-17 08:49:23', '2019-09-17 08:49:23', 'videos');
INSERT INTO material VALUES('Riptide', 4, '2019-09-24 08:43:07', '2019-09-24 08:43:07', 'videos');
INSERT INTO material VALUES('Hakuna Matata', 4, '2019-10-01 08:51:02', '2019-10-01 08:51:02', 'videos');
INSERT INTO material VALUES('One Summers Day', 4, '2019-10-08 08:42:54', '2019-10-08 08:42:54', 'videos');
INSERT INTO material VALUES('Mozart', 5, '2019-09-15 08:41:18', '2019-09-15 08:41:18', 'videos');
INSERT INTO material VALUES('Chopin', 5, '2019-09-22 08:39:22', '2019-09-22 08:39:22', 'videos');
INSERT INTO material VALUES('Hisaishi', 5, '2019-09-29 08:47:18', '2019-09-29 08:47:29', 'videos');
INSERT INTO material VALUES('Perahia', 5, '2019-10-05 08:52:01', '2019-10-05 08:52:01', 'videos');
INSERT INTO material VALUES('18th Century', 6, '2019-09-03 08:25:33', '2019-09-03 08:25:33', 'slides');
INSERT INTO material VALUES('19th Century', 6, '2019-09-03 09:04:01', '2019-09-03 09:04:01', 'slides');
INSERT INTO material VALUES('20th Century', 6, '2019-09-04 08:17:18', '2019-09-04 08:17:18', 'slides');
INSERT INTO material VALUES('21st Century', 6, '2019-09-05 08:52:14', '2019-09-05 08:52:14', 'slides');
INSERT INTO material VALUES('Never Gonna Give You Up', 7, '2020-11-01 06:30:07', '2020-11-01 06:30:07', 'videos');
INSERT INTO material VALUES('Never Gonna Let You Down', 7, '2020-11-01 06:44:23', '2020-11-01 06:44:23', 'slides');
INSERT INTO material VALUES('Never Gonna Turn Around', 7, '2020-11-01 07:18:54', '2020-11-01 07:18:54', 'files');
INSERT INTO material VALUES('And Hurt You', 7, '2020-11-01 08:22:06', '2020-11-01 08:22:06', 'files');
INSERT INTO material VALUES('All The 80s', 8, '2020-11-01 09:12:22', '2020-11-01 09:12:22', 'videos');
INSERT INTO material VALUES('Breakfast Club Music', 8, '2020-11-01 09:15:22', '2020-11-01 09:15:22', 'videos');
INSERT INTO material VALUES('Lionel Richie', 8, '2020-11-01 09:30:18', '2020-11-01 09:30:18', 'slides');
INSERT INTO material VALUES('Hairbands', 8, '2020-11-01 09:42:24', '2020-11-01 09:42:24', 'slides');
INSERT INTO material VALUES('Commercial Jingles', 8, '2020-11-01 10:11:12', '2020-11-01 10:11:12', 'slides');
INSERT INTO material VALUES('The Fall Of Disco', 8, '2020-11-01 10:32:47', '2020-11-01 10:32:47', 'slides');

CREATE TABLE game(
                    g_id integer not null,
                    name varchar(30),
                    primary key (g_id));

INSERT INTO game VALUES(0, '80s Music Adventure');
INSERT INTO game VALUES(1, 'Stars Wars: Beat Saber');
INSERT INTO game VALUES(2, 'Learn Guitar Chords!');
INSERT INTO game VALUES(3, 'Learn Piano!');
INSERT INTO game VALUES(4, 'Didgeridoo, You Can Too!');
INSERT INTO game VALUES(5, 'Fiddle Legends');
INSERT INTO game VALUES(6, 'Guitar Hero');
INSERT INTO game VALUES(7, 'Master Mixalot');
INSERT INTO game VALUES(8, 'Slappa Da Bass Mon');
INSERT INTO game VALUES(9, 'Basic Bass');
INSERT INTO game VALUES(10, 'Advanced Basic Bass');
INSERT INTO game VALUES(11, 'Vibe Check');
INSERT INTO game VALUES(12, 'Funschool Kazounds');
INSERT INTO game VALUES(13, 'Instrument Match');
INSERT INTO game VALUES(14, 'Note Pair');
INSERT INTO game VALUES(15, 'Global Groovin');
INSERT INTO game VALUES(16, 'Melody Street');
INSERT INTO game VALUES(17, 'Music Press Distress');
INSERT INTO game VALUES(18, 'Music Darts');

CREATE TABLE uses_game(
                    lib_id integer,
                    g_id integer,
                    primary key (lib_id, g_id),
                    foreign key (g_id) references game(g_id)
                        on delete cascade,
                    foreign key (lib_id) references lib(lib_id)
                        on delete cascade);

INSERT INTO uses_game VALUES(0, 1);
INSERT INTO uses_game VALUES(0, 8);
INSERT INTO uses_game VALUES(0, 10);
INSERT INTO uses_game VALUES(0, 11);
INSERT INTO uses_game VALUES(1, 5);
INSERT INTO uses_game VALUES(4, 2);
INSERT INTO uses_game VALUES(5, 3);
INSERT INTO uses_game VALUES(8, 0);

CREATE TABLE plays_game(
                    u_id integer,
                    g_id integer,
                    save_state integer,
                    primary key (u_id, g_id),
                    foreign key (u_id) references user(u_id)
                        on delete cascade,
                    foreign key (g_id) references game(g_id)
                        on delete cascade);

INSERT INTO plays_game VALUES(0, 2, 10);
INSERT INTO plays_game VALUES(0, 3, 15);
INSERT INTO plays_game VALUES(1, 2, 11);
INSERT INTO plays_game VALUES(1, 3, 17);
INSERT INTO plays_game VALUES(1, 5, 68);
INSERT INTO plays_game VALUES(2, 1, 23);
INSERT INTO plays_game VALUES(2, 8, 14);
INSERT INTO plays_game VALUES(2, 10, 11);
INSERT INTO plays_game VALUES(2, 11, 4);
INSERT INTO plays_game VALUES(3, 1, 24);
INSERT INTO plays_game VALUES(3, 8, 17);
INSERT INTO plays_game VALUES(3, 10, 10);
INSERT INTO plays_game VALUES(3, 11, 15);
INSERT INTO plays_game VALUES(4, 0, 70);
INSERT INTO plays_game VALUES(4, 5, 100);
INSERT INTO plays_game VALUES(4, 11, 300);
INSERT INTO plays_game VALUES(5, 1, 20);
INSERT INTO plays_game VALUES(5, 8, 20);
INSERT INTO plays_game VALUES(5, 10, 9);
INSERT INTO plays_game VALUES(5, 11, 10);
INSERT INTO plays_game VALUES(5, 16, 22);
INSERT INTO plays_game VALUES(5, 17, 54);
INSERT INTO plays_game VALUES(5, 18, 36);

CREATE TABLE smv(
                    smv_id integer not null,
                    name varchar (30),
                    instrument varchar(30),
                    primary key (smv_id));

INSERT INTO smv VALUES(0, 'Synthesia', 'Piano');
INSERT INTO smv VALUES(1, 'Behance', 'Piano');
INSERT INTO smv VALUES(2, 'Midi', 'Piano');
INSERT INTO smv VALUES(3, 'Flat', 'Guitar');
INSERT INTO smv VALUES(4, 'Guitar Score Visualizer', 'Guitar');
INSERT INTO smv VALUES(5, 'Drum Set Visualization', 'Drums');
INSERT INTO smv VALUES(6, 'Didgeridoo Notation', 'Didgeridoo');

CREATE TABLE uses_smv(
                    lib_id integer,
                    smv_id integer,
                    primary key (lib_id, smv_id),
                    foreign key (lib_id) references lib(lib_id)
                        on delete cascade,
                    foreign key (smv_id) references smv(smv_id)
                        on delete cascade);

INSERT INTO uses_smv VALUES(0, 0);
INSERT INTO uses_smv VALUES(0, 5);
INSERT INTO uses_smv VALUES(0, 6);
INSERT INTO uses_smv VALUES(3, 2);
INSERT INTO uses_smv VALUES(4, 4);
INSERT INTO uses_smv VALUES(5, 1);
INSERT INTO uses_smv VALUES(8, 6);

CREATE TABLE smv_file(
                    smv_f varchar(30),
                    lib_id integer,
                    smv_id integer,
                    date_created datetime,
                    last_modified datetime,
                    primary key (smv_f, lib_id),
                    foreign key (lib_id) references lib(lib_id)
                        on delete cascade,
                    foreign key (smv_id) references smv(smv_id)
                        on delete set null);

INSERT INTO smv_file VALUES('Bangarang.midi', 0, 0, '2011-08-24 12:34:57', '2012-02-16 22:18:54');
INSERT INTO smv_file VALUES('ScaryMonstersNiceSprites.midi', 0, 0, '2009-06-24 06:20:18', '2010-10-2 23:45:42');
INSERT INTO smv_file VALUES('Summit.midi', 0, 5, '2012-01-01 18:29:16', '2012-12-16 15:32:44');
INSERT INTO smv_file VALUES('PurpleLamborghini.midi', 0, 6, '2016-01-18 11:20:18', '2016-12-18 23:14:18');
INSERT INTO smv_file VALUES('Rise.midi', 3, 2, '2020-05-23 01:33:25', '2020-11-14 22:10:53');
INSERT INTO smv_file VALUES('PopStars.midi', 3, 2, '2020-04-20 19:55:23', '2020-4-20 19:55:23');
INSERT INTO smv_file VALUES('LegendsNeverDie.midi', 3, 2, '2020-02-16 12:15:34', '2020-03-01 17:54:33');
INSERT INTO smv_file VALUES('HakunaMatata.midi', 4, 4, '2019-01-20 08:37:55', '2019-03-05 09:16:22');
INSERT INTO smv_file VALUES('TheDuckSong.midi', 4, 4, '2019-03-07 08:26:14', '2019-03-09 10:18:45');
INSERT INTO smv_file VALUES('HotelCalifornia.midi', 4, 4, '2019-03-15 08:14:26', '2019-03-27 09:45:55');
INSERT INTO smv_file VALUES('Chopsticks.midi', 5, 1, '2019-03-04 08:54:33', '2019-03-05 09:13:34');
INSERT INTO smv_file VALUES('TwinkleTwinkle.midi', 5, 1, '2019-03-29 09:23:01', '2019-03-29 09:23:01');
INSERT INTO smv_file VALUES('NotARickRoll.midi', 8, 6, '2020-11-25 14:53:18', '2019-12-05 12:54:12');

CREATE TABLE message(
                    msg_id integer,
                    subject varchar(60),
                    primary key (msg_id));

INSERT INTO message VALUES(0, 'Lab Assignment Question');
INSERT INTO message VALUES(1, 'Dubstep Theory Question');
INSERT INTO message VALUES(2, 'Late lab question');
INSERT INTO message VALUES(3, 'Assignment 2 Question');
INSERT INTO message VALUES(4, 'Confusion with Assignment 4');

CREATE TABLE inbox(
                    u_id integer,
                    msg_id integer,
                    primary key (u_id, msg_id),
                    foreign key (msg_id) references message(msg_id)
                        on delete cascade,
                    foreign key (u_id) references user(u_id)
                        on delete cascade);

INSERT INTO inbox VALUES(0, 0);
INSERT INTO inbox VALUES(2, 0);
INSERT INTO inbox VALUES(0, 1);
INSERT INTO inbox VALUES(3, 1);
INSERT INTO inbox VALUES(0, 2);
INSERT INTO inbox VALUES(3, 2);
INSERT INTO inbox VALUES(4, 3);
INSERT INTO inbox VALUES(5, 3);
INSERT INTO inbox VALUES(3, 4);
INSERT INTO inbox VALUES(5, 4);

CREATE TABLE message_chain(
                    submsg_id integer,
                    msg_id integer,
                    sender_id integer,
                    receiver_id integer,
                    content text,
                    time_sent datetime,
                    time_read datetime,
                    primary key (submsg_id, msg_id),
                    foreign key (msg_id) references message(msg_id)
                        on delete cascade,
                    foreign key (sender_id) references user(u_id)
                        on delete set null,
                    foreign key (receiver_id) references user(u_id)
                        on delete set null);

INSERT INTO message_chain VALUES(0, 0, 2, 0,
                            'Hey professor\nI know you''re super famous, but I has a question about the assignment.
                            I was confused about blah blah blah.',
                            '2020-09-15 12:22:54', '2020-09-15 12:27:18');
INSERT INTO message_chain VALUES(1, 0, 0, 2,
                            'I''m never too busy for my students!\nTo answer your question,
                             blah, blah, blah. Does that make sense?',
                            '2020-09-15 12:37:24', '2020-09-15 12:45:33');
INSERT INTO message_chain VALUES(2, 0, 2, 0,
                            'That makes so much sense now! Thanks!',
                            '2020-09-15 12:53:05', '2020-09-15 12:58:13');
INSERT INTO message_chain VALUES(0, 1, 3, 0,
                            'Dear professor,\nI was confused about blah blah blah in the lab assignment.
                            Could you help me?',
                            '2020-09-25 18:33:14', '2020-09-26 08:15:12');
INSERT INTO message_chain VALUES(1, 1, 0, 3,
                            'You might be thinking of it this way. Try thinking about
                            blah blah blah. I hope that helps!',
                            '2020-09-26 08:22:47', '2020-09-26 09:07:49');
INSERT INTO message_chain VALUES(2, 1, 3, 0,
                            'Oh, yeah. That helps! Thank you!',
                            '2020-09-26 09:53:22', '2020-09-26 10:02:01');
INSERT INTO message_chain VALUES(0, 2, 3, 0,
                            'Dear professor,\nI forgot to submit the lab last night because blah blah blah.
                            Is there any way I can still get full credit?',
                            '2020-10-09 07:54:13', '2020-10-09 08:27:18');
INSERT INTO message_chain VALUES(1, 2, 0, 3,
                            'Please see my syllabus for my policies on late assignments.',
                            '2020-10-09 08:31:14', '2020-10-09 08:33:16');
INSERT INTO message_chain VALUES(0, 3, 4, 5,
                            'Hey prof, I was kinda confused about blah blah blah.',
                            '2020-11-11 17:12:56', '2020-11-11 17:26:18');
INSERT INTO message_chain VALUES(1, 3, 5, 4,
                            'Oh! I see! Yes, that can be confusing, but blah blah blah!',
                            '2020-11-11 17:31:14', '2020-11-11 17:34:15');
INSERT INTO message_chain VALUES(2, 3, 4, 5,
                            'Oh! I understand now, thank you!',
                            '2020-11-11 17:43:54', '2020-11-11 17:43:54');
INSERT INTO message_chain VALUES(0, 4, 3, 5,
                            'Hey\nFor assignment 4, are we supposed to blah blah blah
                            or blah blah blah?',
                            '2020-11-22 12:25:16', '2020-11-22 12:57:14');
INSERT INTO message_chain VALUES(1, 4, 5, 3,
                            'Actually, what I meant was blah blah blah! To do blah blah blah you
                            really need to understand blah blah blah. It''s really fundamental
                            to this assignment!',
                            '2020-11-22 12:57:33', '2020-11-22 13:07:18');
INSERT INTO message_chain VALUES(2, 4, 3, 5,
                            'Oh, ok. That makes more sense. Thanks!',
                            '2020-11-22 13:21:06', '2020-11-22 13:26:14');