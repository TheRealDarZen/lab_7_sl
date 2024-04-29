import random
import string


class PasswordGenerator:
    def __init__(self, length, charset, count):
        self.length = length
        self.charset = charset
        self.count = count
        self.numOfGenerated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.numOfGenerated >= self.count:
            raise StopIteration

        self.numOfGenerated += 1
        return ''.join(random.choice(self.charset) for _ in range(self.length))

if __name__ == '__main__':
    passwords = PasswordGenerator(10, (string.ascii_letters + string.digits), 5)

    print(next(passwords))

    for password in passwords:
        print(password)

    print(next(passwords))