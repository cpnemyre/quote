from system.core.model import Model
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()

    def login(self, data):
        query = "SELECT * FROM users WHERE email = :email"
        values = {
        "email" : data['email']
    }
        user_exists = self.db.query_db(query, values)
        print user_exists
        if not user_exists and user_exists[0]:
            return (False, ['Email or password not valid'])

        elif self.bcrypt.check_password_hash(user_exists[0]['password'], data['password']):
            return(True, {'id' : user_exists[0]['id'],
                "name" : user_exists[0]['name']})
            return(False, ["Email or password is not valid"])

    def register(self, data):
        print data
        errors=[]
        if len(data['name']) == 0:
            errors.append("Name required")
        if len(data['alias']) == 0:
            errors.append("Alias required")
        if len(data['email']) == 0:
            errors.append("Email needs to be valid")
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Email format must be valid!')
        if len(data['password']) < 8:
            errors.append("Password must be 8 or more characters")
        if data['password'] != data['confirm_password']:
            errors.append("does not match")

        query  = "SELECT * FROM users WHERE email = :email"
        values = {
        "email" : data['email']
    }
        user_exists = self.db.query_db(query,values)
        print user_exists
        if user_exists and user_exists[0]:
            errors.append("Invalid user")

        if len(errors) > 0:
            return (False, errors)
        # return (False, ['Invalid registration'])

        password = self.bcrypt.generate_password_hash(data['password'])

        query = "INSERT INTO users (name, alias, email, password, date_of_birth, created_at, updated_at) VALUES (:name, :alias, :email, :password, :date_of_birth, NOW(), NOW())"
        values = {
            "name" : data["name"],
            "alias" : data["alias"],
            "email" : data["email"],
            "date_of_birth" : data['date_of_birth'],
            "password" : password

        }

        self.db.query_db(query, values)
        return self.login(data)

    def addQuote(self, data):
        query = "INSERT INTO quotes (author, message, poster_id) VALUES (:author, :message, :poster_id)"
        values = {
                "author" : data['author'],
                "message" : data['message'],
                "poster_id" : data['poster_id']
        }
        posted_quotes = self.db.query_db(query, values)
        print posted_quotes
        return self.db.query_db(query, values)

    def addToList(self, user_id, poster_id):
        query = "INSERT INTO favorites (user_id, quote_id) VALUES (:user_id, :quote_id)"
        values = {
                "user_id" : data['user_id'],
                "poster_id" : data['poster_id']
        }
        return self.db.query_db(query, values)

    def removeFav(self, quote_id, user_id):
        query = "DELETE FROM favorites WHERE quote_id = :quote_id AND user_id = :user_id"
        values = {"quote_id" : data['quote_id'], "user_id" : data['user_id']}
        return self.db.query_db(query)

    def displayFavs(self, id):
        query = ""
        values = {"id" : data['id']}
        return self.db.query_db(query)

    def displayNotFavs(self, id):
        query = ""
        return self.db.query_db(query, values)
