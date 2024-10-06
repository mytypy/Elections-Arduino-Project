from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from urls import Urls


idpk = Annotated[str, 256, mapped_column(primary_key=True)]
str256 = Annotated[str, 256]


class Model(DeclarativeBase): # Нужно для того
    type_annotation_map = {
        str256: String(256),
        idpk: String(256)
    }
    

class User(Model):
    __tablename__ = 'user'

    idCard: Mapped[idpk]
    to_election = relationship('UserElection', back_populates='to_user', lazy='joined')
    

class UserElection(Model):
    __tablename__ = 'user_elections'
    
    idCard: Mapped[idpk] = mapped_column(ForeignKey('user.idCard', ondelete='RESTRICT'))
    election: Mapped[int] = mapped_column(ForeignKey('elections.id', ondelete='RESTRICT'))
    choose: Mapped[int] = mapped_column(ForeignKey('elections_choose.id', ondelete='RESTRICT'))
    
    election_id = relationship('Elections', back_populates='to_user_election_id', lazy='joined')
    
    choose_id = relationship('ElectionsChoose', back_populates='to_user_choose_id', lazy='joined')
    
    to_user = relationship('User', back_populates='to_election')
    

class Elections(Model):
    __tablename__ = 'elections'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str256]
    to_user_election_id = relationship('UserElection', back_populates='election_id')


class ElectionsChoose(Model):
    __tablename__ = 'elections_choose'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str256]
    election_id: Mapped[int]
    
    to_user_choose_id = relationship('UserElection', back_populates='choose_id')


# urls = Urls('simple')
# Model.metadata.create_all(urls.engine)