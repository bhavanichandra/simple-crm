OS = mac
VENV=.venv

ifeq ($(OS), mac)
	PYTHON = $(VENV)/bin/python
	PIP = $(VENV)/bin/pip
else
	PYTHON = $(VENV)/Scripts/python
	PIP = $(VENV)/Scripts/pip
endif

run: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

requirements:
	rm -f requirements.txt
	$(PIP) freeze > requirements.txt

clean:
	find . -type d -name __pycache__ -prune -exec rm -r {} +
	rm -rf .idea
	rm -rf .vscode
	rm -rf logs