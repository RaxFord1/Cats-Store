"# web-adaptive" 

Installation steps

0) install conda from website (https://docs.conda.io/en/latest/miniconda.html)

2) conda create -n web_adaptive

3) conda activate web_adaptive

4) conda install Flask

5) conda install -c conda-forge flask-sqlalchemy

6) conda install pytest


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
