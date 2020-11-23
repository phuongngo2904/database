DELIMITER $$
CREATE PROCEDURE login(
    IN un varchar(25)
)
BEGIN
SELECT u_id, username, hashed_password
    FROM user WHERE username = un;

END $$
DELIMITER ;

DELIMITER $$
	CREATE PROCEDURE check_usernameExists (IN un varchar(25))
BEGIN
	SELECT username FROM user WHERE username = un;
END$$
DELIMITER ;

DELIMITER $$
	CREATE PROCEDURE insert_newUser (
        IN un varchar(25),
        IN em varchar(50),
        IN fn varchar(20),
        IN mi char(1),
        IN ln varchar(20),
        IN db date,
        IN g char(1),
        IN p varchar(10),
        IN pw varchar(40))
BEGIN
	SELECT (MAX(u_id) + 1) INTO @id FROM user;
    SET @currentTime = NOW();
	INSERT INTO user VALUES (@id, un, em, fn, mi, ln, db, g, p, @currentTime, NULL, False, pw);
END$$
DELIMITER ;

DELIMITER $$
	CREATE PROCEDURE update_password (IN un varchar(25), IN pw varchar(40))
BEGIN
	SELECT u_id into @id FROM user WHERE username = un;
	UPDATE user SET hashed_password = pw WHERE u_id = @id;
END$$
DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE update_message(
        IN sub varchar(60),
        IN sender integer,
        IN receiver integer,
        IN content text)
BEGIN
    Select (MAX(msg_id)+1) INTO @msgid from message;
    INSERT INTO message VALUES (@msgid,sub);
    Select (MAX(submsg_id)+1) INTO @submsgid from message_chain;
    SET @currentTime = NOW();
    INSERT INTO message_chain values(@submsgid,@msgid,sender,receiver,content,@currentTime,NULL);

END$$
DELIMITER ;

DELIMITER $$
        CREATE PROCEDURE check_email (IN user_email varchar(50))
BEGIN
    Select u_id from user where email = user_email;
END $$
DELIMITER ;

 DELIMITER $$
    CREATE PROCEDURE inbox_sent(IN sender integer)
BEGIN
    select u.fname, m.subject,mc.content, mc.time_sent from user u, message_chain mc, message m where m.msg_id = mc.msg_id and u.u_id=mc.receiver_id and mc.sender_id =sender;
END $$

DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE inbox_read(IN receiver integer)
BEGIN
    select u.fname, m.subject,mc.content, mc.time_read from user u, message_chain mc, message m where m.msg_id = mc.msg_id and u.u_id=mc.sender_id and mc.receiver_id =receiver;
END $$

DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE teacher_view_course(IN instructor integer)
BEGIN
    select c.c_id,c.c_name,s.sec_id,c.active from course c, section s where c.c_id = s.c_id and c.i_id=instructor;

END $$

DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE student_view_course(IN student integer)
BEGIN
    select c.c_name, s.sec_id, u.fname, c.active from course c, section s, user u, enrolled e
    where c.c_id=s.c_id and e.sec_id=s.sec_id and e.c_id=c.c_id and c.i_id = u.u_id and e.s_id=student;

END $$

DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE dashboard_course(IN userid integer)
BEGIN
    SELECT i_id from course where i_id=userid;

END $$

DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE update_lastlogin(IN userid integer)
BEGIN
    SET @currentTime = NOW();
    UPDATE user SET last_login=@currentTime where u_id=userid;

END $$

DELIMITER ;

