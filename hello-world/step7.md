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

# TODO: 7. print out percentage of done compared to total stories
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 7. print out percentage of done compared to total stories">
# python is not smart - we need float here

print(float(total_done) / float(total))
</pre>

Run `python app.py`{{execute}}
