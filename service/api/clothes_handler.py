import logging

from flask import request
from flask_restplus import Resource

from service.domain.garment_management_interface import GarmentManagementInterface
from service.dtos.color import Color
from service.dtos.garment_dto import GarmentArticle


class ClothesHandler(Resource):
    def __init__(self: object, *args, domain: GarmentManagementInterface, **kwargs):
        logging.debug("ClothesHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def post(self: object):
        logging.debug("ClothesHandler.post")
        json_data = request.get_json()
        json_data["garment_article"] = GarmentArticle(json_data["garment_article"])
        json_data["garment_color"] = Color(json_data["garment_color"])
        garment_id = self.__domain.register_garment(**json_data)
        return {"garment_id": str(garment_id)}

    def get(self: object):
        logging.debug("ClothesHandler.get")
        garment_dtos = self.__domain.find_clothes()
        return {
            "clothes": [garment_dto.as_serialized_dict() for garment_dto in garment_dtos]
        }
