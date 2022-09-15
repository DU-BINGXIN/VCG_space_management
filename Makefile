export PWD=`pwd`
export PYTHONPATH=$PYTHONPATH:$(pwd)
export PYTHON=poetry run python
export PYSEN=poetry run pysen

lint:
	$(PYSEN) run lint

format:
	$(PYSEN) run format
