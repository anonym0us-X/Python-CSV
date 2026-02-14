# Now we will learn about the csv.sniffer which is used to detect the format of the CSV file. It can be used to detect the delimeter, quotechar, etc. in a csv file.

import csv

with open('lang.csv', mode = 'r', encoding = 'utf-8', newline = "") as f:
    sample = f.read(1024)
    delimiter = csv.Sniffer().sniff(sample)
    print("Delimiter : ", repr(delimiter.delimiter))
    f.seek(0) # this will move the cursor to the beginning of the file after reading the sample
    row = csv.DictReader(f, dialect=delimiter)
    for r in row:
        print(r)



# output: 
"""
Delimiter :  ','
{'language': 'Python', 'creator': 'Guido van Rossum', 'year': '1991'}
{'language': 'C', 'creator': 'Dennis Ritchie', 'year': '1972'}
{'language': 'C++', 'creator': 'Bjarne Stroustrup', 'year': '1985'}
{'language': 'Java', 'creator': 'James Gosling', 'year': '1995'}
{'language': 'JavaScript', 'creator': 'Brendan Eich', 'year': '1995'}
{'language': 'C#', 'creator': 'Anders Hejlsberg', 'year': '2000'}
{'language': 'Go', 'creator': 'Robert Griesemer; Rob Pike; Ken Thompson', 'year': '2009'}
{'language': 'Rust', 'creator': 'Graydon Hoare', 'year': '2010'}
{'language': 'Ruby', 'creator': 'Yukihiro Matsumoto', 'year': '1995'}
{'language': 'PHP', 'creator': 'Rasmus Lerdorf', 'year': '1995'}
{'language': 'Swift', 'creator': 'Chris Lattner', 'year': '2014'}
{'language': 'Kotlin', 'creator': 'JetBrains', 'year': '2011'}
{'language': 'TypeScript', 'creator': 'Microsoft', 'year': '2012'}
{'language': 'Scala', 'creator': 'Martin Odersky', 'year': '2004'}
{'language': 'Perl', 'creator': 'Larry Wall', 'year': '1987'}
{'language': '1', 'creator': '2', 'year': '3'}
{'language': '4', 'creator': '5', 'year': '6'}
{'language': '8', 'creator': '5', 'year': '7'}
{'language': '12', 'creator': '37', 'year': '26'}
"""