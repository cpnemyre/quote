
from system.core.router import routes


routes['default_controller'] = 'Quotes'
routes['POST']['/login'] = 'Quotes#login'
routes['POST']['/register'] = 'Quotes#register'
routes['GET']['/success'] = 'Quotes#success'
routes['POST']['/addQuote'] = 'Quotes#addQuote'
routes['/logout'] = 'Quotes#logout'
routes['/postpage'] = 'Quotes#postpage'
