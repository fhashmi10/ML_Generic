"""App module to run web"""
from web import app, views

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
