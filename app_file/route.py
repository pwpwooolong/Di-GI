from app_file import app
from app_file import db
from flask import render_template
from app_file.model import UserRegister
from app_file.form import FormRegister

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def test():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        user = UserRegister(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return '註冊成功！' 
    return render_template('register.html', form=form)
