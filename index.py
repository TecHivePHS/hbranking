print("""
<!DOCTYPE html>
<html>
  <head>
    <title>Update count: 3</title>
  </head>
  <body>
    <!-- (A) JS -->
<script defer src="csv.min.js"></script>
<script defer src="read.js"></script>
 
<!-- (B) PICK CSV FILE -->
<input type="file" accept=".csv" id="demoPick">
 
<!-- (C) GENERATE HTML TABLE HERE -->
<table id="demoTable"></table>
  </body>""")
i = 5
