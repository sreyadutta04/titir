from flask import Flask,session,render_template,request,redirect,url_for

app=Flask(__name__)

app.secret_key='asdsdfsdfs13sdf_df%&'

@app.route('/login',methods=['GET','POST'])

def login():
    if request.method=='POST':
        session['username']=request.form['username']
        session['password']=request.form['password']
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again'
        else:
            return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('password',None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    login=False
    if 'username'and 'password' in session:
        login=True
    return render_template('login_home.html',login=login)

if __name__=='__main__':
    app.run(debug=True)