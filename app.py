from flask import Flask, render_template, request
from modules import port_scanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        target_ip = request.form['target_ip']
        port_start = int(request.form['port_start'])
        port_end = int(request.form['port_end'])
        port_range = range(port_start, port_end + 1)
        results = port_scanner.start_scan(target_ip, port_range)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
