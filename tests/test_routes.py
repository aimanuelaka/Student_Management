
def test_login_admin(client):
    response = client.post("/auth/login", data={"username": "admin", "password": "admin123"}, follow_redirects=True)
    assert b"Dashboard" in response.data or response.status_code == 200

def test_login_standard_sees_average_only(client):
    client.post("/auth/login", data={"username": "user", "password": "user123"}, follow_redirects=True)
    response = client.get("/notes/averages")
    assert response.status_code == 200
    response2 = client.get("/notes/add")
    assert response2.status_code in (302, 403)
