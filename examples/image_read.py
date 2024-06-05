from flask import Flask, send_file, abort
import os

app = Flask(__name__)

IMAGE_DIRECTORY = os.path.join(os.getcwd(), 'images')

@app.route('/image/<filename>')
def get_image(filename):
    file_path = os.path.join(IMAGE_DIRECTORY, filename)
    
    try:
        return send_file(file_path)
    except FileNotFoundError:
        abort(404, description="Resource not found")
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=True)
