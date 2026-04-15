.PHONY: create-practice remove-practice reqs

create-practice: reqs
ifndef NAME
	$(error NAME is not defined. Use: make create-practice NAME=your_name)
endif
	mkdir -p $(NAME)
	cp PracticeMakefile $(NAME)/Makefile

remove-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	rm -rf $(NAME)

reqs:
	pipreqs . --force
	git add requirements.txt

