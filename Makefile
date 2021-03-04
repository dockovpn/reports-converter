.PHONY: build clean test

all: build

build:
	pyinstaller main.py -F

test:
	pytest

clean:
	rm main.spec
	rm -rf dist
	rm -rf build