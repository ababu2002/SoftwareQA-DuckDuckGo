import requests

url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    print(rsp_data)
    assert "DuckDuckGo" in rsp_data["Heading"]