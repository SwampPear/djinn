CC = g++

TARGET = app
INCLUDE = include
INCLUDE_PATH = src
SUB_DIR = src src/mavan src/mavan/web src/mavan/web/http src/mavan/web/json src/mavan/core src/mavan/core/parser src/mavan/database src/mavan/log src/mavan/model
CLEAN_DIR = src/mavan src/mavan/web src/mavan/web/http src/mavan/web/json src/mavan/core src/mavan/core/parser src/mavan/database src/mavan/log src/mavan/model
#LIB = lib/*

#CFLAGS = -std=c++17 -Wall -shared -L. $(LIB) -I $(INCLUDE) -I $(INCLUDE_PATH)
CFLAGS = -std=c++17 -Wall -w -L. $(LIB) -I $(INCLUDE) -I $(INCLUDE_PATH)

all: $(TARGET)

$(TARGET): $(wildcard *.cpp $(foreach fd, ${SUB_DIR}, $(fd)/*.cpp)) $(wildcard *.hpp $(foreach fd, ${SUB_DIR}, $(fd)/*.hpp))
	$(CC) $(CFLAGS) -o $(TARGET) $(wildcard *.cpp $(foreach fd, ${SUB_DIR}, $(fd)/*.cpp))

clean:
	$(RM) $(TARGET)
	echo "$(wildcard *.hpp $(foreach fd, ${SUB_DIR}, $(fd)/*.hpp))"

style:
	cpplint $(wildcard *.cpp $(foreach fd, ${CLEAN_DIR}, $(fd)/*.cpp)) $(wildcard *.hpp $(foreach fd, ${CLEAN_DIR}, $(fd)/*.hpp))
