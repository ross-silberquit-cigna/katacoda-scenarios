There's gotta be a better way! And there is, Kevin!

<pre class="file" data-filename="app.py" data-target="replace">

# TODO: redo steps 1-4 after reading the docs

import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)

</pre>

Run `python app.py`{{execute}}