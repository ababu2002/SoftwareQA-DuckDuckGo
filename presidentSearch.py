import requests

url_ddg = "https://api.duckduckgo.com"

PresidentNames = ["Adams"
,"Adams"
,"Arthur"
,"Biden"
,"Buchanan"
,"Bush"
,"Bush"
,"Carter"
,"Cleveland"
,"Clinton"
,"Coolidge"
,"Eisenhower"
,"Fillmore"
,"Ford"
,"Garfield"
,"Grant"
,"Harding"
,"Harrison"
,"Harrison"
,"Hayes"
,"Hoover"
,"Jackson"
,"Jefferson"
,"Johnson"
,"Johnson"
,"Kennedy"
,"Lincoln"
,"Madison"
,"McKinley"
,"Monroe"
,"Nixon"
,"Obama"
,"Pierce"
,"Polk"
,"Reagan"
,"Roosevelt"
,"Roosevelt"
,"Taft"
,"Taylor"
,"Truman"
,"Trump"
,"Tyler"
,"Van Buren"
,"Washington"
,"Wilson"]

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    print(rsp_data["RelatedTopics"])
    for topic in rsp_data["RelatedTopics"]:
        for president in PresidentNames:
            if president in topic["Result"]:
                PresidentNames.remove(president)
    assert PresidentNames == []
