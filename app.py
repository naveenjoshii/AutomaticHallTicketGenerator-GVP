from flask import Flask,render_template,request,make_response,session,redirect,url_for
import pdfkit
from pymongo import MongoClient
import bcrypt
import json
client = MongoClient("mongodb://localhost:27017/")
db3=client['Users_info']
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'
course = ''
branch = ''
semester = ''
month = ''
year = ''
reg=''


@app.route('/semester',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        global course, branch, semester, month, year,reg
        course = request.form['course']
        branch = request.form['branch']
        semester = request.form['sem']
        month = request.form['semMonth']
        year = request.form['year']
        reg = request.form['reg']
        print("------branch-------",branch)
        db = client[branch]
        print("------------------",semester)
        user = semester
        ele=[]
        sub=[]
        labs=[]
        labelec=[]
        eleres={}
        labres={}
        collection = db[user.lower()]
        db2 = client['electives']
        eke = db2['electives']
        g =collection.find({},{"_id":0})
        for i in g:
            if i['elective']!="0" and i['lab']=="0":
                ele.append(i)
            elif i['lab']!="1":
                sub.append(i)
            elif i['elective']!="0" and i['lab']=="1" :
                labelec.append(i)
            else:
                labs.append(i)
        for i in ele:
            c = eke.find_one({"elective_no":i['elective']})
            eleres[i['elective']] = c['elective_name']
        for j in labelec:
            d = eke.find_one({"elective_no":j['elective']})
            labres[j['elective']] = d['elective_name']
        sub_ele = dict()
        for key in eleres:
            sub_ele[ eleres[key] ] = [ (x['subject'], x['code']) for x in ele if x['elective'] == key]
        lab_ele = dict()
        for key in labres:
            lab_ele[ labres[key] ] = [ (x['subject'], x['code']) for x in labelec if x['elective'] == key ]
    return render_template('newhello.html',sub=sub ,labs=labs ,eleres=sub_ele,labres=lab_ele)




@app.route('/check/<sub>/<labs>/<ele_res>/<lab_res>',methods=['POST','GET'])
def check(sub,labs,ele_res,lab_res):
    if request.method=='POST':
        ele_res = list(ele_res.split("'"))
        lab_res = list(lab_res.split("'"))
        sub_ele = list()
        for i in ele_res:
            i=i.strip()
            if not i in ",[]":
                val = request.form[i]
                val = list(val.split("'"))[1:-1]
                val = (val[0], val[2])
                sub_ele.append(val)
        lab_ele = list()
        for i in lab_res:
            i=i.strip()
            if not i in ",[]":
                val = request.form[i]
                val = list(val.split("'"))[1:-1]
                val = (val[0], val[2])
                lab_ele.append(val)
        global course, branch, semester, month, year,reg
        roll_no = session['userrol']
        users = db3["user_data"]
        login_user = users.find_one({'roll' : roll_no})
        json_acceptable_string = sub.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        json_acceptable_string = labs.replace("'", "\"")
        e = json.loads(json_acceptable_string)
        rendered = render_template('Studentform.html',subj=d,subj_ele=sub_ele,lab=e,lab_ele=lab_ele, course=course, branch=branch, month=month, year=year, semester=semester, roll_no=session['userrol'], name=login_user['name'],reg=reg)
        pdf = pdfkit.from_string(rendered,False)
        respose = make_response(pdf)
        respose.headers['Content-Type'] = 'application/pdf'
        respose.headers['Content-Disposition'] = 'inline;filename=hallticket.pdf'
    return respose



@app.route('/')
def index():
    if 'userrol' in session:
        return render_template('index.html')
    return render_template('home.html')



@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        if request.form['userrol'] == "admin" and request.form['userpsw'] == "admin123":
            return render_template("admin.html")
        users =db3["user_data"]
        login_user = users.find_one({'roll' : request.form['userrol']})
        if login_user:
            if request.form['userpsw'] == login_user['password']:
                session['userrol'] = request.form['userrol']
                return redirect(url_for('index'))
        return 'Invalid username/password combination'
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    error=""
    psdError=""
    if request.method == 'POST':
        users = db3["user_data"]
        if(len(request.form['userrol'])==10 and len(request.form['userpsw'])>6 and len(request.form['username'])>0 and len(request.form['useremail'])>0):
            existing_user = users.find_one({'roll' : request.form['userrol']})
            if existing_user is None:
                users.insert({'roll' : request.form['userrol'], 'password' : request.form['userpsw'],'name':request.form['username'],'email': request.form['useremail']})
                session['userrol'] = request.form['userrol']
                return redirect(url_for('index'))
            return 'User already exists!'
        else:
            if(len(request.form['userpsw'])<6):
                psdError = "Length of password must be greater than 6"
            error = "Enter all the details"
    return render_template('register.html',error=error,psdError = psdError)



@app.route('/logout')
def logout():
    session.pop('userrol', None)
    return render_template('home.html')



if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
    app.run()
