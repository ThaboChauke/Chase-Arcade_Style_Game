ifeq ($(OS), Windows_NT)
runGame:
	python home.py

dependencies: requirements.txt
	pip install -r requirements.txt

build: setup.py version
	python setup.py build bdist_wheel

version:
	@echo $(shell git describe --tags --always --dirty) > version.txt

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./chase.egg-info" rd /s /q chase.egg-info
else
runGame:
	python3 home.py

dependencies: requirements.txt
	pip3 install -r requirements.txt

build: setup.py
	python3 setup.py build bdist_wheel

version:
	@echo $(shell git describe --tags --always --dirty) > version.txt 

clean:
	rm -rf build
	rm -rf dist
	rm -rf chase.egg-info
endif
