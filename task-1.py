len_p=int(input('Введите длину пароля: '))

import string
import random


ch=string.ascii_letters + string.digits

random_par=''.join(random.choices(ch,k=len_p))

print(random_par)
