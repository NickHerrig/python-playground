def dangerous():
    raise ValueError('This call failed!')

def safe():
    print('Success!')

def cleanup():
    print('Cleaned up!')

def main():
    '''Description of the function'''

    try:
        safe()
    except ValueError:
        print('Value Error caught!')
    else:
        cleanup()

    try:
        dangerous()
    except ValueError:
        print('Value Error caught!')
    else:
        cleanup()



if __name__=='__main__':
    main()

