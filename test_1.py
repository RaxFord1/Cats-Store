from main import db, Cat, User
from datetime import datetime, date
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestDBMethods(unittest.TestCase):
    
    def test_insert(self):
        cat = Cat(name="test", description="Первый счастливчик в нашей маленькой воображаемой семье",
               class_type="A", gender=0, available=0, color="red",
               birthday=date(2002, 2, 17)
            )
        user = User(first_name="test", last_name="test", email="test@test",
                    phone_number="test", gender=0, birthday=date(2002, 2, 17), city="Mykolaiv")

        try:
            db.session.add(cat)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            self.assertRaises(Exception, msg=f'Couldnt insert {e}')

    def test_have(self):
        try:
            cat = Cat.query.filter_by(name="test").one()
        except NoResultFound as e:
            self.assertRaises(NoResultFound, msg=f'{e}')
        except Exception as e:
            self.assertRaises(Exception, msg=f'{e}')

    def test_crash(self):
        self.assertTrue('Foo'.isupper())