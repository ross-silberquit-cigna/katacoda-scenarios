First step is read the csv file with Python. Good thing there is a built in module!

<pre class="file" data-filename="app.py" data-target="replace">
import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)
</pre>

Run `python app.py`{{execute}}