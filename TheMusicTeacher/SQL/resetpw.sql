UPDATE user SET hashed_password=@hashed_pw where username= @username;
SELECT username FROM user WHERE username = @usname;