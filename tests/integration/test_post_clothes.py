import uuid

from tests import tools


def test_create_garment(client, garment_dto, garment_repository):
    exepected_garment_dict = garment_dto.as_serialized_dict()
    payload = {
        "garment_article": exepected_garment_dict["article"],
        "garment_color": exepected_garment_dict["color"],
    }
    response = client.post("/clothes", json=payload)

    assert response.status_code == 200
    assert "garment_id" in response.json
    retrieved_garment_uuid = response.json["garment_id"]
    assert tools.is_uuid(retrieved_garment_uuid)
    garment_dtos = garment_repository.find_clothes()
    garment_dto.id = uuid.UUID(retrieved_garment_uuid)
    assert garment_dtos == [garment_dto]
