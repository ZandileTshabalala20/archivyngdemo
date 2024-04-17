<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
=======
import os

# Print Hello, World!
print("Hello, World!")

# Print the current directory
print("Current Dir is: ", os.getcwd())

# List the contents of the current directory
print(os.listdir())

# Print Docker is set
print("Docker is set")

# Print the image URL
docker_image_url = "https://1.bp.blogspot.com/-Q86XGVJahug/Xm-aQfgtuMI/AAAAAAAAAcA/qqPQeihI39EbG2N87jG65xfnCdvF85-WQCLcBGAsYHQ/s1600/docker.png"
print("Docker image URL:", docker_image_url)
>>>>>>> 6c582d1e76c3a9a0cd1cd8f0ca511147e386b513
