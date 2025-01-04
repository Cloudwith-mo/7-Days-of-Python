# a=7
# b=3
# print(a+b)


# f = open("myfile.txt", "r")
# print(f.read())
# f.close()
 
 
try:
    f = open("myfile.txt", "a+")  # Open file in append mode with read access
    try:
        f.write("Python is great\n")  # Write to the file
        f.seek(0)  # Move file pointer to the beginning
        print(f.read())  # Read the content
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        f.close()  # Ensure the file is closed
except FileNotFoundError:
    print("The file does not exist.")

