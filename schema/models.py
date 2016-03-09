# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from . import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(15), nullable=False)


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=True)


class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    paid_amount = Column(Integer, nullable=False)
    sold_at = Column(DateTime, nullable=False)
