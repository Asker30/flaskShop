from Store import store
from flask import redirect, url_for, request, render_template

BASE_URL = r'/Shop.store'


@store.route('/')
def root_redirect():
    return redirect(url_for('register'))

@store.route(BASE_URL + '/register', methods=['POST'])
def register():
    return render_template('register.html')
