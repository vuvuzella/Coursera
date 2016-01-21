"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Shift all elements towards index 0, combining identical values
    """
    # TODO: Remember begin: the following line still modifies "line"
    # arr_line_copy = line
    # TODO: Remember end
    arr_line_copy = []
    i_line_length = len(line)
    # replaced previous line into copying the elements one by one
    for element in line:
        arr_line_copy.append(element)
    # convert empty elements into zeroes
    arr_line_copy = convert_zeroes(arr_line_copy)
    # shift the elements towards index 0
    arr_line_copy = shift_elements(arr_line_copy)
    # Merge two elements with the same value.
    # Multiply the value by two
    # change the next identical element to zeroes
    # perform another shift of elements towards index 0
    # TODO: make this into a seperate function
    for index in range(i_line_length - 1):
        if arr_line_copy[index] == arr_line_copy[index + 1]:
            arr_line_copy[index] *= 2
            arr_line_copy[index + 1] = 0
            arr_line_copy = shift_elements(arr_line_copy)

    return arr_line_copy

def convert_zeroes(line):
    """
    Convert empty elements into zeroes
    """
    arr_line_copy = line
    for index in range(len(arr_line_copy)-1):
        if not arr_line_copy[index]:
            arr_line_copy[index] = 0

    return arr_line_copy

# TODO: Optimize shifting algorithm
def shift_elements(line):
    """
    shift elements towards index 0
    """
    arr_line_copy = line
    i_temp = 0
    i_line_length = len(line)
    for index in range((i_line_length - 1)):
        # if element is zero, scan succeeding elements until a non-zero is found
        if arr_line_copy[index] == 0:
            i_scan_index = index
            while i_scan_index < (i_line_length):
                if arr_line_copy[i_scan_index] > 0:
                    # swap with non-zero element
                    i_temp = arr_line_copy[index]
                    arr_line_copy[index] = arr_line_copy[i_scan_index]
                    arr_line_copy[i_scan_index] = i_temp
                    break
                else:
                    # do nothing here
                    pass
                i_scan_index += 1
            if i_scan_index == i_line_length:
                # empty line, exit with break
                break
            else:
                # do nothing for now
                pass
        else:
            # do nothing for now.
            pass
    # return the shifted elements array
    return arr_line_copy
