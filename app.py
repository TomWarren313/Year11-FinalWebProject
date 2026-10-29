from bottle import route, run, template, view, static_file


@route('/')
@view('home')
def home():
    return {}

@route('/truthvsmyth')
@view('truthvsmyth')
def truth_vs_myth():
    return {}

@route('/issues')
@view('issues')
def issues():
    return {}

@route('/impacts')
@view('impacts')
def impacts():
    return {}

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./Static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True )