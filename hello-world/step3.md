There's gotta be a better way! And there is, Kevin!

A quick search shows us Python's standard library has a [csv module](https://docs.python.org/2/library/csv.html) that supports reading csv files.

Run `clear`{{execute}}
<pre class="file" data-filename="app.py" data-target="replace">

# TODO: refactor our code

# TODO: use the new DictReader class from the csv module we've just read about

# TODO: print out the headers

# TODO: print out the rows
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: refactor our code">
# import the new module
import csv

# load in csv file
file_handler = open("export.csv")
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: use the new DictReader class from the csv module we've just read about">
# use the new DictReader class from the csv module we've just read about
csv_reader = csv.DictReader(file_handler)
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: print out the headers">
# print out the headers
print(csv_reader.fieldnames)
</pre>

Run `python app.py`{{execute}}

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: print out the rows">
# print out the rows

for row in csv_reader:
    print(row)
</pre>

Run `python app.py`{{execute}}
