from flask import Flask,request,jsonify,redirect,url_for, session
from flask import render_template, redirect
from OpenSSL import SSL

import datamodel
import battlenet

app = Flask(__name__)

app.debug = True
app.secret_key = 'A0Zr98j/3yX R~X90Zr98j/3yX R8j/3yX R~XHH!jmNaHH!jmN]LWX/,?RT'

from battlenet.oauth2 import BattleNetOAuth2
@app.route('/login')
def login():
    bnet = BattleNetOAuth2(key='2nhugzjhnbuzat9qpc8zmscbgcygq5af',
            secret='zPxNfy8aHV8fzeC6KxbMet8T2RtyPQvQ',
            region='eu',
            scope='wow.profile',
            redirect_uri='http://localhost:5000/token',
    )
    app.logger.warning(session)
    url, state = bnet.get_authorization_url()
    app.logger.warning(state)
    # save state somewhere for checking the redirect response against
    session['state'] = state
    app.logger.warning(session)
    app.logger.warning(url)
    return redirect(url)

@app.route("/token", methods=['GET','POST'])
def token():
    if request.args.get('code'):
        if request.args.get('state') and session['state']:
            if request.args.get('state') == session['state']:
                bnet = BattleNetOAuth2()
                data = bnet.retrieve_access_token(request.args.get('code'))

@app.route("/")
def index():
    return render_template('pages/home.html')

# Catch all :)
cool404s = [
		'WR2FvrU-NIM',
		'wNVCJj642n4',
		'dn_CjkNtl6s',
		'f5IRI4oHKNU',
		]
import random
@app.route('/<path:path>')
def catch_all(path):
	return render_template('pages/404.html', video=random.choice(cool404s))
