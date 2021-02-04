import http
import logging

import pydantic
from flask import request, Response
from flask_restplus import Resource

from service.api import datasets_models
from service.domain.dataset_management_interface import DatasetManagementInterface


class DatasetsHandler(Resource):
    def __init__(self: object, *args, domain: DatasetManagementInterface, **kwargs):
        logging.debug("DatasetsHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def post(self: object):
        logging.debug("DatasetsHandler.post")
        try:
            input_data = datasets_models.POSTDatasetsInput(**request.get_json()).dict()
        except pydantic.ValidationError as e:
            return Response(
                response=e.json(),
                status=http.HTTPStatus.UNPROCESSABLE_ENTITY,
                mimetype="application/json",
            )
        self.__domain.register_dataset(dataset=input_data["dataset"])
        return Response(status=http.HTTPStatus.CREATED)
