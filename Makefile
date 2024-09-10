LIB_DIR = $${HOME}/Library/Application\ Support/Djinn/

install:
	# remove outdated
	rm -rf ${LIB_DIR}						# clear old lib

	# init new lib
	mkdir ${LIB_DIR} 						# init lib dir
	cp ./install/djinn ${LIB_DIR}			# copy start script

	# init user
	mkdir ${LIB_DIR}/user
	cp ./install/settings.json ${LIB_DIR}/user/settings.json

	# init projects
	mkdir ${LIB_DIR}/projects				# init projects dir

	# copy prompts
	cp -r ./prompts ${LIB_DIR}/prompts

	# copy env
	cp ./.env ${LIB_DIR}

clean:
	rm ./test/*

run:
	cargo build
	cargo run