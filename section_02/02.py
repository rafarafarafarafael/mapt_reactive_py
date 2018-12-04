from rx import Observable
from rx.testing import marbles, TestScheduler

def print_value(value):
    print('{} is the value.'.format(value))

Observable.from_(['abc', 'def', 'ghi']).subscribe(print_value)

def say_hello(name, callback):
    callback('hello {}!'.format(name))

hello = Observable.from_callback(say_hello) # a factory function to create new observables
hello('Rafael').subscribe(print_value) # actually creates an observable
hello('observable').subscribe(print_value) # and then this also creates an observable

Observable.from_list([1, 2, 3]).subscribe(print_value)
Observable.of(1, 2, 3, 'A', 'B', 'C').subscribe(print_value)

test_scheduler = TestScheduler() # used to schedule streams and test the observables like a marble diagram
Observable.from_marbles('---(a1)-(b2)------(c3)|', test_scheduler).subscribe(print_value)
Observable.from_marbles('(a6)---(b5)(c4)|', test_scheduler).subscribe(print_value)

test_scheduler.start() # start the scheduling

test2_scheduler = TestScheduler()
Observable.interval(10, test2_scheduler).take_until(Observable.timer(30)).subscribe(print_value)
test2_scheduler.start()
