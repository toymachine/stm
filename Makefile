PYTHON=python2.7

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.pyo" -exec rm -rf {} \;
	find . -name "*~" -exec rm -rf {} \;
	find . -name ".#*" -exec rm -rf {} \;
	rm _stm.c
	rm -rf build