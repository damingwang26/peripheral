import os
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1/akme_database'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

# 商品表
class Product(db.Model):
    __tablename__ = 'products'  # 表名

    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(100), nullable=False)  # 商品名称
    description = db.Column(db.Text, nullable=True)  # 商品描述
    price = db.Column(db.Float, nullable=False)  # 商品价格
    image = db.Column(db.Text)
    url = db.Column(db.Text)  # 库存数量
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # 创建时间
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # 更新时间

    def __repr__(self):
        return f"<Product {self.name}>"

# 主页展示商品表
class HotProduct(db.Model):
    __tablename__ = 'hot_products'  # 表名

    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(100), nullable=False)  # 商品名称
    description = db.Column(db.Text, nullable=True)  # 商品描述
    price = db.Column(db.Float, nullable=False)  # 商品价格
    image = db.Column(db.Text)
    url = db.Column(db.Text)  # 库存数量
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # 创建时间
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # 更新时间

    def __repr__(self):
        return f"<HotProduct {self.name}>"

# 主页滚动展示商品表
class SlideProduct(db.Model):
    __tablename__ = 'slide_products'  # 表名

    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(100), nullable=False)  # 商品名称
    description = db.Column(db.Text, nullable=True)  # 商品描述
    price = db.Column(db.Float, nullable=False)  # 商品价格
    image = db.Column(db.Text)
    url = db.Column(db.Text)  # 库存数量
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # 创建时间
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # 更新时间

    def __repr__(self):
        return f"<SlideProduct {self.name}>"
    
# 创建上传目录（如果不存在）
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return {
        'status': 200,
        'data': [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'url': product.url, 'image': product.image} for product in products]
    }

@app.route('/api/home_products', methods=['GET'])
def home_products():
    hot_products = HotProduct.query.all()
    slide_products = SlideProduct.query.all()
    return {
        'status': 200,
        'data': {
          'hot_products': [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'url': product.url, 'image': product.image} for product in hot_products],
          'slide_products': [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'url': product.url, 'image': product.image} for product in slide_products],
        }
    }

@app.route('/api/upload', methods=['POST'])
def upload_image():
    # 检查是否有文件上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # 如果用户没有选择文件
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 检查文件类型是否允许
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400
    
@app.route('/api/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# DEBUG FOR SINGLE PORT SERVER
# @app.route('/')
# def web():
#     return render_template('index.html')

# @app.route('/assets/<filename>')
# def web_file(filename):
#     return send_from_directory('./templates/assets', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')