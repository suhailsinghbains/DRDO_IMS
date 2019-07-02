#https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/


from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'ThisisthePassword'
db = SQLAlchemy(app)

class Auth(db.Model):
    empId = db.Column(db.String(16), db.ForeignKey('employees.empId'), primary_key=True)
    password = db.Column(db.String(16), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False)
    def __init__(self, empId, password):
        self.empId = empId
        self.password = password
        self.admin = False
    
    def __repr__(self):
        return '<User>' +self.empId+self.password+str(self.admin)

class Employees(db.Model):
    group = db.Column(db.String(20), nullable=False)
    empId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    cpu = db.Column(db.String(16), db.ForeignKey('cpu.tagId'))
    ram = db.Column(db.String(16), db.ForeignKey('ram.tagId'))
    psu = db.Column(db.String(16), db.ForeignKey('psu.tagId'))
    display = db.Column(db.String(16), db.ForeignKey('display.tagId'))
    keyboard = db.Column(db.String(16), db.ForeignKey('keyboard.tagId'))
    mouse = db.Column(db.String(16), db.ForeignKey('mouse.tagId'))
    ups = db.Column(db.String(16), db.ForeignKey('ups.tagId'))
    printer = db.Column(db.String(16), db.ForeignKey('printer.tagId'))
    scanner = db.Column(db.String(16), db.ForeignKey('scanner.tagId'))
    messages = db.Column(db.String(16))
    code = db.relationship("Auth", backref="emp")
    def __init__(self, empId, name, group, dob, address):
        self.empId = empId
        self.name= name
        self.group = group
        self.dob = dob
        self.address = address
    def __repr__(self):
        return str({"empId": self.empId, "name": self.name, "group": self.group, "dob": self.dob,
            "address": self.address, "cpu": self.cpu, "ram": self.ram,
            "psu": self.psu, "display": self.display, "keyboard": self.display, "mouse": self.mouse,
            "ups": self.ups, "printer": self.printer, "scanner": self.scanner, "messages": self.messages})

class Cpu(db.Model):
    # tagId = db.relationship("Employees", uselist=False, back_populates="cpu")
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="cpu_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Ram(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="ram")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="ram_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Psu(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="psu")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="psu_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Display(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="display")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="dis_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Ups(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="ups")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="ups_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Scanner(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="scanner")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="sca_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Printer(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="printer")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="pri_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Keyboard(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="keyboard")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="key_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Mouse(db.Model):
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    # tagId = db.relationship("Employees", uselist=False, back_populates="mouse")
    name = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    gen = db.Column(db.String(10), nullable=False)
    remarks = db.Column(db.String(50), nullable=False)
    link = db.relationship("Employees", backref="mou_emp")
    def __init__(self, tagId, name, model, gen, remarks):
        self.empId = tagId
        self.name= name
        self.model = model
        self.gen = gen
        self.remarks = remarks

class Messages(db.Model):
    # tagId = db.relationship("Employees", uselist=False, back_populates="cpu")
    tagId = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(10), nullable=False)
    messages = db.Column(db.String(100), nullable=False)
    # link = db.relationship("Employees", backref="mes_emp")
    def __init__(self, tagId, title, messages):
        self.tagId= tagId
        self.title= title
        self.messages = messages
    def __repr__(self):
        return str({"tagId": self.tagId, "title": self.title, "messages": self.messages})

db.create_all()
db.session.commit()
@app.route('/test', methods=['GET'])
def test():
    print(Auth.query.all())
    print(Employees.query.all())
    return 'Testing'

@app.route('/deleteAll', methods=['GET'])
def delete():
    Auth.query.deleteAll()
    Employees.query.deleteAll()
    return 'Delete All'

@app.route('/', methods=['GET'])
def index():
    # results =  Auth.query.all()
    # print(results)
    # if(session['userId'] = userId)
    if(session=={}):
        return redirect('/signIn')
    else:
        return redirect('/dashboard')

@app.route('/signUp', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        #Get Details from the post
        userId = request.form['userId']
        password = request.form['password']
        cfmpassword = request.form['cfmpassword']
        if(cfmpassword==password):
            auth = Auth.query.filter_by(empId = userId).first()
            if(auth == None):
                authUser = Auth(userId, password)
                emp = Employees(empId=userId)
                db.session.add(authUser)
                db.session.add(emp)
                db.session.commit()
                #Below Line for the User Session
                session['userId'] = userId
                session.modified = True
                # Add Notification to show that I am getting signed up and signing in.
                # http://flask.pocoo.org/docs/0.12/patterns/flashing/
                return redirect('/')
            else:
                # Add Notification to show that 'Sorry, UserId already exists, please Sign In'
                return redirect('/signIn')
        else:
            # Add Notification to show that 'Sorry, Passwords do not match'
            return 'Sorry, Passwords do not match'
    else:
        #Go to the SignUp Page
        return render_template('SignUp/index.html')

@app.route('/signIn', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        userId = request.form['userId']
        password = request.form['password']
        auth = Auth.query.filter_by(empId = userId).first()
        if(auth != None):
            if(auth.password == password):
                session['userId'] = userId
                session.modified = True
                # Add Notification to show that I am getting signed up and signing in.
                # http://flask.pocoo.org/docs/0.12/patterns/flashing/
                return redirect('/dashboard')
            else:
                # Add Notification to show that 'Sorry, Passwords do not match'
                return 'Sorry, Passwords do not match'
        else:
            # Add Notification to show that 'Sorry, UserId doesn't exist, please Sign Up'
            return redirect('/signUp')
    else:
        #Go to the SignUp Page
        return render_template('SignIn/index.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        arr = request.form['js_data'].split(',')
        emp = Employees.query.get_or_404(arr[0])
        emp.name=arr[1]
        emp.group=arr[2]
        emp.dob=arr[3]
        emp.address=arr[4]
        db.session.commit()
        print(emp)
        return str(emp)
        # return render_template('Dashboard/index.html', data=emp)
        # return redirect('/dashboard')
    else:
        if(session=={}):
            return redirect('/')
        else:
            emp = Employees.query.filter_by(empId=session['userId']).first()
            print(emp)
            return render_template('Dashboard/index.html', data=emp)

@app.route('/messages', methods=['POST', 'GET'])
def messages():
    if request.method == 'POST':
        recipient = request.form['recipient']
        title = request.form['title']
        content = request.form['content']
        # Check if the userId exists or not

        newid = str(int(Messages.query.all()[-1].tagId)+1)
        msg= Messages(newid, title, content)
        emp = Employees.query.get(recipient)
        emp.messages= emp.messages+','+ newid
        print(Employees.query.all())
        # Get the empId and references it
        db.session.add(msg)
        db.session.commit()
        # print(Messages.query.all())
        # print (title, content, recipient)
        return redirect('/messages')
    else:
        #Go to the Messages Page
        emp = Employees.query.filter_by(empId=session['userId']).first().messages
        tags=emp.split(',')
        messages='['
        for tag in tags:
            print(tag)
            if(messages=='['):
                messages+=str(Messages.query.filter_by(tagId=tag).first())
            else:
                messages=messages+','+str(Messages.query.filter_by(tagId=tag).first())
        messages+=']'
        # print(eval(messages.split('"')[0]))
        return render_template('Messages/index.html', msg=eval(messages.split('"')[0]))

@app.route('/signOut', methods=['GET'])
def signOut():
    session.pop("userId", None)
    # cookie remove and go to '/'
    # return('SignOut/index.html')
    return redirect('/signIn')

# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'


# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'

#     else:
#         return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
