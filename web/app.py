"""
Vladimir Shatalov Flask API
"""
import config
from flask import Flask, render_template, abort, send_from_directory  #importing stuff

app = Flask(__name__)                                   #dont know what this does


@app.route("/<DOCROOT:filename>")                       #rounting the request
def request_handler(filename):                          #function for handling the request
    forbidden = ['//', '~', '..']                       # making a list of forbidden characters
    if any(x in filename for x in forbidden):           #reused from P1, if any forbidden combinations in filename
        abort(403)                                      #aborting with a 403 error

    DOCROOT = config.configuration().DOCROOT            #otherwise we get the DOCROOT from the config file
    return send_from_directory(DOCROOT, filename), 200  #and then the file from DOCROOT directory

@app.errorhandler(403)                                  #error handler for a 403 error
def forbidden_name(error):                              #function for handling the 403 error
    return render_template('403.html'), 403             #returns 403.html file from the templates folder, and a 403 code

@app.errorhandler(404)                                  #error handler for a 404 error
def file_not_found(error):                              #function for handling the 404 error
    return render_template('404.html'), 404             #returns 404.html file from the templates folder, and a 404 code


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
