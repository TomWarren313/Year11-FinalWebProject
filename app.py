from bottle import route, run, template, view, static_file
#test
@route('/')
@view('home')
def home():
    return {}

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True )