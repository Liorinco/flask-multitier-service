from sqlalchemy import Column, DateTime, ForeignKey, func, Table
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from service.dtos.dataset_dto import DataSetDTO
from service.infrastructure.daos.dao_base import DAOBase
from service.infrastructure.daos.data_dao import DataDAO


class DataSetDAO(DAOBase):
    __tablename__ = "datasets"

    id = Column(UUID(as_uuid=True), primary_key=True)
    created_date = Column(DateTime, server_default=func.now())
    aggregates = Column(JSONB(50))
    # dataset = relationship("DataDAO", back_populates="datasets", uselist=True)
    dataset = relationship("DataDAO", secondary="datasets_data", backref="datasets", uselist=True)

    @classmethod
    def from_dto(cls: object, dataset_dto: DataSetDTO) -> object:
        return cls(
            id=dataset_dto.id,
            created_date=dataset_dto.created_date,
            aggregates=dataset_dto.aggregates,
            dataset=[DataDAO.from_dto(data_dto) for data_dto in dataset_dto.dataset]
        )

    def asdict(self: object) -> dict:
        return {
            "id": self.id,
            "created_date": self.created_date,
            "aggregates": self.aggregates,
            "dataset": self.dataset
        }

    def to_dto(self: object) -> DataSetDTO:
        return DataSetDTO().from_dict(self.asdict())


datasets_data_table = Table(
    "datasets_data",
    DAOBase.metadata,
    Column("dataset_id", UUID(as_uuid=True), ForeignKey("datasets.id"), primary_key=True),
    Column("data_id", UUID(as_uuid=True), ForeignKey("data.id"), primary_key=True)
)
