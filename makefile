FILES :=							  \
	.travis.yml						  \
	models.html  					  \
	IDB.log 						  \
	models.py						  \
	tests.py      					  \
    apiary.apib                       \
    .gitignore                        \
    UML.pdf	                          

all:

check:
	@for i in $(FILES);											\
	do															\
		[ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
	done

clean: 
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB.log
	rm -f  tests.out
	rm -rf __pycache__

config: 
	git config -l

test: RunTests.out

models.html: RunModels.out
	pydoc3 -w models

IDB.log: 
	git log > IDB.log

RunModels.out: models.py
	
RunTests.out: tests.py 
	coverage3 run 	--omit=*numpy*	--branch tests.py  >	RunTests.out 2>&1
	coverage3 report -m 						 >> RunTests.out
	cat RunTests.out

