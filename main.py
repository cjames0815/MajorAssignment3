from sorting import *

#Setting up main
def main():
    """_Prompts user for input and calls selection sort function_
    """    
    #Setting up local variables to store the lists
    # names, grades, first

    #Setting up list
    names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felecia', 'Carl']
    grades = ['A', 'B','D', 'C','A','F','B']
    first = 0

    #Display the orginal unsorted array
    for i in names:
        print(i, end= "")

    #Call sort method
    #Names is passed by reference
    sort(names, grades, first)

    print()

    #Display the sorted array
    for i in names:
        print(i, end= "")

if __name__ == "__main__":
    main()