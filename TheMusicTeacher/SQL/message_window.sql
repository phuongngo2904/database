Select u_id from user where email =@user_email;
Select max(msg_id) from message;
INSERT INTO message values (@msgid,@sub);
Select max(submsg_id) from message_chain;
INSERT INTO message_chain values(@subid,@mid,@senderid,@receiverid,@content,@time_sent,@time_read);
