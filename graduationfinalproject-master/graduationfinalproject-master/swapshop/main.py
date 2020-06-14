'''
author: Waiyat Hamdani                      project-term :Spring 2020 (3 months)
        Aseel Fawalha

note: 1) yearly.html is actually for monthly
      2) peryear is actually for year
      3) baryearly and ybarchart is for monthly
      4) mybaryear and yybarchart is for yearly
      5) pieyearly and ypie is for monthly
      6) peryear and yypie is for yearly
'''
from flask import Flask , render_template ,redirect,url_for ,request , flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import Form, FloatField, TextField, PasswordField, SubmitField,BooleanField, SelectField ,IntegerField
from wtforms.validators import DataRequired
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import check_password_hash, generate_password_hash
import sys
import mypie as pie
import mychart as barchart
import baryearly as ybarchart
import mybaryear as yybarchart
import pieyearly as ypie
import peryear as yypie
import sqlite3
from datetime import datetime



#import pymysql, getpass
#global opas
#opas='swapshop2020'

app= Flask(__name__)
#app.db = None
global connections
connections=sqlite3.connect('swapshop.db',check_same_thread=False)
app.config['SECRET_KEY']="graduate"
bootstrap = Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

global currentDay
currentDay = datetime.now().day
#print(currentDay, file=sys.stderr)
currentMonth = datetime.now().month
#print(currentMonth, file=sys.stderr)
global symonth
if currentMonth == 1 or currentMonth == '1':
    symonth = 'january'
elif currentMonth == 2 or currentMonth == '2':
    symonth = 'febuary'
elif currentMonth == 3 or currentMonth == '3':
    symonth = 'march'
elif currentMonth == 4 or currentMonth == '4':
    symonth = 'april'
elif currentMonth == 5 or currentMonth == '5':
    symonth = 'may'
elif currentMonth == 6 or currentMonth == '6':
    symonth = 'june'
elif currentMonth == 7 or currentMonth == '7':
    symonth = 'july'
elif currentMonth == 8 or currentMonth == '8':
    symonth = 'august'
elif currentMonth == 9 or currentMonth == '9':
    symonth = 'september'
elif currentMonth == 10 or currentMonth == '10':
    symonth = 'october'
elif currentMonth == 11 or currentMonth == '11':
    symonth = 'september'
elif currentMonth == 12 or currentMonth == '12':
    symonth = 'december'
global currentYear
currentYear = datetime.now().year
#print(currentYear, file=sys.stderr)

''' this is for online one
def connectdb():
    if not app.db:
        db_IP = '35.225.168.87'
        # getpass so that password is not echoed to the terminal
        pswd = opas
        app.db = pymysql.connect(db_IP, 'root', pswd, 'swapshop')
    else:
        print('Connected!', file=sys.stderr)
'''
class requestitemform3(FlaskForm):
    itemid1=TextField("item id 1: ",validators=[DataRequired()])
    quantity1=TextField("quantity item 1: ",validators=[DataRequired()])
    itemid2=TextField("item id 2: ",validators=[DataRequired()])
    quantity2=TextField("quantity item 2: ",validators=[DataRequired()])
    itemid3=TextField("item id 3: ",validators=[DataRequired()])
    quantity3=TextField("quantity item 3: ",validators=[DataRequired()])
    dept=TextField("department name: ",validators=[DataRequired()])
    deptphoneext=TextField("department phone ext: ",validators=[DataRequired()])
    southernemail=TextField("southern email: ",validators=[DataRequired()])
    facultyname=TextField("faculty name: ",validators=[DataRequired()])
    submit=SubmitField("request")

class requestitemform2(FlaskForm):
    itemid1=TextField("item id 1: ",validators=[DataRequired()])
    quantity1=TextField("quantity item 1: ",validators=[DataRequired()])
    itemid2=TextField("item id 2: ",validators=[DataRequired()])
    quantity2=TextField("quantity item 2: ",validators=[DataRequired()])
    dept=TextField("department name: ",validators=[DataRequired()])
    deptphoneext=TextField("department phone ext: ",validators=[DataRequired()])
    southernemail=TextField("southern email: ",validators=[DataRequired()])
    facultyname=TextField("faculty name: ",validators=[DataRequired()])
    submit=SubmitField("request")

