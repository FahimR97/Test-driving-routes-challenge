import json

# Tests for your routes go here

"""
When I send a request GET /wave?name=Dana
I expect the status code to be 200 ok 
And the reponse to be 'I am waving at Dana;
"""
def test_get_wave_with_argument(web_client):
    response = web_client.get('/wave?name=Dana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "I am waving at Dana"


"""
When I send a request POST / submit 
with arguments name = 'Dana' and message = "Hello"
I expect the status code to be 200 ok 
And the response to be "Thanks Dana, you sent this message: 'Hello'"
"""

def test_post_submit_with_arguments(web_client):
    response = web_client.post('/submit', data = {
        'name': 'Dana',
        'message': 'Hello'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message:"Hello"'

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'
""" 
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""


def test_post_sort_names_in_list_of_names(web_client):
    response = web_client.post("/sort-names", data ={
        "names": "Joe,Alice,Zoe,Julia,Kieran"
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

""" 
When I make a GET request to /names
I should get a 200 response
I should receive names which are in a predetermined list called current names
The name I have included should be added
"""

def test_get_add_name(web_client):
    response = web_client.get('/names?add=Eddie')
    names_expected = ['Julia','Alice','Karim','Eddie']
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == names_expected


