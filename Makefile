hello:
	@echo Hi!

clean-pyc:
	@find . -name "*.pyc" -exec rm -f {} +
	@find . -name "*.pyo" -exec rm -f {} +
	# @find . -name "*.ipynb" -exec rm -f {} +
	@find . | grep -E "__pycache__" | xargs rm -rf
	@find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info