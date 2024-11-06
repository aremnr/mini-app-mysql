from sqlalchemy.orm import mapped_column, Mapped
from database import Base
import uuid

class MyTestTable(Base):
    __tablename__ = "maintable"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, default=uuid.uuid4())
    value: Mapped[int]
    description: Mapped[str]
    