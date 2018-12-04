from rx import Observable

def print_value(value):
    print('{} is the value.'.format(value))

Observable.from_(['abc', 'def', 'ghi']).subscribe(print_value)

def say_hello(name, callback):
    callback('hello {}!'.format(name))

hello = Observable.from_callback(say_hello) # a factory function to create new observables
hello('Rafael').subscribe(print_value) # actually creates an observable
hello('observable').subscribe(print_value) # and then this also creates an observable