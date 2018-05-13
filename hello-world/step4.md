<pre class="file" data-filename="app.py" data-target="replace">
# TODO: 5. print out specific field 'state'

# TODO: 6. get count of number of rows where the field 'state' is 'done'

# TODO: 7. print out percentage of done compared to total stories

# TODO: 8. print out percentage of done compared to total stories - realize we need float()
</pre>

<pre class="file" data-filename="app.py" data-target="insert" data-marker="# TODO: 5. print out specific field 'state'">
# print out specific field 'state'
for row in csv:
    for field in csv.fieldnames:
        if field == "State":
            print(row[field])
</pre>

Run `python app.py`{{execute}}
