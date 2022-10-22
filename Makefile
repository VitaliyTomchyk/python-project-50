install:
	poetry install

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

update:
	make build
	make publish
	make package-install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest