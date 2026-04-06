#_func.py

def return_info(name, phone, address, email):
    contact_info=f"연락처:{phone}\n이메일:{email}"
    return f"이름:{name}\n{contact_info}\n주소:{address}"

def print_info(name, phone, address, email=""):
    contact_info=f"연락처:{phone}\n이메일:{email}"
    print( f"이름:{name}\n{contact_info}\n주소:{address}")
    
print_info("Aaron","010-5555-5555", "전주")
person=return_info(
    email="hi@ut.ac.kr", phone="010-1111-1111",
    address="교통대학교", name="Aaron"
    )
print()
print(person)