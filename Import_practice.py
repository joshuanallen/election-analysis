# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
# 1st datetime = module ; 2nd datetime = class ; now() = attribute (declares find it for current time)
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Can avoid repetitive module and class naming by declaring a new name when importing
# Import the datetime class from the datetime module.
#import datetime as dt 
#dt now represents datetime module
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# import csv
# import datetime
# import random

# print("csv")
# dir(csv)
# print("int")
# dir(int)
# print("float")
# dir(float)
# print("bool")
# dir(bool)
# print("list")
# dir(list)
# print("tuple")
# dir(tuple)
# print("dict")
# dir(dict)
# print("datetime")
# dir(datetime)
# print("random")
# dir(random)
# print("numpy")
# dir(numpy)
# import os
# dir(os)
# dir(os.path)
# Call in an os.path.join()

# --------------
# joining practice
# Join allows for application of multiple modules on an object using the join() function
# file_to_load = os.path.join("Resources", "election_results.csv")


# opening and writing (3.4.3)
# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")