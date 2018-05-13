<pre class="file" data-filename="app.py" data-target="replace">
# Read in csv with a module, print out field names and lines
import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

# print out specific field 'state'

total_done = 0

total = 0

for row in csv:

    total += 1

    for field in csv.fieldnames:

        item = row[field]

        if field == "State":

            if row[field] == "Done":

                total_done += 1

print(total_done)

print(total)

print(float(total_done) / float(total))

# TODO: 8. graph it! read docs plotly
</pre>

Run `python app.py`{{execute}}

Run `pip install plotly --user`{{execute}}