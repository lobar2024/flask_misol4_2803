from flask import Flask, render_template

app = Flask(__name__)

# 4
@app.route('/colors')
def colors_page():
    colors = ['Qizil', 'Sariq', 'Oq', 'Qora']
    return render_template('colors.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
