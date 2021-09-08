from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="Principal")

' Início do redirecionamento para as subpáginas Sobre o Projeto'

@app.route('/apresentacao')
def apresentacao():
    return render_template('apresentacao.html', titulo="Apresentação")

@app.route('/certificados')
def certificados():
    return render_template('certificados.html', titulo="Certificados")

@app.route('/equipe')
def equipe():
    return render_template('equipe.html', titulo="Equipe")

@app.route('/objetivos')
def objetivos():
    return render_template('objetivos.html', titulo="Objetivos")

@app.route('/publicacoes')
def publicacoes():
    return render_template('publicacoes.html', titulo="Publicações")

' Fim do redirecionamento para as subpáginas Sobre o Projeto'

@app.route('/conceitos')
def conceitos():
    return render_template('conceitos.html', titulo="Conceitos")

'início do redirecionamento para as subpáginas de Objetos V. de Aprendizagem'

@app.route('/categorias')
def categorias():
    return render_template('categorias.html', titulo="Categorias")

' Redirecionamento para as subpáginas das categorias...'
@app.route('/animacao')
def animacao():
    return render_template('animacao.html', titulo = "Animações")

@app.route('/audio')
def audio():
    return render_template('audio.html', titulo = "Audio")

@app.route('/hipertexto')
def hipertexto():
    return render_template('hipertexto.html', titulo = "Hipertextos")

@app.route('/imagens')
def imagens():
    return render_template('imagens.html', titulo = "Imagens")

@app.route('/jogos')
def jogos():
    return render_template('jogos.html', titulo = "Jogos")

@app.route('/mapaconceitual')
def mapaconceitual():
    return render_template('mapaconceitual.html', titulo = "Mapas Conceituais")

@app.route('/mapas')
def mapas():
    return render_template('mapas.html', titulo = "Mapas")

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', titulo = "Quiz")
    
@app.route('/videos')
def video():
    return render_template('videos.html', titulo = "Vídeos")

'Fim do redirecionamento para as subpáginas de categorias'

'Continuação...'

@app.route('/repositorios')
def repositorios():
    return render_template('repositorios.html', titulo="Repositórios")

@app.route('/ferramentas')
def ferramentas():
    return render_template('ferramentas.html', titulo="Ferramentas")

@app.route('/publicacoes2')
def publicacoes2():
    return render_template('publicacoes2.html', titulo="Publicações-OVA")

'Fim do redirecionamento para as subpáginas de Objetos V. de Aprendizagem'


'Início do redirecionamento para as subpáginas das Atividades do GEDOVA'

@app.route('/minicursos')
def minicursos():
    return render_template('minicursos.html', titulo="MiniCursos")

@app.route('/oficinas')
def oficinas():
    return render_template('oficinas.html', titulo="Oficinas")

@app.route('/palestras')
def palestras():
    return render_template('palestras.html', titulo="Palestras")

@app.route('/participacoes')
def participacoes():
    return render_template('participacoes_em_eventos.html', titulo="Participações em Eventos")

@app.route('/reunioes')
def reunioes():
    return render_template('reunioes.html', titulo="Reuniões")

if __name__ == "__main__":
    app.run(debug=True)