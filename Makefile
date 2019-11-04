hello:
	@echo Hi!

clean-pyc:
	@echo Starting ...
	@find . -name "*.pyc" -exec rm -f {} +
	@find . -name "*.pyo" -exec rm -f {} +
	@find . | grep -E "__pycache__" | xargs rm -rf
	@find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	@echo Done!

clean-build:
	@echo Starting ...
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	@echo Done!

create-linguistic-features:
	@echo Starting ...
	python -m jupyter nbconvert --ExecutePreprocessor.timeout=-1 --to html --execute "notebooks/Review Linguistics.ipynb"
	@echo Done!

create_env: requirements.txt
	@echo Starting ...
	python3 -m venv "./venv/credenv"
	@echo Environment created. Activating environment ...
	\
	source ./venv/credenv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	which python; \
	python -m spacy download en_core_web_sm; \
	python -m spacy download en_core_web_lg;
	@echo Done!