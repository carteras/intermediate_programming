def write_file_stuff(filename):
    with open(filename, 'w') as fp:
        for row in range(10):
            for col in range(10):
                fp.write("{},{} ".format(row, col))
            fp.write("\n")


file = "bits_and_bobs.txt"
write_file_stuff(file)

coords = []


def read_file_stuff(filename):
    with open(filename, 'r') as fp:
        for line in fp:
            row = []
            for col in line.split(" "):
                if not col == '\n':
                    row.append(col)
            coords.append(row)


read_file_stuff(file)
