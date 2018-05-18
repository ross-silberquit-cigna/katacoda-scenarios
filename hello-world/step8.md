<pre class="file" data-filename="app.py" data-target="replace">
# import the new module
import csv

# load in csv file
file_handler = open("export.csv")

# use the new DictReader class from the csv module we've just read about
csv_reader = csv.DictReader(file_handler)

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

print(float(total_done) / float(total))

# TODO: graph it! read docs plotly
</pre>

Run `python app.py`{{execute}}

Run `pip install plotly --user`{{execute}}