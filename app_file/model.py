from app_file import db

class UserRegister(db.Model):
    """記錄使用者資料的資料表"""
    __tablename__ = 'UserRegister'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)
