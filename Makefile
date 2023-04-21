clean:
	rm -rf dist/
	rm -rf mongo_db_operation.egg-info/
	rm -rf build/
	rm -rf poetry.lock

install_requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

install:
	poetry install

build:
	poetry build



upload:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository pypi dist/* 