class requestitemform1(FlaskForm):
    itemid1=TextField("item id 1: ",validators=[DataRequired()])
    quantity1=TextField("quantity item 1: ",validators=[DataRequired()])
    dept=TextField("department name: ",validators=[DataRequired()])
    deptphoneext=TextField("department phone ext: ",validators=[DataRequired()])
    southernemail=TextField("southern email: ",validators=[DataRequired()])
    facultyname=TextField("faculty name: ",validators=[DataRequired()])
    submit=SubmitField("request")

class loginform(FlaskForm):
    id=TextField("User:",validators=[DataRequired()])
    pas=PasswordField("Pass:", validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit=SubmitField("login")

class categoryform(FlaskForm):
    cat=SelectField('Item Category: ', choices=[('binder','binder'),('envelope','envelope')
    ,('Divders, Tabs and Labels','Divders, Tabs and Labels'),
    ('Files and Folders','Files and Folders'),('Paper','Paper'),
    ('Organizational Supplies','Organizational Supplies'),
    ('General Office Supplies','General Office Supplies'),
    ('Electronics','Electronics'),('other','other')])

    submit=SubmitField("search")

class addexistingform(FlaskForm):
    itemid=TextField('item ID: ',validators=[DataRequired()])
    quantity=FloatField('change quantity',validators=[DataRequired()])
    submit=SubmitField("change")

class pickupform(FlaskForm):
    id=TextField('ID: ', validators=[DataRequired()])
    quantity=FloatField('quantity: ', validators=[DataRequired()])
    requestdate= TextField('request date:', validators=[DataRequired()])
    requestmonth=SelectField('request month: ', choices=[('january','january'),('febuary','febuary')
    ,('march','march'),('april','april'),('may','may'),('june','june'),
    ('july','july'),('august','august'),('september','september'),('october','october'),
    ('november','november'),('december','december')])
    weight=FloatField('Weight in pounds: ', validators=[DataRequired()])
    dept=TextField('dept : ', validators=[DataRequired()])
    faculty=TextField('faculty name : ', validators=[DataRequired()])
    SubmitField=SubmitField('pick up')

class addnewform(FlaskForm):
    name=TextField('item id: ', validators=[DataRequired()])
    quantity=FloatField('quantity: ', validators=[DataRequired()])
    value=FloatField('value/item (enter without $): ', validators=[DataRequired()])
    yearin=TextField('year: ', validators=[DataRequired()])
    monthin=SelectField('month: ', choices=[('january','january'),('febuary','febuary')
    ,('march','march'),('april','april'),('may','may'),('june','june'),
    ('july','july'),('august','august'),('september','september'),('october','october'),
    ('november','november'),('december','december')])
    categories=SelectField('Item Category: ', choices=[('binder','binder'),('envelope','envelope')
    ,('Divders, Tabs and Labels','Divders, Tabs and Labels'),
    ('Files and Folders','Files and Folders'),('Paper','Paper'),
    ('Organizational Supplies','Organizational Supplies'),
    ('general office supplies','general office supplies'),
    ('Electronics','Electronics'),('other','other')])
    SubmitField=SubmitField('pick up')

class searchform(FlaskForm):
    category=SelectField('Item Category: ', choices=[('binder','binder'),('envelope','envelope')
    ,('Divders, Tabs and Labels','Divders, Tabs and Labels'),
    ('Files and Folders','Files and Folders'),('Paper','Paper'),
    ('Organizational Supplies','Organizational Supplies'),
    ('General Office Supplies','General Office Supplies'),
    ('Electronics','Electronics'),('other','other')])
    submit=SubmitField("search")

class yearlyform(FlaskForm):
    months=SelectField('month: ', choices=[('january','january'),('febuary','febuary')
    ,('march','march'),('april','april'),('may','may'),('june','june'),
    ('july','july'),('august','august'),('september','september'),('october','october'),
    ('november','november'),('december','december')])
    year=SelectField('year: ', choices=[('2020','2020'),('2021','2021')
    ,('2022','2022'),
    ('2023','2023'),('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027')])
    submit=SubmitField("calculate")

class peryearform(FlaskForm):
    year=SelectField('year: ', choices=[('2020','2020'),('2021','2021')
    ,('2022','2022'),
    ('2023','2023'),('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027')])
    submit=SubmitField("calculate")

class regitrationform(FlaskForm):
    id=TextField('register id:', validators=[DataRequired()])
    pas=TextField('register password:', validators=[DataRequired()])
    submit=SubmitField("register")

class removeregform(FlaskForm):
    id=TextField('remove id:', validators=[DataRequired()])
    submit=SubmitField("remove")

def is_admin():
    if current_user:
        if current_user.role == 'admin':
            return True
        else:
            return False
    else:
        print('User not authenticated.', file=sys.stderr)

def is_assistant():
    if current_user:
        if current_user.role=='assistant':
            return True
        else:
            return False
    else:
        print("User not authenticated.", file=sys.stderr)

class User(UserMixin):
    def __init__(self, username, password, role):
        self.id = username
        #print(userid, file=sys.stderr)
        #hash the password andn output it to stderr
        self.pass_hash = generate_password_hash(password)
        print(self.pass_hash, file=sys.stderr)
        self.role = role

global user_admin
user_admin = {}

def mylogindb():
    c = connections.cursor()
    c.execute('SELECT * from login')
    login_list = c.fetchall()
    for mylogin in login_list:
        user_admin[str(mylogin[0])]=User(str(mylogin[0]),str(mylogin[1]),str(mylogin[2]))

@login_manager.user_loader
def load_user(id):
    return user_admin.get(id)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/item3",methods=['GET','POST'])
def ritem3():
    '''
    if not app.db:
        connectdb()
    '''
    itemid1=None
    quantity1=None
    itemid2=None
    quantity2=None
    itemid3=None
    quantity3=None
    dept=None
    deptphoneext=None
    southernemail=None
    facultyname=None
    #conn=app.db.cursor()
    conn=connections.cursor()
    forma=requestitemform3()
    if forma.validate_on_submit():
        itemid1=forma.itemid1.data
        quantity1=forma.quantity1.data
        itemid2=forma.itemid2.data
        quantity2=forma.quantity2.data
        itemid3=forma.itemid3.data
        quantity3=forma.quantity3.data
        dept=forma.dept.data
        deptphoneext=forma.deptphoneext.data
        southernemail=forma.southernemail.data
        facultyname=forma.facultyname.data
        myday=currentDay
        mymonth=symonth
        myyear=currentYear
        conn.execute('insert into reciept values("{}",{},"{}",{},"{}",{},"{}","{}","{}","{}","{}","{}","{}")'.format(itemid1,quantity1,itemid2,quantity2,itemid3,quantity3,dept,deptphoneext,southernemail,facultyname,myday,mymonth,myyear))
        #app.db.commit()
        flash('Thank you for your request order and Have a nice day')
        connections.commit()
        return render_template('item3.html', forma=forma)
    return render_template('item3.html',forma=forma)

@app.route("/item2",methods=['GET','POST'])
def ritem2():
    '''
    if not app.db:
        connectdb()
    '''
    itemid1=None
    quantity1=None
    itemid2=None
    quantity2=None
    dept=None
    deptphoneext=None
    southernemail=None
    facultyname=None
    #conn=app.db.cursor()
    conn=connections.cursor()
    forma=requestitemform2()
    if forma.validate_on_submit():
        itemid1=forma.itemid1.data
        quantity1=forma.quantity1.data
        itemid2=forma.itemid2.data
        quantity2=forma.quantity2.data
        itemid3= "none"
        quantity3= 0
        dept=forma.dept.data
        deptphoneext=forma.deptphoneext.data
        southernemail=forma.southernemail.data
        facultyname=forma.facultyname.data
        myday=currentDay
        mymonth=symonth
        myyear=currentYear
        conn.execute('insert into reciept values("{}",{},"{}",{},"{}",{},"{}","{}","{}","{}","{}","{}","{}")'.format(itemid1,quantity1,itemid2,quantity2,itemid3,quantity3,dept,deptphoneext,southernemail,facultyname,myday,mymonth,myyear))
        #app.db.commit()
        flash('Thank you for your request order and Have a nice day')
        connections.commit()
        return render_template('item2.html', forma=forma)
    return render_template('item2.html',forma=forma)

@app.route("/item1",methods=['GET','POST'])
def ritem1():
    '''
    if not app.db:
        connectdb()
    '''
    itemid1=None
    quantity1=None
    dept=None
    deptphoneext=None
    southernemail=None
    facultyname=None
    #conn=app.db.cursor()
    conn=connections.cursor()
    forma=requestitemform1()
    if forma.validate_on_submit():
        itemid1=forma.itemid1.data
        quantity1=forma.quantity1.data
        itemid2="none"
        quantity2=0
        itemid3= "none"
        quantity3= 0
        dept=forma.dept.data
        deptphoneext=forma.deptphoneext.data
        southernemail=forma.southernemail.data
        facultyname=forma.facultyname.data
        myday=currentDay
        mymonth=symonth
        myyear=currentYear
        conn.execute('insert into reciept values("{}",{},"{}",{},"{}",{},"{}","{}","{}","{}","{}","{}","{}")'.format(itemid1,quantity1,itemid2,quantity2,itemid3,quantity3,dept,deptphoneext,southernemail,facultyname,myday,mymonth,myyear))
        #app.db.commit()
        flash('Thank you for your request order and Have a nice day')
        connections.commit()
        return render_template('item1.html', forma=forma)
    return render_template('item1.html',forma=forma)

@app.route("/item",methods=['GET','POST'])
def item():
    cat = None
    '''
    if not app.db:
        connectdb()
    '''
    #conn=app.db.cursor()
    conn=connections.cursor()
    conn.execute('select * from itemin where category="binder"')
    inlist=conn.fetchall()
    formc=categoryform()
    if formc.validate_on_submit():
        cat=formc.cat.data
        if cat == 'all':
            conn.execute('select * from itemin')
            inlist=conn.fetchall()
            return render_template('item.html',inlist=inlist,formc=formc)
        else:
            conn.execute('select * from itemin where category = "{}"'.format(cat))
            inlist=conn.fetchall()
            return render_template('item.html',inlist=inlist,formc=formc)
    return render_template('item.html',inlist=inlist,formc=formc)

@app.route("/addexistingitem", methods=['GET','POST'])
@login_required
def add():
    itemid=None
    quantity=None
    category=None
    '''
    if not app.db:
        connectdb()
    '''
    #conn=app.db.cursor()
    conn=connections.cursor()
    conn.execute('select * from itemin where category="binder"')
    inlist=conn.fetchall()
    formae=addexistingform()
    forms=searchform()
    if formae.validate_on_submit():
        itemid=formae.itemid.data
        quantity=formae.quantity.data
        conn.execute('update itemin set quantity ={} where itemid="{}";'.format(quantity, itemid))
        #app.db.commit()
        connections.commit()
        flash('change successful refresh the page please')
    if forms.validate_on_submit():
        category=forms.category.data
        conn.execute('select * from itemin where category = "{}";'.format(category))
        inlist=conn.fetchall()
        return render_template('addexisting.html',inlist=inlist,formae=formae, forms=forms)

    return render_template('addexisting.html',inlist=inlist,formae=formae, forms=forms)

@app.route("/addnew",methods=['GET','POST'])
@login_required
def addnew():
    name=None
    quantity=None
    value=None
    yearin=None
    monthin=None
    categories=None
    category=None
    '''
    if not app.db:
        connectdb()
    '''
    #conn=app.db.cursor()
    conn=connections.cursor()
    conn.execute('select * from itemin where category="binder"')
    inlist=conn.fetchall()
    forma=addnewform()
    forms=searchform()
    if forma.validate_on_submit():
        name=forma.name.data
        quantity=forma.quantity.data
        value=forma.value.data
        yearin=forma.yearin.data
        monthin=forma.monthin.data
        categories=forma.categories.data
        conn.execute('insert into itemin values("{}",{},{},"{}",{}","{}")'.format(name,quantity,value,yearin,monthin,categories))
        #app.db.commit()
        connections.commit()
        flash('change successful')
    if forms.validate_on_submit():
        category=forms.category.data
        conn.execute('select * from itemin where category = "{}";'.format(category))

        inlist=conn.fetchall()
        return render_template('addnew.html',inlist=inlist,forma=forma, forms=forms)
    return render_template('addnew.html',inlist=inlist,forma=forma, forms=forms)


@app.route("/pickup",methods=['GET','POST'])
@login_required
def pickup():
    id=None
    name=None
    quantity=None
    requestdate=None
    requestmonth=None
    faculty=None
    value=None
    weight=None
    dept=None
    categories=None
    category=None
    '''
    if not app.db:
        connectdb()
    '''
    #conn=app.db.cursor()
    conn=connections.cursor()
    conn.execute('select * from itemin where category="binder"')
    inlist=conn.fetchall()
    forma=pickupform()
    forms=searchform()

    if forma.validate_on_submit():
        id=forma.id.data
        conn.execute('select * from itemin where itemid="{}"'.format(id))
        mydata=conn.fetchall()
        name=mydata[0][1]
        quantity=forma.quantity.data
        value=mydata[0][3]
        yearout=currentYear
        monthout=symonth
        weight=forma.weight.data
        dept=forma.dept.data
        requestdate=forma.requestdate.data
        requestmonth=forma.requestmonth.data
        faculty=forma.faculty.data
        categories=mydata[0][6]
        pastquantity=mydata[0][2]
        try:
            conn.execute('insert into itemout values("{}","{}",{},{},"{}","{}",{},"{}","{}")'.format(id,name,quantity,quantity*value,yearout,monthout,weight,dept,categories))
            conn.execute('update itemin set quantity ={} where itemid="{}";'.format(pastquantity-quantity, id))
            conn.execute('DELETE FROM reciept WHERE dept="{}" and facultyname="{}" and day={} and month="{}" ;'.format(dept,faculty,requestdate,requestmonth))
            #app.db.commit()
            connections.commit()
            flash('change successful')
        except ValueError:
            conn.execute('insert into itemout values("{}","{}",{},{},"{}","{}",{},"{}","{}")'.format(id,name,quantity,quantity*value,yearout,monthout,weight,dept,categories))
            conn.execute('update itemin set quantity ={} where itemid="{}";'.format(pastquantity-quantity, id))
            #app.db.commit()
            connections.commit()
            flash('change successful')

    if forms.validate_on_submit():
        category=forms.category.data
        print(category, file=sys.stderr)
        conn.execute('select * from itemin where category = "{}";'.format(category))
        inlist=conn.fetchall()
        return render_template('pickup.html',inlist=inlist,forma=forma, forms=forms)
    return render_template('pickup.html',inlist=inlist,forma=forma, forms=forms)


@app.route("/yearly",methods=['GET','POST'])
@login_required
def yearly():
    y="january"
    x=2020
    formae=yearlyform()
    if formae.validate_on_submit():
        itemid=formae.year.data
        itemidy=formae.months.data
        x=itemid
        y=itemidy

    binder=ypie.binder(x,y)
    env=ypie.envelope(x,y)
    dtl=ypie.dtl(x,y)
    file=ypie.fileandfolder(x,y)
    paper=ypie.paper(x,y)
    ogs=ypie.organizationalsupplies(x,y)
    gof=ypie.generaloffice(x,y)
    elt=ypie.electronic(x,y)
    allpickup=ypie.alltotalpickup(x,y)
    allweight=ypie.totalweight(x,y)

    bbinder=ybarchart.binder(x,y)
    benv=ybarchart.envelope(x,y)
    bdtl=ybarchart.dtl(x,y)
    bfile=ybarchart.fileandfolder(x,y)
    bpaper=ybarchart.paper(x,y)
    bogs=ybarchart.organizationalsupplies(x,y)
    bgof=ybarchart.generaloffice(x,y)
    belt=ybarchart.electronic(x,y)
    allsale=ybarchart.allsalestatistic(x,y)

    return render_template('yearly.html',binder=binder,env=env,dtl=dtl,file=file,paper=paper,
    ogs=ogs, gof=gof, elt=elt,bbinder=bbinder,benv=benv,bdtl=bdtl,bfile=bfile,bpaper=bpaper,
    bogs=ogs, bgof=gof, belt=belt , allsale=allsale , allpickup=allpickup, allweight=allweight, formae=formae)

@app.route("/peryear",methods=['GET','POST'])
@login_required
def peryear():
    y="january"
    x=2020
    formae=peryearform()
    if formae.validate_on_submit():
        itemid=formae.year.data
        x=itemid

    binder=yypie.binder(x)
    env=yypie.envelope(x)
    dtl=yypie.dtl(x)
    file=yypie.fileandfolder(x)
    paper=yypie.paper(x)
    ogs=yypie.organizationalsupplies(x)
    gof=yypie.generaloffice(x)
    elt=yypie.electronic(x)
    allpickup=yypie.alltotalpickup(x)
    allweight=yypie.totalweight(x)

    bbinder=yybarchart.binder(x)
    benv=yybarchart.envelope(x)
    bdtl=yybarchart.dtl(x)
    bfile=yybarchart.fileandfolder(x)
    bpaper=yybarchart.paper(x)
    bogs=yybarchart.organizationalsupplies(x)
    bgof=yybarchart.generaloffice(x)
    belt=yybarchart.electronic(x)
    allsale=yybarchart.allsalestatistic(x)

    return render_template('peryear.html',binder=binder,env=env,dtl=dtl,file=file,paper=paper,
    ogs=ogs, gof=gof, elt=elt,bbinder=bbinder,benv=benv,bdtl=bdtl,bfile=bfile,bpaper=bpaper,
    bogs=ogs, bgof=gof, belt=belt , allsale=allsale , allpickup=allpickup, allweight=allweight, formae=formae)

@app.route("/registerassistantforswapshop", methods=['GET','POST'])
def register():
    conn=connections.cursor()
    id=None
    pas=None
    form=regitrationform()
    if form.validate_on_submit():
        id=form.id.data
        pas=form.pas.data
        type="assistant"
        conn.execute("insert into login values('{}','{}','{}')".format(id,pas,type))
        connections.commit()
        flash('register successful')
        return render_template('regist.html',form=form)
    return render_template('regist.html',form=form)

@app.route("/removeassistantfromswapshop",methods=['GET','POST'])
def removeregister():
    id=None
    conn=connections.cursor()
    conn.execute('select * from login where role="assistant"')
    inlist=conn.fetchall()
    form=removeregform()
    if form.validate_on_submit():
        id=form.id.data
        conn.execute("delete from login where id='{}' and role='assistant' ".format(id))
        connections.commit()
        flash('remove successful refresh the page please')
        return render_template('removereg.html',form=form,inlist=inlist)
    return render_template('removereg.html',form=form,inlist=inlist)

@app.route("/recieptforrequest")
@login_required
def recieptnotification():
    conn=connections.cursor()
    conn.execute('select * from reciept')
    inlist=conn.fetchall()
    return render_template('recip.html', inlist=inlist)


@app.route("/success",methods=['GET','POST'])
@login_required
def success():
    userid=usern
    binder=pie.binder()
    env=pie.envelope()
    dtl=pie.dtl()
    file=pie.fileandfolder()
    paper=pie.paper()
    ogs=pie.organizationalsupplies()
    gof=pie.generaloffice()
    elt=pie.electronic()
    allpickup=pie.alltotalpickup()
    allweight=pie.totalweight()

    bbinder=barchart.binder()
    benv=barchart.envelope()
    bdtl=barchart.dtl()
    bfile=barchart.fileandfolder()
    bpaper=barchart.paper()
    bogs=barchart.organizationalsupplies()
    bgof=barchart.generaloffice()
    belt=barchart.electronic()
    allsale=barchart.allsalestatistic()

    return render_template('suc.html',userid=userid ,binder=binder,env=env,dtl=dtl,file=file,paper=paper,
    ogs=ogs, gof=gof, elt=elt,bbinder=bbinder,benv=benv,bdtl=bdtl,bfile=bfile,bpaper=bpaper,
    bogs=ogs, bgof=gof, belt=belt , allsale=allsale , allweight=allweight, allpickup=allpickup)


@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('success') )
    id = None
    pas = None
    forml = loginform()
    if forml.validate_on_submit():
        mylogindb()
        id = forml.id.data
        global usern
        usern= id
        pas = forml.pas.data
        user=user_admin[id]
        valid_password=check_password_hash(user.pass_hash,pas)
        if user is None or not valid_password :
            print('invalid', file=sys.stderr)
            return render_template("login.html", forml=forml)
        else:
            login_user(user, forml.remember_me.data)
            return redirect(url_for('success'))

    return render_template("login.html", forml=forml,id=id,pas=pas)




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
