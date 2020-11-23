select g.g_id, g.name from game g, uses_game ug where g.g_id = ug.g_id and ug.lib_id=@libid;
select g.name, pg.save_state from plays_game pg, game g where pg.g_id=g.g_id and pg.u_id=@user_id;