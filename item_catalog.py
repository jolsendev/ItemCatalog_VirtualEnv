from flask import Flask

app = Flask("First App")


@app.route('/')
def index():
    return "Yes it is working!!"


if __name__ == "__main__":
    app.run()
