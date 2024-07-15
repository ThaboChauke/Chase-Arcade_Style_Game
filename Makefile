ifeq ($(OS), Windows_NT)
run:
	python home.py

install: requirements.txt
	pip install -r requirements.txt

build: setup.py
	python setup.py build bdist_wheel

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./chase.egg-info" rd /s /q chase.egg-info
else
run:
	python3 home.py

install: requirements.txt
	pip3 install -r requirements.txt

build: setup.py
	python3 setup.py build bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf chase.egg-info
endif