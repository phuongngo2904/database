select s.name, s.instrument,sf.smv_f, sf.date_created, sf.last_modified from smv s, smv_file sf where s.smv_id= sf.smv_id and sf.lib_id=@libid;