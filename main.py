import csv

"""--------------------------------------------------------------------------------------------"""

# open the CSV file for reading
with open('lang.csv', mode = 'r', encoding= 'utf-8') as f:
    for row in csv.reader(f):
        print(row)

# The above code will read the CSV file and print each row in the CSV as a list.

"""-----------------------------------------------------------------------------------------------------------"""

# now we will read the CSV file and print the results in more readable format using csv.DictReader

with open('lang.csv', mode = 'r', encoding = 'utf-8') as f:
    for row in csv.DictReader(f):
        print(row["language"])

# The code above will read the CSV file and print only the language column of the CSV file. Also notice that the header of the column is not printed in the DIctReader.

"""-----------------------------------------------------------------------------------------------------------"""

# Now enough of reading we will now write to the CSV file using csv.writer and the various modes of writing to a file.

data = [[1,2,3], [4,5,6]]

with open('lang-for-write.csv', mode = 'w', encoding = 'utf-8') as f:
    w = csv.writer(f)
    w.writerows(data)


# The above code will write to the CSV file, BUT REMEMBER we have choosen to write in 'w' mode which will overwrite the existing file meaning that the earlier data will be lost and the new data will be added to the file.
# Also the data written will be having multiple newline characters in between the wors because we did not specify the newline character in the open statement.


# Now lets see the way to not use the extra newline char which by default is addedin the csv.write method
data = [[1,2,3], [4,5,6]]

with open('lang-for-write-newline.csv', mode = 'w', encoding = 'utf-8', newline = "") as f:
    w = csv.writer(f)
    w.writerows(data)



'''For the output of these two and difference please check the lang-for-write.csv and lang-for-write-newline.csv files.'''


"""-----------------------------------------------------------------------------------------------------------"""

# Now let us write to the file in 'a' mode which will append the data to the existing file instead of overwriting it.
data = [[1,2,3], [4,5,6]]

with open('lang.csv', mode = 'a', encoding = 'utf-8', newline = "") as f:
    w = csv.writer(f)
    w.writerows(data)


"""-----------------------------------------------------------------------------------------------------------"""

# Now similar to the DictReader we have a DictWriter which will write the data in the form of a dictionary to the CSV file.
data = [{'language': 8,"creator": 5,'year':7}, 
        {'language':12, 'creator':37,'year':26}]

with open('lang.csv', mode = 'a', encoding = 'utf-8', newline = "") as f:
    w = csv.DictWriter(f, fieldnames=['language', 'creator', 'year'])
    # w.writeheader() # this line will add the header to the CSV file, if you do not want to add the header/ already have header then remove it
    w.writerows(data)

"""-----------------------------------------------------------------------------------------------------------"""

# Now we will learn about the csv.sniffer which is used to detect the format of the CSV file. It can be used to detect the delimeter, quotechar, etc. in a csv file.

