file_name = input("Enter the file name: ")
with open(file_name) as file:
    orig_content = file.read()
print(orig_content)
print()
print("Backup version:")
print()    
with open(file_name+".bak") as file:
    bak_content = file.read()
print(bak_content)
answer = input("Do you want to restore the backup? (Y/N)")
if (answer.lower() == "y"):
    with open(file_name, "w") as outfile:
        outfile.write(bak_content)
    print("Done")
else:
    with open(file_name, "a") as outfile:
        outfile.write(content)