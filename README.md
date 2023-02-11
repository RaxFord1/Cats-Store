"# web-adaptive" 

Installation steps

*With Conda:*

0) install conda from website (https://docs.conda.io/en/latest/miniconda.html)

2) conda create -n web_adaptive

3) conda activate web_adaptive

4) conda install Flask

5) conda install -c conda-forge flask-sqlalchemy

6) conda install pytest

7) conda install pyjwt

*With venv*

1) pip install Flask

2) pip install flask-sqlalchemy

3) pip install pytest

4) pip install pyjwt


Init project and db

0) git clone https://github.com/RaxFord1/web-adaptive.git

1) cd {project_path} 

2) python

3) from main import db

4) db.create_all()

5) exit()


Run server 

1) cd {project_path}

2) python -m main.py
