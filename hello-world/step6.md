<pre class="file" data-filename="app.py" data-target="replace">
# import the new module
import csv

# load in csv file
file_handler = open("export.csv")

# use the new DictReader class from the csv module we've just read about
csv_reader = csv.DictReader(file_handler)

# print out the headers
print(csv_reader.fieldnames)


# TODO: print out percentage of done compared to total stories

</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: print out percentage of done compared to total stories">
# print out specific field 'state'

total_done = 0
total = 0
for row in csv_reader:
    total += 1
    for field in csv_reader.fieldnames:
        item = row[field]
        if field == "State":
            if row[field] == "Done":
                total_done += 1

print(total_done)

print(total)

print(total_done / total)
</pre>

Run `python app.py`{{execute}}
