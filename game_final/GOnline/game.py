from flask import Flask, render_template
app = Flask(__name__)
import gonline
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
    return gonline.main()

if __name__ == '__main__':
  app.run(debug=True)