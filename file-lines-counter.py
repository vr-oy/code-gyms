# Program to Get Line Count of a File
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

num_of_lines = file_len("my_file.txt")

print(num_of_lines)
