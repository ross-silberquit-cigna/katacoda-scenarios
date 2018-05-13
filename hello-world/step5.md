<pre class="file" data-filename="app.py" data-target="replace">
# Read in csv with a module, print out field names and lines
import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)

# TODO: 6. get count of number of rows where the field 'state' is 'done'

# TODO: 7. print out percentage of done compared to total stories

# TODO: 8. print out percentage of done compared to total stories - realize we need float()
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 6. get count of number of rows where the field 'state' is 'done'">
# print out specific field 'state'
total_done = 0
for row in csv:
    for field in csv.fieldnames:
        if field == "State":
            if row[field] == "Done":
                total_done += 1
print(total_done)
</pre>

Run `python app.py`{{execute}}
