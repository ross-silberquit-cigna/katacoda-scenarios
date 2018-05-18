Below are the outlined high level steps of one way to read the contents of a file.

When we look at the csv file, we can see that the headers of the data are stored on the first line of the first.

The first step is to read in the file and then print the first line (the headers) and then the rest of the lines (the data)

<pre class="file" data-filename="app.py" data-target="replace">
# TODO: load in csv file

# TODO: print the first line

# TODO: print the rest of the file
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: load in csv file">
# load in csv file
file_handler = open("export.csv")
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: print the first line">
# print out the first line
header = file_handler.readline()
print(header)
</pre>

Run `python app.py`{{execute}}

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: print the rest of the file">
# print the rest of the csv file
for line in file:
    print(line)
</pre>

Run `python app.py`{{execute}}