# my_zip.py
def my_zip(*args):
    '''
        zip function written in python
        takes in any number of non indexable iterables
        with the same length
        returns a list of tuples, where each tuple contains
        the i-th element
    '''
    # turn every iterable into an iterator
    itrs = [iter(i) for i in args]
    # if any iterators were made
    if len(itrs):
        while True:
            # return the i-th element
            try:
                yield tuple([next(i) for i in itrs])
            # stop if the end of any iterator was reached
            except StopIteration:
                break
