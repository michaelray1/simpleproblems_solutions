import numpy as np
def flatten(x):
    #Flattens an arbitrarily nested list, x
    #Assumes all entries are integers less than 1000 digits long

    ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    string_x = str(x)

    flat_list = []

    char_index = 0
    while char_index < len(string_x):
        count = 0
        if (string_x[char_index] != '[') and (string_x[char_index] != ']') and (string_x[char_index] != ' ') and (string_x[char_index] != ','):
            
            for i in np.arange(1000):
                if string_x[char_index+i] in ints:
                    count+=1
                else:
                    break
                
            num = string_x[char_index : char_index+count]
            char_index+=count
            flat_list.append(num)

        else:
            char_index+=1
            
    return flat_list


#Example nested list
y = [[1, 2], [5], 72, [55, 8341, [2,6]], [1, [[11, 0, 3], 43, 9807218]]]
print("flattened {} = ".format(y), flatten(y))
