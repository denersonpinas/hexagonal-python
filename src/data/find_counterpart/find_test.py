
from faker import Faker

from src.data.find_counterpart import FindCounterpart
from src.infra.test import CounterpartRepositorySpy

faker = Faker()

def test_by_id():
    '''Testing by_id method'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'id': faker.random_number(digits=2)}
    response = find_counterpart.by_id(counterpart_id=attributes['id'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params['counterpart_id'] == attributes['id']

    # Testing Output
    assert response['Success'] is True
    assert response['Data']

def test_by_id_fail():
    '''Testing by_id method fail'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'id': faker.word()}
    response = find_counterpart.by_id(counterpart_id=attributes['id'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params == {}

    # Testing Output
    assert response['Success'] is False
    assert response['Data'] is None

def test_by_required():
    '''Testing by_required method'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'required': faker.boolean()}
    response = find_counterpart.by_required(required=attributes['required'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params['required'] == attributes['required']

    # Testing Output
    assert response['Success'] is True
    assert response['Data']

def test_by_required_fail():
    '''Testing by_required method fail'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'required': faker.word()}
    response = find_counterpart.by_required(required=attributes['required'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params == {}

    # Testing Output
    assert response['Success'] is False
    assert response['Data'] is None

def test_by_default():
    '''Testing by_default method'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'default': faker.boolean()}
    response = find_counterpart.by_default(default=attributes['default'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params['default'] == attributes['default']

    # Testing Output
    assert response['Success'] is True
    assert response['Data']

def test_by_default_fail():
    '''Testing by_default method fail'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'default': faker.word()}
    response = find_counterpart.by_default(default=attributes['default'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params == {}

    # Testing Output
    assert response['Success'] is False
    assert response['Data'] is None

def test_by_id_and_required():
    '''Testing by_id_and_required method'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'id': faker.random_number(digits=2), 'required': faker.boolean()}
    response = find_counterpart.by_id_and_required(counterpart_id=attributes['id'], required=attributes['required'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params['counterpart_id'] == attributes['id']
    assert counterpart_repo.select_counterpart_params['required'] == attributes['required']

    # Testing Output
    assert response['Success'] is True
    assert response['Data']

def test_by_id_and_required_fail():
    '''Testing by_id_and_required method fail'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'id': faker.random_number(digits=2), 'required': faker.word()}
    response = find_counterpart.by_id_and_required(counterpart_id=attributes['id'], required=attributes['required'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params == {}

    # Testing Output
    assert response['Success'] is False
    assert response['Data'] is None

def test_by_id_and_dafault():
    '''Testing by_id_and_dafault method'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'id': faker.random_number(digits=2), 'default': faker.boolean()}
    response = find_counterpart.by_id_and_default(counterpart_id=attributes['id'], default=attributes['default'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params['counterpart_id'] == attributes['id']
    assert counterpart_repo.select_counterpart_params['default'] == attributes['default']

    # Testing Output
    assert response['Success'] is True
    assert response['Data']

def test_by_id_and_dafault_fail():
    '''Testing by_id_and_dafault method fail'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'id': faker.random_number(digits=2), 'default': faker.word()}
    response = find_counterpart.by_id_and_default(counterpart_id=attributes['id'], default=attributes['default'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params == {}

    # Testing Output
    assert response['Success'] is False
    assert response['Data'] is None

def test_by_required_and_default():
    '''Testing by_required_and_default method'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'required': faker.boolean(), 'default': faker.boolean()}
    response = find_counterpart.by_required_and_default(required=attributes['required'], default=attributes['default'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params['required'] == attributes['required']
    assert counterpart_repo.select_counterpart_params['default'] == attributes['default']

    # Testing Output
    assert response['Success'] is True
    assert response['Data']

def test_by_required_and_default_fail():
    '''Testing by_required_and_default method fail'''

    counterpart_repo = CounterpartRepositorySpy()
    find_counterpart = FindCounterpart(counterpart_repository=counterpart_repo)

    attributes = {'required': faker.boolean(), 'default': faker.word()}
    response = find_counterpart.by_required_and_default(required=attributes['required'], default=attributes['default'])

    # Testing inputs
    assert counterpart_repo.select_counterpart_params == {}

    # Testing Output
    assert response['Success'] is False
    assert response['Data'] is None
