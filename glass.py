#!/usr/bin/env python

import datetime
import re

import sh
from flask import Flask, render_template, request, make_response

from functools import wraps

app = Flask("lg")
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/go', methods=['POST'])
def go():
    log(request)
    output = do(request.form.get('method'), request.form.get('target'))

    return render_template('index.html', results=output)


@app.route('/api')
def api():
    return render_template('api.html')

def returns_plaintext(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = f(*args, **kwargs)
        response = make_response(r)
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        return response
    return decorated_function

@app.route('/api/host/<target>')
@returns_plaintext
def api_host(target):
    print(target)
    log(request, method='host', target=target)
    return do('host', target)

@app.route('/api/iperf3/<target>')
@returns_plaintext
def api_iperf3(target):
    print(target)
    log(request, method='iperf3', target=target)
    return do('iperf3', target)

@app.route('/api/nping/<target>')
@returns_plaintext
def api_nping(target):
    print(target)
    log(request, method='nping', target=target)
    return do('nping', target)

@app.route('/api/ping/<target>')
@returns_plaintext
def api_ping(target):
    print(target)
    log(request, method='ping', target=target)
    return do('ping', target)

@app.route('/api/mtr/<target>')
@returns_plaintext
def api_mtr(target):
    log(request, method='mtr', target=target)
    return do('mtr', target=target)


def do(method, target):
    output = ''
    result = None

    target = sanitize(target)
    if target:
        if method == 'iperf3':
            result = iperf3(target)
        elif method == 'host':
            result = host(target)
        elif method == 'nping':
            result = nping(target)
        elif method == 'ping':
            result = ping(target)
        elif method == 'mtr':
            result = mtr(target)
        else:
            output = "You gave me an invalid method!"

        if result is not None:
            output = result.stderr + result.stdout
            output = result.stderr + result.stdout
    else:
        output = "Your target doesn't look like an IP address or a hostname."

    return output


def host(dest):
    return sh.unbound_host(dest, _ok_code=[0, 1, 2])

def iperf3(dest):
    # need -c for client
    return sh.iperf3('-c', dest, _ok_code=[0, 1, 2])

def ping(dest, count=10):
    return sh.ping(dest, c=count, _ok_code=[0, 1, 2])

def nping(dest, count=10):
    return sh.nping(dest, c=count, _ok_code=[0, 1, 2])

def mtr(dest, count=10):
    return sh.mtr(dest, b=True, r=True, w=True, c=count, _ok_code=[0, 1])


def sanitize(dirty_target):
    match = re.match("([\w\.\:\-\_]+)", dirty_target)
    if match:
        target = match.group(1)
    else:
        target = ''

    return target


def log(request, method=None, target=None):
    if not method:
        method = request.form.get('method')

    if not target:
        target = request.form.get('target')

    print("[{0}] {1} - {2} - {3}".format(str(datetime.datetime.now()),
                                         request.remote_addr,
                                         method,
                                         target))


if __name__ == '__main__':
    app.run()
