from src.models import create_app
#File to run three different enpoints
app = create_app()
if __name__ == '__main__':
  app.run(debug=True)