Next lets print out the rows!

<pre class="file" data-filename="app.py" data-target="replace">
import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

for row in csv:
    print(row)
</pre>