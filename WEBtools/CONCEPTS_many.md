## numpy as np:

### TO ADD PICTURES TO Files.md:

''' You need to type the descriptive names, using this simple syntax:
![Description of the image] (image-link.jpg) '''

### TO ADD PICTURES TO Files.html:

''' By using the image tag:
<img src="tartaria-map.jpg" alt="Ancient Map of Tartaria" style="max-width:100%;"> '''

### LANGUAGE file.MJML:

### TABLES IN FILES.HTML:

They are usuful to set emails and images only. A table will be start by a tag table: <table> ... </table>

# It will cover up all the content within the table tag.

# tag block.

# Common attributes and events.

# Self attribute: summary=

"text" that allows a description the table content to websearch and accesibility.

## "BORDER" atributte.

(it displays how our table looks like).

# Tag <tr> ...

</tr> or table row: it displays that there will be a row. It will have as many rows as table need.

<table> //There will be a table displays. And within this table we'll have: if our chart has to have 3 rows then we will have 3 tags <tr>
<tr>Age</tr> 
<tr>Sex</tr>
<tr>Name</tr>

### TAG <th> ... </th>,

It stands for table head: This tag defines a specific CELL on the table. The code is written vertically(in a list), but the result is horizontal.

<tr>
<th>Age</th>
<th>Name</th>
<th>Sex</th> 
</tr>

# OR

<tr><th>Age</th><th>Name</th><th>Sex</th></tr>; but this mode is not used by developers due to better syntax structure by doing it on the vertical form.

### Tag caption, <td> ...

</td>: the web engines will use it to display the title on the table. And for us, the developers, we will use it to describe in text the table's content- title.

<table border="5">
<tr align="center">
<td>PERSONAL INFORMATION</td></tr>
<tr><th>Age</th></tr>
<tr><th>Name</th></tr>
<tr><th>Sex</th></tr>
</table>

### To see how this table looks like, press COMMAND+K, then let go and press V.This open a live preview on the side of your screen.

### DOCKER

When isntalling something on my debian environmnent terminal, remember to type first "apt". As in this example: apt-get update, or apt-get install -y python3 (and press enter).

Code Repository (GITHUB)

# WTP

# WSL

## TO ADD IMAGES IN A FILE.MD

![Alt text](URL or file path)
