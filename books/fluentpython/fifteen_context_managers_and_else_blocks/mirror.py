import sys

class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        return self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write=self.original_write
        if exc_type is ZeroDivisionError:
            print('Please do no divide by zero!')
            return True

import contextlib
@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please do not divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

def main():
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print('hello world')
        print(what)

    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        1/0
        print('hello world')
        print(what)

    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)



if __name__=='__main__':
    main()

