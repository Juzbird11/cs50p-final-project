# Binary Search Algorithm Visualization
Demostrate step by step to reach the target using the binary search algorithm

### Explain Binary Search:
1. Begin by sorting the list of numbers in ascending order. This is a prerequisite for using binary search, as it relies on the list being sorted.
1. Determine the mid-point of the list by taking the average of the highest and lowest values in the list.
1. Compare the target number to the mid-point value. If the target number is less than the mid-point, discard the upper half of the list and repeat step 2 with the remaining lower half. If the target number is greater than the mid-point, discard the lower half of the list and repeat step 2 with the remaining upper half. If the target number is equal to the mid-point, the search is complete and the index of the mid-point is the index of the target number.
1. Repeat steps 2 and 3 with the remaining half of the list until the target number is found or the list is exhausted.

### Program Flow:
To use the program,

* the user first needs to input a list of numbers. The numbers should be separated by commas and entered in randomly **no need to be order**. For example, the user could input "1, 2, 4, 5, 3, 6, 7, 8, 9" as the number list.

* Next, the user inputs the target number they want to find. This can be any number within the range of the number list. For example, the user could input "5" as the target number.

* Once the inputs are provided, the program uses the binary search algorithm to find the target number in the list. Binary search works by repeatedly dividing the list in half until the target number is found or the list is exhausted. At each step, the program outputs the range of the list being searched and the mid-point being compared with the target. This provides the user with a clear understanding of how the binary search algorithm is working to find the target number.

### Requirement and installation:
* First, make sure you have Python 3 installed on your computer. Python 3 is required to run the program.
* Clone the repository `git clone "https://github.com/Juzbird11/cs50Python.git"` to your local machine.
* Navigate to the cloned repository using the cd command. In this case, the repository is named "cs50Python".
* Run the program by entering the command `python project.py` in your terminal while you are in the directory where the "project.py" file is located. This will execute the program in the terminal and produce the desired output.
* To test the program, you can use pytest, a Python testing framework. To do so, enter the command `pytest test_project.py` in your terminal while you are in the directory where the "test_project.py" file is located. This will run the tests in the "test_project.py" file and report the results.

Happy hacking :v:


### About CS50
CS50 is a free course from Harvard University and taught by David J.Malan

Introduction to Programming with Python is the starter course for the new student to learn the programming. I prefer CS50P than CS50x because of using Python. This course guides me to the next level.

Thank you for all CS50.