#!/usr/bin/python3
"""
    Pascal Triangle Function
                            """


def pascal_triangle(input_num):
    """
        Generates/Computes levels of pascal's triangle into list of lists
                                                                        """
    trackArray = [] # Keeps track of current list generated
    pascalArray = []

    for i in range(input_num):
        if len(trackArray) == 0:
            trackArray.append(1) # Append 1 if array is empty
        else:
            temp = []
            for j in range(len(trackArray)):
                if j == 0:
                    temp.append(trackArray[j])
                if j + 1 >= len(trackArray): # Append 1 if last element 
                    temp.append(1)
                else:
                    # Add current and next element
                    temp.append(trackArray[j] + trackArray[j + 1])
            trackArray = temp
        pascalArray.append(trackArray)

    return pascalArray
