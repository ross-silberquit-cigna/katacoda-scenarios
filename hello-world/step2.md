First step is read the csv file with Python. Good thing there is a built in module!

<pre class="file" data-filename="app.py" data-target="replace">
# TODO: 1. import csv

# TODO: 2. load in csv file

# TODO: 3. print out the first line

# TODO: 4. print the rest of the file
</pre>
<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 1. import csv">
# import the csv module
import csv
</pre>
<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 2. load in csv file">
# load in csv file
file = open("export.csv")
</pre>
<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 3. print out the first line">
# print out the first line
header = file.readline()
print(header)
</pre>
<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 4. print the rest of the file">
# print the rest of the csv file
for line in file.readline():
    print(line + "\n")
</pre>


Run `python app.py`{{execute}}