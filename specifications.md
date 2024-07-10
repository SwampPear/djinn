# installation
1. create Djinn library dir (/Library/Djinn)
2. copy contents of djinn library into /Library/Djinn/djinn
3. create Djinn data dir (/var/db/Djinn)
4. create user settings file (/var/db/Djinn/user.json)
5. create projects dir (/var/db/Djinn)

# djinn new <project name>
1. search to see if project name is in projects dir if it is, error
2. initialize <project name>/data
3. initialize <project name>/settings.json and populate

# djinn start <project name>
1. search to see if project name is in projects dir if not, error
2. open app

# djinn rm <project name>
1. search to see if project name is in projects dir if not, error
2. delete project folder from projects dir
