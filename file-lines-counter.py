# Program to Get Line Count of a File
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# first solution
num_of_lines = file_len("my_file.txt")

print(num_of_lines)

# second solution
num_of_lines2 = sum(1 for l in open('my_file.txt'))

assert num_of_lines is num_of_lines2
