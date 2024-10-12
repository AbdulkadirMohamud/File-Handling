# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

 #  f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

f = open('./files/reading_file_example.txt', 'r')
txt = f.read()
print(type (txt))
print(txt)
f.close()

# output 
<class 'str'>
This is an example to show how to open a file and read.

# opening Files for writing and updating
with open('./files/reading_file_example.txt', 'w') as f: # context manager open('./files/reading_file_example.txt', 'w')
f.write('This is an example to show how to open a file and read.')

# Deleting Files
import as
if as.path.exists('./files/reading_file_example.txt'):
    os.remove('./files/reading_file_example.txt')
else: 
    print('The file does not exist')

    #  File Types
    File with json extension
        
        # dictionary
        person_dct = {
            "name": "Abdulkadir",
            "country": "The Netherlands",
            "city": "The Hague",
            skills: ["Python", "Javascript", "React/Next.js"]
        }
        # changing JSON to Dictionary
         import json
        # JSON 
        person_json = '''{
            "name": "Abdulkadir",
            "country": "The Netherlands",
            "city": "The Hague",
            skills: ["Python", "Javascript", "React/Next.js"]}'''
        
        # changing Dictionary to JSON

        import json
        # python dictionary
        person = {
           "name": "Abdulkadir",
           "country": "The Netherlands",
           "city": "The Hague",
           "skills": ["Python", "Javascript", "React/Next.js"]
        }
    # lets convert it to JSON
        person_json = json.dumps(person)
        print (type(person_json))
        print(person_json)

        # saving as JSON File
        # python dictionary
        person = {
           "name": "Abdulkadir",
           "country": "The Netherlands",
           "city": "The Hague",
           "skills": ["Python", "Javascript", "React/Next.js"]
        }
        with open('./filees/json_examples.json ', 'w'  encoding=  'utf-8' as f:
            json.dump(person, f), ensures_ascii=False, indent=4)
        
        # File with csv Extension

        import csv
        with open('./files/csv_example.csv', 'w', newline='') as f:
           csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv 
           line _count = 0
           for row in csv_reader:
              if line_count == 0:
                 print(f'Column names are {", ".join(row)}')
                 line_count += 1
              else:
                 print(f'\t{row[0]} {row[1]}')
                 line_count += 1

              else:
print(
   f'/t{row[0]} {row[1]} is a Developer. He lives in {row[2]}
   line_count += 1
   print('fNumber of lines {line_count}')
)

# file with xml Extension
<?xml version="1.0"?>
<person gender="male">
  <name>Abdulkadir</name>
  <country>The Netherlands</country>
  <city>The Hague</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>

# file with xlsx Extension
import xlrd
excel_book = xlrd.open_workbook('./files/xlsx_example.xlsx')
print(excel_book.nsheets)
print(excel_book.sheet_names(
    
))
