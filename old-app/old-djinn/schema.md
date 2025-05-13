+Sprint
-id int autoinc pk

+Log
-id int autoinc pk
-sprint_id int fk
-type_code varchar(2)
-contents text

+Context
-id int autoinc pk
-content text
