from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder="./resources/html")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    class_type = db.Column(db.String(1), nullable=False)
    gender = db.Column(db.Boolean, nullable=False) # 0 - мальчик 1 - девочка TODO: сделать проверку, что 0 или 1
    available = db.Column(db.Boolean) # бронь 0 - забронирован 1 - свободно TODO: сделать проверку, что 0 или 1

    image = db.Column(db.BLOB)

    color = db.Column(db.String(50), nullable=False) # Окрас

    birthday = db.Column(db.DateTime, nullable=False) # День рождения
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Cat %r>' % self.id

class Kitty(db.Model):
    # маленькое животное
    # id = db.Column(db.Integer, primary_key = True)

    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id', ondelete="CASCADE"), primary_key = True)
    mom = db.Column(db.Integer, db.ForeignKey('cat.id', ondelete="CASCADE"))
    dad = db.Column(db.Integer, db.ForeignKey('cat.id', ondelete="CASCADE"))

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Kitty %r>' % self.id

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    
    gender = db.Column(db.Boolean) # TODO: сделать проверку, что 0 или 1
    
    birthday = db.Column(db.DateTime)
    
    city = db.Column(db.String(50), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

class Booking(db.Model):
    # маленькое животное
    id = db.Column(db.Integer, primary_key = True)

    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    comment = db.Column(db.String(200))

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Kitty %r>' % self.id

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        gender = request.form['gender'] # TODO: сделать проверку, что 0 или 1
        if gender == 'male':
            gender = 0
        else:
            gender = 1
        birthday = datetime.strptime(request.form['birthday'], "%Y-%M-%d") 
        city = request.form['city']
        
        user = User(first_name=first_name, last_name=last_name, email=email, 
            phone_number=phone_number, gender=gender, birthday=birthday, city=city
        )

        print(user)
        print(first_name, last_name, email, phone_number, gender, birthday, city)
        try:
            # TODO: навешать логики, если юзер уже создан
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Couldnt insert {e}'
    
    return render_template('index.html')

@app.route("/login", methods=['POST, GET'])
def login():
    
    return render_template('index.html', task=False)

if __name__ == "__main__":
    app.run(debug=True)