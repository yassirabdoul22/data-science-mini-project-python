PYTHON = python3
MAIN = main

install: 
	pip intall -r requirements.txt

run:
	$(PYTHON) $(MAIN)

clean:
	rm -rf __pycache__
	rm -f .pyc

.PHONY: install run test clean
