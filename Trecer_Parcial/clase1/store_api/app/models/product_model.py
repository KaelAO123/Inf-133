from app.database import db
class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Double(),nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    def __init__(self,name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def save(self):
        db.session.add(self)
        db.commit()
    
    @staticmethod
    def get_all():
        return Product.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)
    
    def update(self, name = None,description = None,price = None,stock = None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()