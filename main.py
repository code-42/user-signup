import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">.error {color: red;}</style>
</head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_form = self.build_form()
        page_content = page_header + page_form + page_footer
        self.response.write(page_content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

#        v_username = valid_username(username)
#        v_password = valid_username(password)
#        v_verify = valid_username(verify)
#        v_email  = valid_username(email)

        #verify 3 required fields were filled in correctly

#        if (v_username and v_password and v_verify):
        if (username == ""):
            #self.rewrite_form(username, password, verify, email)
            self.response.write(self.build_form(username=username, password=password,verify=verify,email=email))
            #self.redirect("/?error=" + "error message")
        else:
            self.redirect("/welcome")


#signup_form = MainHandler()

    def build_form(self, username="", password="", verify="", email="", error=""):
            header = "<h1>Signup</h1>"
            username_label = "<label>Username:</label>"
            username_input = "<input type='text' name='username' value=''/><span class='error'>%(error)s</span><br>"
            password_label = "<label>Password:</label>"
            password_input = "<input type='password' name='password' value=''/><span class='error'>%(error)s</span><br>"
            verify_label = "<label>Verify Password:</label>"
            verify_input = "<input type='password' name='verify' value=''/><span class='error'>%(error)s</span><br>"
            email_label = "<label>Email (optional):</label>"
            email_input = "<input type='text' name='email' value=''/><span class='error'>%(error)s</span><br>"
            submit = "<input type='submit'/>"
            form = "<form action='/' method='post'>" +\
                username_label + username_input + "<br>" +\
                password_label + password_input + "<br>" +\
                verify_label + verify_input + "<br>" +\
                email_label + email_input + "<br>" +\
                submit + "</form>"

            return header + form % {"username":username, "password":password,
                                      "verify":verify,
                                      "email":email,
                                      "error":error}

def valid_username(username):
    if username:
        x_username = cgi.escape(username, quote=True)
        return x_username

def valid_password(password):
    if password:
        x_password = cgi.escape(password, quote=True)
        return x_password

def valid_verify(verify):
    if verify:
        x_verify = cgi.escape(verify, quote=True)
        #if password == verify:
        return x_verify

def valid_email(email):
    if email:
        x_email = cgi.escape(email, quote=True)
        return x_email

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome ")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomePage)
], debug=True)
