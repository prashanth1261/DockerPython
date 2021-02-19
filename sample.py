from flask import Flask

# Print a nice greeting
def say_hello(username = "World"):
    return '<h1>Hello %s!</h1>\n' % username

# Some bits of text for the page
header_text = '''
    <html>\n<head> <title>Docker Python</title> </head>\n<body>'''
instructions = '''
    <h3>Welcome to dockerizing python project using Flask</h3>\n
    <p>The End</p>
    '''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# Elastic Beanstalk looks for an 'application' that is callable by default
application = Flask(__name__)

# Add a rule for the index page
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# Add a rule when the page is accessed with a name appended to the site
# URL
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# Run the application
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run(host="0.0.0.0")