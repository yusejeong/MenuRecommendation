def create_session(request, id, pwd):
    request.session['username'] = id
    request.session['password'] = pwd
