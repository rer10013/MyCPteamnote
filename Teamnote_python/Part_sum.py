''' Part Sum '''
def subset_sum(x_table, r_target):
    def part_sum(x_table, i=0):
        if i == len(x_table):
            yield 0
        else:
            for s_idx in part_sum(x_table, i + 1):
                yield s_idx
                yield s_idx + x_table[i]

    k = len(x_table) // 2 # divide input
    y_value = list(part_sum(x_table[:k]))
    z_value = [r_target - v for v in part_sum(x_table[k:])]
    y_value.sort() # test of intersection between y_value and z_value
    z_value.sort()
    i = 0
    j = 0
    while i < len(y_value) and j < len(z_value):
        if y_value[i] == z_value[j]:
            return True
        if y_value[i] < z_value[j]: # increment index of smallest element
            i += 1
        else:
            j += 1
    return False