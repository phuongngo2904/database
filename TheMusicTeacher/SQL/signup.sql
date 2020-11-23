SELECT MAX(u_id) FROM user;
INSERT INTO user VALUES (@id,@username,@email, @fname,@minit,@lname,@dob,@g,@phone,@dc,@ll,@verified,@pw);
SELECT username FROM user WHERE username = @username;