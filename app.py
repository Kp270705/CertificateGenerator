from flask import Flask, render_template, jsonify, request, flash, redirect, session
from werkzeug.utils import secure_filename

import asyncio
import os, uuid, bcrypt


from PythonTasksScripts.ProcessData import ProcessData
from db.extensions import db, migrate 
from db.AuthDb import User 


UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}


app=Flask(__name__)
# ============================

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)  # Initialize app with db
migrate.init_app(app, db)

# ============================

app.secret_key = uuid.uuid4().hex
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


with app.app_context():
    db.create_all()


# check file extension:
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# check file exist or not, if exist then process task:
@app.route('/FormData', methods=['GET', 'POST'])
def upload_file():
    userFiles = f"./Uploads"
    if request.method == 'POST':
        
        oprchoice = request.form.get("action")
        certificate_choice_id = request.form.get('certificate_choice')
        eventName = request.form.get("eventName")
        orgName = request.form.get("OrgName")
        certType = request.form.get("certificateType")
        organizer1 = request.form.get("Organizer1Desig")
        organizer2 = request.form.get("Organizer2Desig")

        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        CsvFile = request.files['file']
        Logo1File = request.files["logo"] # to get name of logo file
        Logo2File = request.files["logo2"]

        organizer1File = request.files["organizer1"] 
        organizer2File = request.files["organizer2"] 


        # If the user does not select a file, the browser submits an empty file without a filename.  
      
        if CsvFile.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if (CsvFile and allowed_file(CsvFile.filename)) or (CsvFile.filename) :
            csv_filename = secure_filename(CsvFile.filename)
            CsvFile.save(os.path.join(app.config['UPLOAD_FOLDER'], csv_filename))
            
        if (Logo1File and allowed_file(Logo1File.filename)) or (Logo1File.filename) :
            logo1_filename = secure_filename(Logo1File.filename)  
            Logo1File.save(os.path.join(app.config['UPLOAD_FOLDER'], logo1_filename))

        if (Logo2File and allowed_file(Logo2File.filename)) or (Logo2File.filename) :
            logo2_filename = secure_filename(Logo2File.filename)
            Logo2File.save(os.path.join(app.config['UPLOAD_FOLDER'], logo2_filename))

        if (organizer1File and allowed_file(organizer1File.filename)) or (organizer1File.filename) :
            organizer1_filename = secure_filename(organizer1File.filename)
            organizer1File.save(os.path.join(app.config['UPLOAD_FOLDER'], organizer1_filename))

        if (organizer2File and allowed_file(organizer2File.filename)) or (organizer2File.filename) :
            organizer2_filename = secure_filename(organizer2File.filename)
            organizer2File.save(os.path.join(app.config['UPLOAD_FOLDER'], organizer2_filename))
            

        if oprchoice == "Generate":
            if Logo2File.filename == '':
                print(f'\n\n\tLogo2 file is not given...')
                asyncio.run(ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", None, organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}"))
            else:
                print(f'\n\n\tLogo2 file is given...')
                asyncio.run(ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", f"{userFiles}/{logo2_filename}", organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}"))
            
            return render_template("ack.html")
        
        if oprchoice == "Preview":
            if Logo2File.filename == '':
                print(f'\tLogo2 file is not given...')
                asyncio.run(ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", None, organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}"))
            else:
                print(f'\tLogo2 file is given...')
                asyncio.run(ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", f"{userFiles}/{logo2_filename}", organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}"))
            
            return render_template("preview.html")

    return render_template("home.html")


#use to show user given data in new page:
@app.route("/csvFile")
def showcsv(csvData):
    return render_template("yourData.html", data=csvData)


# use to navigate to registration page:
@app.route("/Register", methods=["GET", "POST"])
def Register():
    if request.method == "POST":
        username = request.form['username']
        # fav_color = request.form["fav_color"]
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        newUser = User(username, email, password, confirm_password)
        if password == confirm_password:
            db.session.add(newUser)
            db.session.commit()
            return redirect("/")
        
    return render_template("RegisterT.html")


# landing page:
@app.route("/landing", methods=['GET', 'POST'])
def landingPage():
    if request.method == "POST":
        return render_template("landingT.html")
    return render_template("landingT.html")


#loggin page
@app.route('/', methods=['GET', 'POST'])
def Loggin():
    if request.method == "POST":
        email = request.form['email']
        name = request.form['username']
        password = request.form['password']
        print(f"\nLoggin password is: {password} ")

        # user = User.query.filter_by(email=email).first() # you can choose any of these filter_by()
        user = User.query.filter_by(name=name).first()

        # user = (User.query.filter_by(name=name).first()) and (User.query.filter_by(email=email).first())
        
        if user and user.check_password(password):
            session['name'] = user.name # after selecting filter_by() on wish, select right session.
            return render_template("landingT.html")
        
        else:
            return render_template('LogginT.html', error="Invalid user")
    if request.method == "GET":
        return render_template ("LogginT.html")

    return render_template("LogginT.html")


# home page: 
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return render_template("home.html")
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")    


