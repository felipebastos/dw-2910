import os

from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
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
    return render_template('upload/index.html', imagens=imgs)


@bp.post('/save')
def save():
    if 'file' not in request.files:
        flash('Formulário não tem campo de arquivos.')
        return redirect(url_for('upload.root'))
    file = request.files['file']
    if file.filename == '':
        flash('Não selecionou arquivos.')
        return redirect(url_for('upload.root'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        app = create_app()

        imgs = os.listdir(app.config['UPLOAD_FOLDER'])
        filename = f'{len(imgs)+1:08}.{filename.rsplit(".", 1)[1].lower()}'

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Upload com sucesso!')
        
        return redirect(url_for('upload.root'))
    return redirect(url_for('upload.root'))

@bp.get('/img/<nome>')
def imagem(nome):
    app = create_app()
    return send_from_directory(app.config['UPLOAD_FOLDER'], nome)

def init_app(app):
    app.register_blueprint(bp)