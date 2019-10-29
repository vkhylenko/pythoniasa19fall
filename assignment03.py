import string
import random

def task01(start, end):
    print(','.join(str(i) for i in range(start, end + 1) if i % 7 ==0 and i % 5 !=0))


def task02(x, y):
    return[[i*j for j in range(y)] for i in range(x)]

def task03(password):
    '''
    >>> task03('ABd1234@1')
    True
    >>> task03('a F1#')
    False
    >>> task03('2w3E*')
    False
    >>> task03('2We3345')
    False
    '''
    return (6 <= len(password) <= 12
            and any('a' <= s <= 'z' for s in password)
            and any('A' <= s <= 'Z' for s in password)
            and any('0' <= s <= '9' for s in password)
            and any (s in '#@$' for s in password))


def task04():
    '''
    >>> task03(task04())
    True
    '''
    symb = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    password = [None]*random.randint(6, 12)
    password[0] = random.choice(string.ascii_lowercase)
    password[1] = random.choice(string.ascii_uppercase)
    password[2] = random.choice(string.digits)
    password[3] = random.choice('@#!')
    for i in range (4, len(password)):
        password[i] = random.choice("".join(symb))

    random.shuffle(password)
    fin = ''.join(password)
    return fin

print(task04())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

