from YTMT.models import *

def find_user(request):
    # 저장된 session 안의 username을 저장
    id = request.session.get('username')
    # id가 동일한 user객체를 검색하여 생성
    return User.objects.get(username = id)

def create_session(request, id, pwd):
    request.session['username'] = id
    request.session['password'] = pwd
