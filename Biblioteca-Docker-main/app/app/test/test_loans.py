def test_index(client):
    response = client.get('/Loan/')
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data

def test_add_loan(client, book, user):
    response = client.post('/Loan/add', data={
        'bookId': book.idBook,
        'userId': user.idUser
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Book' in response.data

def test_edit_loan(client, loan):
    response = client.post(f'/Loan/edit/{loan.idLoan}', data={
        'returnDate': '2030-01-01',
        'fine': '0',
        'status': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data

def test_return_loan(client, loan):
    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data

def test_delete_loan(client, loan):
    response = client.get(f'/Loan/delete/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data