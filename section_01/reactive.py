from rx import Observable

def print_number(x):
    print(f'The number is {x}')

Observable.from_(range(10)).subscribe(print_number)