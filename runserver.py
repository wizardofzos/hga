import os
from app import app

from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('yourserver.key')
context.use_certificate_file('yourserver.crt')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    print port
    app.run(host='0.0.0.0', port=port, ssl_context=context)
