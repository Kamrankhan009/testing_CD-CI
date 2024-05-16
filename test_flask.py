from app import app
import json


def test_get_all_book():
    main_res = app.test_client().get("/bookapi/books")
    response = json.loads(main_res.data)
    response = response.get("Books")
    
    assert type(response[0]) is dict
    assert type(response[1]) is dict
    
    assert response[0]['author'] == "Havard"
    assert response[0]['borrowed'] == False
    
    assert main_res.status_code == 200