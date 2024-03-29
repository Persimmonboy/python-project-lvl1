install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

patch:
	poetry install

	poetry build

	poetry publish --dry-run --username ' ' --password ' '

	python3 -m pip install --user dist/*.whl --force-reinstall
