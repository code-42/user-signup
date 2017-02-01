import webapp2
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Unit 2 Signup</title>
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
        params = dict(username='', email='', u_error='', p_error='', v_error='', e_error='', password='', verify='')
        page_form = self.build_form(**params)
        page_content = page_header + page_form + page_footer
        self.response.write(page_content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        d = {"username":username, "email":email}
        username = d.get('username',username)
        email = d.get('email',email)

        # initialize error message CONSTANTS
        U_ERROR = ''
        E_ERROR = ''
        P_ERROR = ''
        V_ERROR = ''

        # validators return True or False
        v_username = valid_username(username)
        if v_username == False:
            U_ERROR = " That's not a valid username."

        # if user provide email address it must be valid
        v_email = valid_email(email)
        print(email, v_email)
        if email == '':
            v_email = True

        if v_email == False:
            E_ERROR = " That's not a valid email."

        v_password = valid_password(password)
        if v_password == False:
            P_ERROR = " That wasn't a valid password."

        v_verify = False
        if verify == password:
            v_verify = True
        else:
            V_ERROR = " Your passwords didn't match."

        #print variables to  gae log
        print("d.getUsername == " + d.get('username',username))
        print("d.geteMail == " + d.get('email',email))

        if (v_username == False or v_password == False or v_verify == False or v_email == False):
            #print variables to  gae log
            print("parms == ",username,email,password,verify)
            # pass in username and email make them sticky
            username = d.get('username',username)
            email = d.get('email',email)
            # clear password fields for security
            password = ''
            verify = ''

            page_form = self.build_form(username,email,U_ERROR,P_ERROR,V_ERROR,E_ERROR)
            page_content = page_header + page_form + page_footer
            self.response.write(page_content)
        else:
            # Upon valid user input, your web app should redirect to a welcome page for the user.
            self.redirect("/welcome?username=%(username)s"%d)


    def build_form(self, username, email, u_error, p_error, v_error, e_error, password="", verify=""):
        # The form elements where the user inputs their username, password, password again, and email address
        # must be named "username", "password", "verify", and "email", respectively.
        header = "<h1>Signup</h1>"
        username_label = "<label>Username:</label>"
        username_input = "<input type='text' name='username' value='%(username)s'>"
        username_error = "<span name='u_error' class='error'>%(u_error)s</span><br>"
        password_label = "<label>Password:</label>"
        password_input = "<input type='password' name='password' value=''>"
        password_error = "<span name='p_error' class='error'>%(p_error)s</span><br>"
        verify_label = "<label>Verify Password:</label>"
        verify_input = "<input type='password' name='verify' value=''>"
        verify_error = "<span name='v_error' class='error'>%(v_error)s</span><br>"
        email_label = "<label>Email (optional):</label>"
        email_input = "<input type='text' name='email' value='%(email)s'>"
        email_error = "<span name='e_error' class='error'>%(e_error)s</span><br>"
        submit = "<input type='submit'/>"
        form = "<form action='/' method='post'>" +\
        username_label + username_input + username_error + "<br>" +\
        password_label + password_input + password_error + "<br>" +\
        verify_label + verify_input + verify_error + "<br>" +\
        email_label + email_input + email_error + "<br>" +\
        submit + "</form>"

        return header + form % {"username":username,
                                "password":password,
                                "verify":verify,
                                "email":email,
                                "u_error":u_error,
                                "p_error":p_error,
                                "v_error":v_error,
                                "e_error":e_error}

# form validation begin here
# regex provided by Udacity quiz
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    print("u_re.match == ", USER_RE.match(username))
    if USER_RE.match(username) == None:
        return False
    else:
        return True

def valid_password(password):
    print("p_re.match == ", PASSWORD_RE.match(password))
    if PASSWORD_RE.match(password) == None:
        return False
    else:
        return True

def valid_email(email):
    print("e_re.match == ", EMAIL_RE.match(email))
    # if invalid or empty email match == None so return False
    if EMAIL_RE.match(email) == None:
        return False
    else:
        return True

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        d = {"username":username}
        # This page must include both "Welcome" and the user's username.
        self.response.write("<h2>Welcome, %(username)s!</h2>"%d)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomePage)
], debug=True)
