from flask_restful import Resource
import logging as logger


class TaskBYID(Resource):
    def get(self, taskId):
        logger.debug("Inside get method of task by id")
        return {"message": "inside get method of task by id. TASK-ID = {}".format(taskId)}, 200

    def post(self, taskId):
        logger.debug("Inside post method of task by id")
        return {"message": "inside post method of task by id. TASK-ID = {}".format(taskId)}, 200

    def put(self, taskId):
        logger.debug("Inside put method of task by id")
        return {"message": "inside put method of task by id. TASK-ID = {}".format(taskId)}, 200

    def delete(self, taskId):
        logger.debug("Inside delete method of task by id")
        return {"message": "inside delete method of task by id. TASK-ID = {}".format(taskId)}, 200
