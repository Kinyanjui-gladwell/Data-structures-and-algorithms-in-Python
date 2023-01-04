"""Working with text files."""
#writing to an empty file
file_name = 'pi_digits.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.")

# writing multiple lines
file_name = 'pi_digits.txt'
list_of_lines = ['I love programming.\n', 'I love programming.\n', 'I love programming.\n']
with open(file_name, 'w') as file_objects:
    file_objects.writelines(list_of_lines)

#Appending to an existing file
file_name = 'pi_digits.txt'
list_of_lines = ['I love gaming.\n', 'I love cooking.\n', 'I love dining.\n']
with open(file_name, 'a') as fp:
    fp.writelines(list_of_lines)

#Reading entire content of file
with open('pi_digits.txt') as file_objects:
    contents = file_objects.read()
    print(contents)

#Reading line by line
with open('pi_digits.txt') as fp:
    content_list = fp.readlines() #readlines stores lines in a list
    for content in content_list:
        print(content)
