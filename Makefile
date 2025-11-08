.phony : env html clean

env : environment.yml
	conda env update --name ligo --file environment.yml --prune

html : 
	myst build --html

clean :
	rm -f figures/* 
	rm -f audio/*
	rm -rf _build/*