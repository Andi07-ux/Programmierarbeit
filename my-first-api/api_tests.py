import requests

URL = "http://127.0.0.1:8000/"

def test_get_root():
    response = requests.get(URL)
    response.status_code = 200
    if response.status_code == 200: 
        print ("GET / - Success") 
    else:
        print ("GET / - Failed")
    
    if response.json()["title"] == "title":
        print ("POST /notes/  -  TITLE MATCHES")
    else:
        print ("POST /notes/  -  TITLE DOES NOT MATCH")

def test_post_creation():
    payload = {
        "title": "title", 
        "content": "content",
        "category": "category",
        "tags": ["tag1", "tag2"]
        }
    response = requests.post(URL + "posts/", json=payload)
    print(response.status_code)
    print(response.json()) 

if __name__ == "__main__":
    test_get_root()