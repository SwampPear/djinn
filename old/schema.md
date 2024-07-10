+Project
-id int autoinc pk
-name text

+Sprint
-id int autoinc pk
-project_id int fk

+Log
-id int autoinc pk
-sprint_id int fk
-project_id int fk
-type_code varchar(2)
-contents text

+Context
-id int autoinc pk
-content text
