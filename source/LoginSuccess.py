def solution(id_pw, db):
    login_db = {input_data[0]: input_data[1] for input_data in db}
    ID = id_pw[0]
    Password = id_pw[1]
    if ID in login_db:
        return 'login' if login_db[ID] == Password else 'wrong pw'
    else :
        return 'fail'
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120883