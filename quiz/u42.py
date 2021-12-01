
if __name__ == '__main__':
    file_name = input("Enter the file name: ")
    with open(file_name) as infile:
        contents = infile.read()
    with open(file_name+".bak", "w") as outfile:
        outfile.write(contents)