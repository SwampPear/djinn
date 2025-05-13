CC = g++

TARGET = djinn
INCLUDE = include
INCLUDE_PATH = src
SUB_DIR = src src/djinn/core

CFLAGS = -std=c++17 -Wall -I $(INCLUDE) -I $(INCLUDE_PATH) -I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib -lssl -lcrypto

DATA_DIR = $(HOME)/Library/Application\ Support/djinn
EXEC_DIR = /usr/local/bin/

all: $(TARGET)

$(TARGET): main.cpp $(wildcard $(foreach fd, ${SUB_DIR}, $(fd)/*.cpp)) $(wildcard $(foreach fd, ${SUB_DIR}, $(fd)/*.hpp))
	# compile
	$(CC) $(CFLAGS) -o $(TARGET) main.cpp $(wildcard $(foreach fd, ${SUB_DIR}, $(fd)/*.cpp))

	# install executable
	sudo mv ./djinn $(EXEC_DIR)/djinn

	# install prompts
	sudo rm -rf $(DATA_DIR)
	sudo mkdir $(DATA_DIR)
	sudo cp -r prompts $(DATA_DIR)/prompts

clean:
	# clean executable
	$(RM) $(TARGET)
	echo "$(wildcard $(foreach fd, ${SUB_DIR}, $(fd)/*.hpp))"

	# clean app dir
	sudo rm -rf $(APP_DIR)

	# clean data dir
	sudo rm -rf $(DATA_DIR)



	