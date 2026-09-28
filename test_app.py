from app import get_status

def test_status():
    data = get_status()
    assert data["status"] == "success"
    assert data["environment"] == "production"
    print("All functional assertions passed.")

if __name__ == '__main__':
    test_status()
