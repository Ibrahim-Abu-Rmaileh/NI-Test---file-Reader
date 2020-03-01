


NUMBERS_DECODING={ 63: 0, 6: 1, 91: 2, 79: 3, 102: 4, 109: 5, 125: 6, 7: 7, 127: 8, 111: 9, 0: ' ' }


def converting_from_7segment_to_decimal(filename):

    #
    # aggregate_four_lines=""
    # with open(filename) as f:
    #     for line in f:
    #         aggregate_four_lines+=line
    #         if line=='\n':
    #             one_line_stored_in_array = []
    #             one_line_stored_in_array.append(aggregate_four_lines)
    #             print(one_line_stored_in_array)

    with open(filename) as f:
        for line in f:
            # print(line)
            one_line_stored_in_array=[]
            one_line_stored_in_array.append(line)
            print(one_line_stored_in_array)



converting_from_7segment_to_decimal("input_Q1a.txt")