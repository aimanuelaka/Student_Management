
def test_access_notes_average(client):
    client.post("/auth/login", data={"username": "user", "password": "user123"}, follow_redirects=True)
    res = client.get("/notes/averages")
    assert res.status_code == 200

def test_redirect_anonymous_to_login(client):
    res = client.get("/admin/dashboard", follow_redirects=True)
    assert b"Login" in res.data
