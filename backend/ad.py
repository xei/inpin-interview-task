from app import db, ma
from sqlalchemy import Column, DECIMAL, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_method


class Ad(db.Model):
    __tablename__ = 'ad'

    id = Column(BIGINT(20), primary_key=True)
    agency_id = Column(ForeignKey('agency.id'), nullable=False, index=True)
    name = Column(VARCHAR(45))
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8))

    agency = relationship('Agency')

    def __init__(self, agency_id, name, latitude, longitude):
        self.agency_id = agency_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


class AdSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'agency_id', 'name', 'latitude', 'longitude')


ad_schema = AdSchema()
ads_schema = AdSchema(many=True)