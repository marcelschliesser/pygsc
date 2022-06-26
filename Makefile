tf-apply:
	terraform -chdir=infrastructure init
	terraform -chdir=infrastructure fmt
	terraform -chdir=infrastructure validate
	terraform -chdir=infrastructure plan
	terraform -chdir=infrastructure apply

run:
	python application/main.py