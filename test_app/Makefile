CXX = g++
CXXFLAGS = -g -O1

all: main clean

clean:
    rm -f *.o

main: main.o
    $(CXX) $(CXXFLAGS) $^ -o $@.exe

main.o: main.cpp
    $(CXX) $(CXXFLAGS) -c $^

.PHONY: all clean
