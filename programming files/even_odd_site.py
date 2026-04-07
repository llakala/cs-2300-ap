# Grab numbers from html file and add header -CF
with open("numbers.html", "w") as f:
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    # Loop 50 times and create html table sorting numbers into even and odd categories -CF
    for i in range(1, 50):
        if i % 2 == 0:
            i.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        if i % 2 != 0:
            i.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    # Close tags for table -CF
    f.write("</table>\n</body>\n</html>")
# Write back to original file
with open("numbers.html") as f:
    print(f.read())
    
