import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
</head>
<body>
    <h1>User Signup</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, username="", password="", verify="", email=""):
        self.response.out.write(build_page("") % {"username":username,
                                                  "password":password,
                                                  "verify":verify,
                                                  "email":email})

    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        v_username = valid_username(username)
        v_password = valid_username(password)
        v_verify = valid_username(verify)
        v_email = valid_username(email)

        #verify all 3 required form fields were filled in correctly
        if not(v_username and v_password and v_verify and v_email):
            self.write_form(username, password, verify, email)
            self.response.out.write("Please fill in the form completely!")
        else:
            self.response.out.write("Thanks, it works!")


def build_page(signup_form):
        header = "<h2>Signup</h2>"
        username_label = "<label>Username:</label>"
        username_input = "<input type='text' name='username' value='%(username)s'/><br>"
        password_label = "<label>Password:</label>"
        password_input = "<input type='password' name='password' value='%(password)s'/><br>"
        verify_label = "<label>Verify Password:</label>"
        verify_input = "<input type='password' name='verify' value='%(verify)s'/><br>"
        email_label = "<label>Email (optional):</label>"
        email_input = "<input type='text' name='email' value='%(email)s'/><br>"
        submit = "<input type='submit'/>"
        form = ("<form action='' method='post'>" +
                username_label + username_input + "<br>" +
                password_label + password_input + "<br>" +
                verify_label + verify_input + "<br>" +
                email_label + email_input + "<br>" +
                submit + "</form>")

        return header + form

def valid_username(username):
    if username:
        #x_username = cgi.escape(username, quote=True)
        return username

def valid_password(password):
    if password:
        #x_username = cgi.escape(username, quote=True)
        return password

def valid_verify(verify):
    if verify:
        #x_username = cgi.escape(username, quote=True)
        return verify

def valid_email(email):
    if email:
        #x_username = cgi.escape(username, quote=True)
        return email


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
