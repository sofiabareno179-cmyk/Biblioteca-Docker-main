def test_index(client):
    response = client.get('/cloans/')
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data

def test_add_computer_loan(client, computer, user):
    response = client.post('/cloans/add', data={
        'computerId': computer.idComputer,
        'userId': user.idUser
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Model' in response.data

def test_edit_computer_loan(client, computer_loan):
    response = client.get(f'/cloans/update/{computer_loan.idLoan}')
    assert response.status_code == 200
    assert b'Editar Pr' in response.data

def test_return_computer_loan(client, computer_loan):
    response = client.post(f'/cloans/return/{computer_loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data

def test_delete_computer_loan(client, computer_loan):
    response = client.post(f'/cloans/delete/{computer_loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr' in response.data