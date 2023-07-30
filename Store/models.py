from Store import db
import datetime

class Users(db.Model):
    """Таблица для хранения пользователей"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow) # Дата регистрации
    
    def __repr__(self):
        return f'User: {self.name}'
    
    
class Product(db.Model):
    """Таблица для хранения товаров"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    company = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Product: {self.title}'
    
class Comment(db.Model):
    """Таблица комментариев к товаром.
        Связана с таблицей товаров свяью один ко многим
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text)
    comment_creat = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'Comment: {self.comment_creat}'
