First step is read the csv file with Python. Good thing there is a built in module!

<pre class="file" data-filename="app.py" data-target="replace">
import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)

# TODO: 5. learn how to print out every row - first time use readline restart here after reading docs!! theres gotta be a better way!!!

# TODO: redo steps 1-5

# TODO: 6. print out specific field 'state'

# TODO: 7. get count of number of rows where the field 'state' is 'done'

# TODO: 8. print out percentage of done compared to total stories

# TODO: 9. print out percentage of done compared to total stories - realize we need float()

# TODO: 10. graph it!  read docs plotly

# TODO: 11. pip install plotly

# TODO: 12. import plotly & create graph data

# TODO: 13. simple http server

# TODO: 14. run and open browser
</pre>