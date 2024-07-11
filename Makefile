LIB_DIR = $${HOME}/Library/Application\ Support/Djinn/

install:
	mkdir ${LIB_DIR} 						# init lib dir
	cp ./djinn.py ${LIB_DIR}				# copy start script
	mkdir ${LIB_DIR}/user					# init user dir
	cp ./user.json ${LIB_DIR}/user.json		# init user settings
	mkdir ${LIB_DIR}/projects				# init projects dir
	cp -r ./djinn ${LIB_DIR}/djinn			# copy lib

clean:
	rm -rf ${LIB_DIR}
