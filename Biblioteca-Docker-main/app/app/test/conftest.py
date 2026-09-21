from app import create_app, db
import pytest

from app.models.authors import Author
from app.models.books import Book
from app.models.cloans import ComputerLoan
from app.models.computers import Computer
from app.models.loans import Loan
from app.models.rooms import Room

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables within the context
        yield app
        db.session.remove()  # Cleanup session objects
        db.drop_all()
  

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    from app.models.users import User
    user = User(nameUser="test_user", passwordUser="test_password")
    db.session.add(user)
    db.session.commit()  # Commit changes within the context
    yield user
    # Cleanup changes within the context


@pytest.fixture
def author(app):
    author = Author(
        nameAuthor="Test Author",
        nationalityAuthor="Test Nationality",
    )
    db.session.add(author)
    db.session.commit()
    return author


@pytest.fixture
def book(app, author):
    book = Book(titleBook="Test Book", author=author)
    db.session.add(book)
    db.session.commit()
    return book


@pytest.fixture
def computer(app):
    computer = Computer(
        brandComputer="Test Brand",
        modelComputer="Test Model",
        statusComputer="Active",
    )
    db.session.add(computer)
    db.session.commit()
    return computer


@pytest.fixture
def room(app):
    room = Room(name="Test Room", description="Test Description")
    db.session.add(room)
    db.session.commit()
    return room


@pytest.fixture
def loan(app, book, user):
    from datetime import datetime, timedelta

    loan = Loan(
        book=book,
        user=user,
        returnDate=datetime.utcnow() + timedelta(days=14),
    )
    db.session.add(loan)
    db.session.commit()
    return loan


@pytest.fixture
def computer_loan(app, computer, user):
    from datetime import datetime, timedelta

    computer_loan = ComputerLoan(
        computer=computer,
        user=user,
        loanDate=datetime.utcnow(),
        returnDate=datetime.utcnow() + timedelta(days=1),
        status="Active",
    )
    db.session.add(computer_loan)
    db.session.commit()
    return computer_loan