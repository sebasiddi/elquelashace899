from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

RSS_FEED_URL = "https://www.spreaker.com/show/6491155/episodes/feed"

def obtener_episodios():
    feed = feedparser.parse(RSS_FEED_URL)
    episodios = []
    for entry in feed.entries:
        episodio_id = entry.id.split("/")[-1]  # Extraer el ID desde entry.id
        episodios.append({
            "titulo": entry.title,
            "url": entry.link,
            "id": episodio_id  # Usar este ID para el embed
        })
    return episodios

@app.route('/')
def home():
    episodios = obtener_episodios()
    return render_template("index.html", episodios=episodios)

@app.route('/episodio/<id>')
def episodio(id):
    episodios = obtener_episodios()
    episodio = next((e for e in episodios if e["id"] == id), None)
    if not episodio:
        return "Episodio no encontrado", 404
    return render_template("episodio.html", episodio=episodio)

if __name__ == '__main__':
    app.run(debug=True)

# Creación de carpetas necesarias
# templates/index.html
# templates/episodio.html
