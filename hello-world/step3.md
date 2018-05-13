Next lets print out the rows!

<pre class="file" data-filename="app.py" data-target="replace">

# TODO: redo steps 1-4 after reading the docs

import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)

</pre>