First step is read the csv file with Python. Good thing there is a built in module!

<pre class="file" data-filename="app.py" data-target="replace">
import csv
</pre>

<pre class="file" data-filename="app.py" data-target="clipboard">
file_handler = open("export.csv")
</pre>

<pre class="file" data-filename="app.py" data-target="clipboard">
csv = csv.DictReader(file_handler)
</pre>

<pre class="file" data-filename="app.py" data-target="clipboard">
print(csv.fieldnames)
</pre>
