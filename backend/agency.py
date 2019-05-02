from app import db, ma
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.orm import relationship


class Agency(db.Model):
    __tablename__ = 'agency'

    id = Column(BIGINT(20), primary_key=True)
    parent_id = Column(ForeignKey('agency.id'), index=True)
    name = Column(VARCHAR(45))

    parent = relationship('Agency', remote_side=[id])

    def __init__(self, name, parent_id):
        self.parent_id = parent_id
        self.name = name


class AgencySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'parent_id', 'name')


agency_schema = AgencySchema()
agencies_schema = AgencySchema(many=True)