from sqlalchemy.orm import Session
from database.create_db import Stock
from database.connect_db import engine
from sqlalchemy import and_

local_session = Session(bind=engine)


def item_all():
    """Вывод всех записей"""
    temp_list = []
    with local_session as session:
        for item in session.query(Stock).filter(Stock.status == 1).order_by(Stock.id.desc()).all():
            temp_list.append(item)

    return temp_list


def create_item(title, invent, count, price):
    """Добавление записи в БД"""
    with local_session as session:
        stock = Stock()
        stock.title = title
        stock.inventary_num = invent
        stock.count = count
        stock.price = price
        session.add(stock)
        session.commit()


def search_item(value):
    """Поиск записи в БД"""
    temp_list = []
    with local_session as session:
        results = session.query(Stock).filter(and_(Stock.title.like(f'%{value}%'), Stock.status == 1)).order_by(
            Stock.id.desc()).all()
        for item in results:
            temp_list.append(item)
    return temp_list


def update_item(pk, title, invent, count, price):
    """Обновляет запись из БД"""
    with local_session as session:
        result = session.query(Stock).filter(Stock.id == pk).first()
        date = result.date
        result.title = title
        result.inventary_num = invent
        result.count = count
        result.price = price
        result.date = date
        session.commit()


def delete_item(pk):
    """Удаляем запись из БД"""
    with local_session as session:
        result = session.query(Stock).filter(Stock.id == pk).first()
        session.delete(result)
        session.commit()
