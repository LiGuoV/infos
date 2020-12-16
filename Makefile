test:
	pytest --tb=short

watch-test:
	ls *.py | entr pytest --tb=short
