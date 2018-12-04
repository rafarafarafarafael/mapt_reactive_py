from rx import Observable

def print_value(value):
    print('{} is the value.'.format(value))

Observable.from_(['abc', 'def', 'ghi']).subscribe(print_value)
