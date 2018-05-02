#### Steps 1-4 jumping in to it without reading docs

import csv
file_handler = open("export.csv")

#### Realize there's an easier way to do it after reading the docs
# Step 1 (again) refactor the code using dictreader

from __future__ import print_function



import csv

file_handler = open("export.csv")

csv = csv.DictReader(file_handler)

print(csv.fieldnames)

####

#### step 6 begin
total_done = 0

total = 0



for row in csv:

    total += 1

    for field in csv.fieldnames:

        item = row[field]

        if field == "State":

            if row[field] == "Done":

                total_done += 1
#### step 6 end

#### step 2 begin
        if field == "Percent Done By Story Count":

            item = "%0.2f%%" % (float(row[field]) * 100)

        print("%s, " % item, end="")

#### step 2 end

    print("\n") # also step 6




#### step 7
print(total_done)

print(total)

print(total_done / total)

#### step 8

print(float(total_done) / float(total))


#### step 10 pip install

#### step 11

from plotly.offline import plot

import plotly.graph_objs as go



labels = ['Done', 'Not Done']

values = [total_done, total - total_done]



trace = go.Pie(labels=labels, values=values)



plot([trace], filename='basic_pie_chart.html')


####
python -m SimpleHTTPServer 8080

#### control c step


