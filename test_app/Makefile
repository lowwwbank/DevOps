CXX = g++
CXXFLAGS = -g -O1

all: main clean
clean:
    rm *.o
main: main.o
    $(CXX) $(CXXFLAGS) $^ -o $@.exe

main.o:
    $(CXX) $(CXXFLAGS) -c main.cpp