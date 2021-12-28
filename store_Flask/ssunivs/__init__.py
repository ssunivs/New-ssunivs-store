from flask import Flask
app=Flask(__name__)
def create_app():
    app=Flask(__name__)

    @app.route('/')
    def main_page():
        return 'Hello,SSUNIVERSE'

    return app