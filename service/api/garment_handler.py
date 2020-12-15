import logging
import uuid

from flask import request
from flask_restplus import Resource

from service.domain.garment_management_interface import GarmentManagementInterface
from service.dtos.garment_dto import GarmentDTO


class GarmentHandler(Resource):
    def __init__(self: object, *args, domain: GarmentManagementInterface, **kwargs):
        logging.debug("GarmentHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def get(self: object, garment_id: uuid.UUID):
        logging.debug(f"GarmentHandler.get(garment_id={garment_id})")
        garment_dto = self.__domain.find_garment_by_id(garment_id=garment_id)
        return garment_dto.as_serialized_dict()

    def put(self: object, garment_id: uuid.UUID):
        logging.debug(f"GarmentHandler.put(garment_id={garment_id})")
        garment_data = {"id": garment_id}
        garment_data.update(request.get_json())
        garment_dto = GarmentDTO().from_dict(garment_data)
        self.__domain.update_garment(garment_dto=garment_dto)

    def delete(self: object, garment_id: uuid.UUID):
        logging.debug(f"GarmentHandler.delete(garment_id={garment_id})")
        self.__domain.remove_garment(garment_id=garment_id)
