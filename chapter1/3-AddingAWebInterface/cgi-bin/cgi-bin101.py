import cgi

form = cgi.FieldStorage()  # parse form data
print('Content-Type: text/html\n')  # hdr plus bland line
print('<title>Reply Page</title>')  # html replay
if 'username' not in form:
    print('<h1>Who you are </h1>')
else:
    print('<h1>Hello <i>%s</i> </h1>' % cgi.html.escape(form['username'].value))
