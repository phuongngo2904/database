select u.fname, m.subject,mc.content, mc.time_sent from user u, message_chain mc, message m where m.msg_id = mc.msg_id and u.u_id=mc.receiver_id and mc.sender_id =@sender;
select u.fname, m.subject,mc.content, mc.time_read from user u, message_chain mc, message m where m.msg_id = mc.msg_id and u.u_id=mc.sender_id and mc.receiver_id =@receiver;