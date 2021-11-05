import flask
import requests

app = flask.Flask(__name__)

# Where to save the file
temp_filepath = '/mnt/c/users/19186/jumpcloud/jc2/tempfile.txt'

download_url = 'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'


def read_file(filepath) -> str:
    """Read the file and return its content in a single string

    Args:
        filepath (string): Path to local file

    Returns:
        string: Single line string with all lines from the file
    """
    out = ''
    with open(filepath, 'r') as file:
        for line in file:
            out += line + '\n'
    return out

# /
@app.route('/')
def index():
    return '<h1>Hello, this is the index page</h1>'

# /manage_file
@app.route('/manage_file', methods=['POST'])
def manage_file():
    # Trying to read the request data (payload)
    try:
        json_data = flask.request.json
        # {'action': 'read'} payload
        if json_data['action'] == 'read':
            try:
                return flask.Response(read_file(temp_filepath), status=200)
            except FileNotFoundError:
                # Handling potential error if file is not downloaded
                return flask.Response('No file, try to download it first', status=500)

        # {'action': 'download'} payload
        elif json_data['action'] == 'download':
            try:
                r = requests.get(download_url)
                with open(temp_filepath, 'wb') as file:
                    file.write(r.content)
                return flask.Response('File downloaded', status=200)
            except Exception:
                return flask.Response('Failed to download file', status=500)
        # Another payload that is not one of the two above
        else:
            return flask.Response('Not a valid request', status=400)
    except KeyError:
        # Another payload that is not correct
        return flask.Response('Not a valid request', status=400)


if __name__ == '__main__':
    app.run(debug=True)