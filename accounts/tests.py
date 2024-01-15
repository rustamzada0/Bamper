# from django.test import TestCase

# # Create your tests here.

# import re

# example1 = '+994 55 345 67 89' # True
# example2 = '+994 50 345 67 89' # True
# example3 = '+994 70 345 67 89' # True
# example4 = '+994 77 345 67 89' # True
# example5 = '+994 51 345 67 89' # True
# example6 = '+994 10 345 67 89' # True
# example7 = '+994 99 345 67 89' # True
# example8 = '+994 53 345 67 89' # False
# example9 = '+994 asd 345 67 89' # False
# example10 = '+994 555 345 67 89' # True

# patern = re.compile(r'^\+994 [55|50|70|77|51|10|99] [0-9]{3} [0-9]{2} [0-9]{2}$')

# if patern.match(example8):
#     print('True')
# else:
#     print('False')

import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Örnek kullanım:
email_to_check = "ornek@smail.com"
if validate_email(email_to_check):
    print(f"{email_to_check} geçerli bir e-posta adresidir.")
else:
    print(f"{email_to_check} geçerli bir e-posta adresi değildir.")
