import os

from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename

from backend.app import create_app


bp = Blueprint('upload', __name__, url_prefix='/upload', template_folder='templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def root():
    app = create_app()
    imgs = os.listdir(app.config['UPLOAD_FOLDER'])
    #return render_template('upload/index.html', imagens=imgs)
    response = {'imagens': imgs}
    return jsonify(response)


@bp.post('/save')
def save():
    if 'arquivo' not in request.files:
        response = {'status': 'Formulário não tem campo de arquivos.'}
        return jsonify(response)
    file = request.files['arquivo']
    if file.filename == '':
        response = {'status': 'Arquivo sem nome.'}
        return jsonify(response)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        app = create_app()

        imgs = os.listdir(app.config['UPLOAD_FOLDER'])
        filename = f'{len(imgs)+1:08}.{filename.rsplit(".", 1)[1].lower()}'

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        response = {'status': 'Upload com sucesso!'}
        return jsonify(response)
    else:
        response = {'status': 'Formato de arquivo não permitido.'}
        return jsonify(response)

@bp.get('/img/<nome>')
def imagem(nome):
    app = create_app()
    return send_from_directory(app.config['UPLOAD_FOLDER'], nome)

def init_app(app):
    app.register_blueprint(bp)