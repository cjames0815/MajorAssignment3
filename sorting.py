def sort (names, grades, first: int):
    """_Sortss a list of grades from largest to smallest and 
    sorts the list of names according to the order defined by
    the sorted grades_

    Args:
        names : _list of names_
        grades : _list of grades_
        first (int): _the list index at which the sort will begin _
    """    
    
    #Creating  loop counter variables 
    i = 0
    #Setting up j variable
    j = 0
    

    # Storing the smallest index 
    small = 0

    #To move array value
    swap = 0

    #loop through the list as many times as specified by grades
    while (i > 0):
        #setting small equal to grades
        small = grades

        #looping through the list starting with element at grades  -1
        #continue until i reach the first element
        j = grades + 1
        while (j <= first + i):
            #if the value in small is greater than the current grade
            if(names[small] > names[j]):
                #set small equal to the index of the grade
                small = j

            # increment j by 1
            j += 1
            

            #swap the data in i with the data in small 
           
            swap = names

            #set temp to value in small
            names[first - i] = names[small]
            #set value in small to swap
            names[small] = swap

            # increment
            i = i + 1


