from flask import render_template, request, current_app as app
from .scanner.scanner import scan_ports, get_os


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    results = scan_ports(target)
    return render_template('results.html', results=results, get_os=get_os)
