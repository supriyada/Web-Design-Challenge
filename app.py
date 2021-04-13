import pandas as pd
import os

input_file = os.path.join('Resources', 'cities.csv')
print(input_file)
# creating the dataframe
df = pd.read_csv(input_file)

html_string = """
<html>
  <head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="style.css">
  </head>
  
  <body>
    {table}
  </body>
</html>
"""

# OUTPUT AN HTML FILE
htmlfile = "city_table.html"
with open(htmlfile, "w") as file_out:
    file_out.write(html_string.format(table=df.to_html(classes="table table-hover table-striped table-responsive", border=0,index=False,table_id='city_tab_html')))
    