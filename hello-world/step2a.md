First step is read the csv file with Python. Good thing there is a built in module!

<pre class="file" data-filename="app.py" data-target="replace">
import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)

# TODO: redo steps 1-4 after reading the docs

# TODO: 5. print out specific field 'state'

# TODO: 6. get count of number of rows where the field 'state' is 'done'

# TODO: 7. print out percentage of done compared to total stories

# TODO: 8. print out percentage of done compared to total stories - realize we need float()

# TODO: 9. graph it!  read docs plotly

# TODO: 10. pip install plotly

# TODO: 11. import plotly & create graph data

# TODO: 12. simple http server

# TODO: 13. run and open browser
</pre>