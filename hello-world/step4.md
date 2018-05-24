Run `clear`{{execute}}
<pre class="file" data-filename="app.py" data-target="replace">
# import the new module
import csv

# load in csv file
file_handler = open("export.csv")

# use the new DictReader class from the csv module we've just read about
csv_reader = csv.DictReader(file_handler)

# print out the headers
print(csv_reader.fieldnames)


# TODO: print out specific field 'state'

# TODO: get count of number of rows where the field 'state' is 'done'

# TODO: print out percentage of done compared to total stories

</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: print out specific field 'state'">
# print out specific field 'state'
for row in csv_reader:
    for field in csv_reader.fieldnames:
        if field == "State":
            print(row[field])
</pre>

Run `python app.py`{{execute}}
