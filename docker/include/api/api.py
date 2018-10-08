import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Initial Flask test page</h1><p>Check to see if we have our minimal flask app running properly in Docker</p>"
# host arg because we need container to listen on its public interface so localhost on host can see it.
app.run(host='0.0.0.0')
