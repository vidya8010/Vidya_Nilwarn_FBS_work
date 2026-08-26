import re as r
def email_verification(e):
    patt='^[a-z][a-z0-9]+@[a-zA-Z0-9]+\.[a-z]'
    if r.match(patt,e):
        return True
    else:
        return False

email='vidya123@gmail.com'
print(email_verification(email))
