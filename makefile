test.out: test.py
	coverage run --branch test.py > test.out 2>&1
	coverage report -m >> test.out 
	cat test.out
clean:
	rm -f test.out
test: test.out
