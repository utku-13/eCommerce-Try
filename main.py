from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import os

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///all_users.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#you cant put this one before 

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

ferrari_pics = ["https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Ferrari_F8_Tributo_Genf_2019_1Y7A5665.jpg/1200px-Ferrari_F8_Tributo_Genf_2019_1Y7A5665.jpg",
                "https://hips.hearstapps.com/hmg-prod/images/roa080120fea-ferrari-5-1598543431.jpg?crop=0.862xw:0.727xh;0,0.168xh&resize=1200:*",
                "https://o.aolcdn.com/images/dims3/GLOB/legacy_thumbnail/1062x597/format/jpg/quality/100/https://s.aolcdn.com/os/ab/_cms/2022/04/05044014/Ferrari-F8-Tributo-front-three-quarter1.jpg"]

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"#login fonksiyonu isminden geliyo dene yine de!

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/ferrari')
def ferrari():
    return render_template('ferrari.html')

@app.route('/porsche')
def porsche():
    return render_template('porsche.html')

@app.route('/bmw')
def bmw():
    return render_template('bmw.html')

@app.route("/ferrari/sale")
def saleferrari():
    return render_template('saleferrari.html', ferrari_pics = ferrari_pics)

@app.route('/porsche/sale')
def saleporsche():
    return render_template('saleporsche.html')

@app.route('/bmw/sale')
def salebmw():
    return render_template('salebmw.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(name=form.name.data,
                         email=form.email.data,
                         password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

@app.route('/log-in',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try: 
            user = db.session.query(Users).filter_by(email=form.email.data).scalar()
            if user.password == form.password.data :
                login_user(user)
                print("User Succesfully logged in!")
            return redirect(url_for('home'))
        except:
            flash("This email has not registered yet!",'error')
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/buy/<string:caruwant>')
def buy(caruwant):
    return render_template('buynow.html', caruwant=caruwant)
    
if __name__ == '__main__':
    app.run(debug=True)