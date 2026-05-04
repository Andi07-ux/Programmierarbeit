import pytest
import requests
from faker import Faker

name_fake = Faker()

BASE_URL = "http://localhost:8000" 



def test_read_root():
    """Test the root endpoint returns the expected greeting message."""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello World!"

def test_check_404_Error():
    """Test that requesting a non-existent endpoint returns a 404 error."""
    response = requests.get(f"{BASE_URL}/nonexistent")
    assert response.status_code == 404

def test_check_greetings():
    """Test the personalized greeting endpoint with a sample name."""
    for _ in range(10):
        name = name_fake.first_name()
        response = requests.get(f"{BASE_URL}/greetings/{name}")
        assert response.status_code == 200
        assert response.json()["message"] == f"Hello {name}!"

def test_is_adult():
    """Test if Check Adult works"""
    for age in range(0, 40):
        adult = age >= 18
        response = requests.get(f"{BASE_URL}/is-adult/{age}")
        assert response.status_code == 200
        data = response.json()
        for key in ["is_adult", "can_drive", "can_vote"]:
            assert data[key] == adult
        assert data["age"] == age

def test_is_adult_negative_age():
    """Test if Adult is not negative"""
    for age in range(-20, 0):
        response = requests.get(f"{BASE_URL}/is-adult/{age}")
        assert response.status_code == 400


def test_create_note():
    """Test creating a new note"""
    note_data = {
        "title": "Hausaufgabe",
        "content": "API Tests schreiben",
        "category": "Studium",
        "tags": ["python", "pytest"]
    }
    response = requests.post(f"{BASE_URL}/notes", json=note_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Hausaufgabe"
    assert "id" in data

def test_list_notes():
    """Test listing all notes"""
    response = requests.get(f"{BASE_URL}/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_note():
    """Test updating a note (PUT)"""
    # Erst erstellen
    create_resp = requests.post(f"{BASE_URL}/notes", json={
        "title": "Original", "content": "Text", "category": "Test", "tags": []
    })
    note_id = create_resp.json()["id"]
    
    # Update durchführen
    updated_data = {
        "title": "Updated Title",
        "content": "Updated content",
        "category": "Updated",
        "tags": ["updated"]
    }
    response = requests.put(f"{BASE_URL}/notes/{note_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_delete_note():
    """Test deleting a note"""
    create_resp = requests.post(f"{BASE_URL}/notes", json={
        "title": "To Delete", "content": "...", "category": "Test", "tags": []
    })
    note_id = create_resp.json()["id"]
    
    # Löschen
    del_response = requests.delete(f"{BASE_URL}/notes/{note_id}")
    assert del_response.status_code in [200, 204]
    
    # Verifizieren
    get_resp = requests.get(f"{BASE_URL}/notes/{note_id}")
    assert get_resp.status_code == 404

def test_filter_by_category():
    """Test filtering notes by category"""
    category = "Work"
    requests.post(f"{BASE_URL}/notes", json={
        "title": "Job", "content": "Task", "category": category, "tags": []
    })
    response = requests.get(f"{BASE_URL}/notes?category={category}")
    assert response.status_code == 200
    for note in response.json():
        assert note["category"] == category

def test_create_note_missing_field():
    """Test validation error (422)"""
    invalid_note = {"title": "Missing fields"} # Content & Category fehlen
    response = requests.post(f"{BASE_URL}/notes", json=invalid_note)
    assert response.status_code == 422

def test_notes_statistics():
    """Test GET /notes/stats endpoint"""
    response = requests.get(f"{BASE_URL}/notes/stats")
    assert response.status_code == 200
    assert "total_notes" in response.json()

def test_patch_note_title_only():
    """Test partial update via PATCH"""
    create_resp = requests.post(f"{BASE_URL}/notes", json={
        "title": "Old", "content": "Stay", "category": "Test", "tags": []
    })
    note_id = create_resp.json()["id"]
    
    response = requests.patch(f"{BASE_URL}/notes/{note_id}", json={"title": "New"})
    assert response.status_code == 200
    assert response.json()["title"] == "New"
    assert response.json()["content"] == "Stay"
 