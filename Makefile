all: install run

install: venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python3 main.py

check_code:
	. venv/bin/activate && isort . && black .

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
