# Sorting 
Sorting is a college project made for Data Structures II class. This course is given in the Federal University of Maranhão by professor Dalysson João.

## About the project
The main project goal was implementing some famous sorting algorithms. Those algorithms could be implemented in any of the 3 following languages:

* C/C++
* Java
* Python

Each algorithm should pass in 5 testing files (or at least 4 of them, the last one had 1 GB ). The test files were basicly text files. Your code is supposed to print in the screen the list of words sorted by alphabetical order or by it's occurrence number.

**The project must use Linux notation like to run in the terminal!**


### How to run

General usage
```
usage: sort.py [-h] [-a ALGORITHM] [-m METHOD] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -a ALGORITHM, --algorithm ALGORITHM
  -m METHOD, --method METHOD
  -f FILE, --file FILE
```

Sort using Heap Sort by alphabetical order the file named as test1.txt:
```
python3 sort.py -a HeapSort -m alphabetical -f test1.txt
```

#### Working Algorithms by method
* Alphabetical Order
	* Insertion Sort
	* Heap Sort
	* Shell Sort
	* Selection Sort
	* Intro Sort 
* Occurrences Number
	* Insertion Sort
	* Heap Sort
	* Shell Sort
	* Selection Sort
	* Binary Insertion Sort 
	* Intro Sort 
	* Quick Sort