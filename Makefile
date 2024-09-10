LIB_DIR = $${HOME}/Library/Application\ Support/Djinn/

bootstrap:
	cp ./target/release/djinn ./install

install:
	# remove outdated
	rm -rf ${LIB_DIR}						# clear old lib

	# init new lib
	mkdir ${LIB_DIR} 						# init lib dir
	cp ./djinn.py ${LIB_DIR}				# copy start script

	# init user
	mkdir ${LIB_DIR}/user
	cp ./user.json ${LIB_DIR}/user/user.json

	# init projects
	mkdir ${LIB_DIR}/projects				# init projects dir

	# copy lib
	cp -r ./djinn ${LIB_DIR}/djinn

	# copy prompts
	cp -r ./prompts ${LIB_DIR}/prompts

	# copy env
	cp ./.env ${LIB_DIR}

clean:
	rm ./test/*

try:
	cd test && python3 ${LIB_DIR}djinn.py new t
	cd test && python3 ${LIB_DIR}djinn.py prompt t write me a program that adds two numbers in python

run:
	cargo build
	cargo run