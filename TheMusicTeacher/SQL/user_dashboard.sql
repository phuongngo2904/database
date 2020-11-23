SELECT i_id from course where i_id=@user_id;
UPDATE user SET last_login=%s where u_id=@id;