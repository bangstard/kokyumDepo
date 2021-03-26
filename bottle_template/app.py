from bottle import run
import bottle
import os
import sys
# routes contains the HTTP handlers for our server and must be imported.
import routes



if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

    port = os.environ.get('PORT', 5000)

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    # Starts a local test server.
    #Ok
    
    run(host='localhost', port=port, reloader = True, debug=True)
