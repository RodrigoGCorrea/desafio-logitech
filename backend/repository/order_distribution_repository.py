from fastapi import Depends
from sqlalchemy.orm import Session

from database.postgres import get_db
from entity import OrderDistributionEntity
from repository.generic_repository import GenericRepository


class OrderDistributionRepository(GenericRepository[OrderDistributionEntity]):
    def __init__(self, db: Session):
        super().__init__(db, OrderDistributionEntity)


def get_order_distribution_repository(
    db: Session = Depends(get_db),
) -> OrderDistributionRepository:
    return OrderDistributionRepository(db)
