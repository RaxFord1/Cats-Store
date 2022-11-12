"# web-adaptive" 

Installation steps
1) install conda

2) conda create -n web_adaptive

3) conda activate web_adaptive

4) conda install Flask

5) conda install -c conda-forge flask-sqlalchemy

Init db

1) cd {project_path} 

2) python

3) from main import db

4) db.create_all()

Run server 

1) cd {project_path}

2) python -m main.py