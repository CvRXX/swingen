from flask import Flask
from flask import render_template
import parseSingenWaves

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route("/")
def hello():
    return render_template('dashboard.html')

@app.route("/wavedata.js")
def waveData():
    return render_template('data/wavesignals.js', waveData=parseSingenWaves.parseWaves("/home/carlos/gits/singen/src"))

if __name__ == "__main__":
    app.run()
