from app import app

@app.route('/')
def index():
	return 'Hello Inpin!'

if __name__ == "__main__":
    app.run()