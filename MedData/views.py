from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Patient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'None'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/databasename'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def get_current_user():
    if 'user' in session:
        return User.query.filter_by(name=session['user']).first()
    return None

@app.route('/')
def index():
    user = get_current_user()
    return render_template('home.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = User.query.filter_by(name=name).first()
        if user and user.check_password(password):
            session['user'] = user.name
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if User.query.filter_by(name=name).first():
            return render_template('register.html', error="Username already taken.")
        new_user = User(name=name)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    patients = Patient.query.all()
    return render_template('dashboard.html', user=user, allpatient=patients)

@app.route('/addnewpatient', methods=['GET', 'POST'])
def addnewpatient():
    if request.method == 'POST':
        patient_data = {key: request.form[key] for key in request.form}
        new_patient = Patient(**patient_data)
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('addnewpatient.html')

@app.route('/singlepatient/<int:id>')
def singlepatient(id):
    user = get_current_user()
    patient = Patient.query.get(id)
    return render_template('singlepatient.html', single_patient=patient)

@app.route('/fetchone/<int:id>')
def fetchone(id):
    user = get_current_user()
    patient = Patient.query.get(id)
    return render_template('updatepatient.html', user=user, single_patient=patient)

@app.route('/updatepatient/<int:id>', methods=['GET', 'POST'])
def updatepatient(id):
    patient = Patient.query.get(id)
    if request.method == 'POST':
        for field in request.form:
            setattr(patient, field, request.form[field])
        db.session.commit()
        return redirect(url_for('singlepatient', id=id))
    return render_template('updatepatient.html', single_patient=patient)

@app.route('/deletepatient/<int:id>', methods = ["GET", "POST"])
def deletepatient(id):
    user = get_current_user()
    patient = Patient.query.get(id)
    if patient:
        db.session.delete(patient)
        db.session.commit()
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))