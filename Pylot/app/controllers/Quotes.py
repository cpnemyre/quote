from system.core.controller import *
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)

        self.load_model('Quote')
        self.db = self._app.db

    def index(self):


        return self.load_view('index.html')


    def login(self):
        print request.form
        # validation and login occur in model
        # two options with login: A: successful login -> return redirect '/success' B. return redirect ('/') with errors
        # self.
        possible_member = self.models['Quote'].login(request.form)
        # possible_member will be a tupil with two pieces: piece aka possible_member[0] = True/False that will help show the difference betwen a and b
        # possible_member[1]  = errors or member
        if possible_member[0]:
            session['id'] = possible_member[1]['id']
            session['name'] = possible_member[1]['name']
            return redirect('/success')
        else:
            flash(errors)
            return redirect('/')

    def register(self):
        print request.form
        # first name, last, email, password, confirm psw
        # validation and register occur in model
        # two options: A: successful register -> rredirect (/'success') B. return redirect ('/') with errors.
        possible_member = self.models['Quote'].register(request.form)
        if possible_member[0]:
            session['id'] = possible_member[1]['id']
            session['name'] = possible_member[1]['name']
            return redirect('/success')
        else:
            flash(possible_member)
            return redirect('/')


    def logout(self):
        session.clear
        return redirect('/')

    def success(self):
        return self.load_view('success.html')

    def addQuote(self):

        return redirect('/success')

    def postpage(self):
        return self.load_view('postpage.html')
