import random
import string

def create_password(lenght: int = 8, chars: str = string.ascii_letters + string.digits + string.punctuation) -> str:
    return ''.join(random.choice(chars) for _ in range(lenght))

if __name__ == '__main__':
    print(create_password())
    print(create_password(16))
    print(create_password(16, chars=string.ascii_letters + string.digits))
    print(create_password(16, chars=string.digits))
    print(create_password(16, chars=string.ascii_letters))
    print(create_password(16, chars=string.ascii_lowercase))
    print(create_password(16, chars=string.ascii_uppercase))
    print(create_password(16, chars=string.punctuation))
    print(create_password(16, chars=string.hexdigits))
    print(create_password(16, chars=string.octdigits))
    print(create_password(16, chars=string.printable))
    print(create_password(16, chars=string.whitespace))
    print(create_password(16, chars=string.ascii_letters + string.digits + string.punctuation))