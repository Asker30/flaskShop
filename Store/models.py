from Store import db
import datetime
import pytz

moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))


class Users(db.Model):
    """Таблица для хранения пользователей"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=moscow_time) # Дата регистрации
    user_type = db.Column(db.String(10), default='user')
    active = db.Column(db.Boolean, default=True)
    comments = db.relationship('Comment', backref='user')
    
    def __repr__(self):
        return f'User: {self.name}'
    
    
class Product(db.Model):
    """Таблица для хранения товаров"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    img = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)
    company = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='product')
    
    def __repr__(self):
        return f'Product: {self.title}'
    
class Comment(db.Model):
    """Таблица комментариев к товаром.
        Связана с таблицей товаров связью один ко многим
    """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text)
    comment_creat = db.Column(db.DateTime, default=moscow_time)
    
    def __repr__(self):
        return f'Comment: {self.comment_creat}'
    
    
    class Session:
        def __init__(self, user):
            self.user = user
            
        def get(self):
            return self.user.id
