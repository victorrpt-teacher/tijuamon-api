# tiny entry point to run the app
from src import create_app

# create the app using the factory function
app = create_app()

# run the app
if __name__ == "__main__":
    app.run(debug=True)