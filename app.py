from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")
flaskAppInstance = Flask(__name__)  # extansiating flask, like app=express()
if __name__ == '__main__':  # this is so the code inside the if block will run
    logger.debug("Starting the app")
    from api import *
    flaskAppInstance.run(host="0.0.0.0", port=3000,
                         debug=True, use_reloader=True)
# this block is the start function,host is all servers, debug mode is on, reloder is like nodemon, don't forget that true or false need to be capitalized to be a boolean
