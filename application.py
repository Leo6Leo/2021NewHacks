from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("mainpage.html")

@app.route("/uploaded", methods=["POST"])
def uploaded():
    upload = request.args.get("upload")
    if not upload:
        return "failure"
    render_template("success.html")

if __name__ == '__main__':
    app.run()
