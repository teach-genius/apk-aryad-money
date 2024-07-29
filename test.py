import requests

# Les cookies de session obtenus à partir de la connexion
cookies = {
    'session_token': '3d23fa073262f07b273795dc77faac0801d217da23a9ada8061a7c9899a991ac',
    'username': 'farya'
}

cookies2 = {
'b_user':'61561065616257',
'c_user':'100075454100402',	
'datr':'IrFoZpQUFSrqtRcOYRjsKy6E',
'dpr':'1.5',
'fr':'0E9CllOuyj1SJS1zg.AWUmNppLkmv7PggwCR5qCUvU4v4.Bmpypx..AAA.0.0.Bmpypx.AWX02btREgA',
'oo':'v1',
'presence':'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1722231415617%2C%22v%22%3A1%7D',		
'sb':'IrFoZh_p0KwHonFcKu3uKB62',
'usida':'eyJ2ZXIiOjEsImlkIjoiQXNoOXdwaGdmcGJnYyIsInRpbWUiOjE3MjIwNjkwNDB9',	
'wd':'150x585',	
'xs':'42%3AaSMRgS4wGtKDsA%3A2%3A1718137128%3A-1%3A3106%3ANq4xscrcnaYB6A%3AAcX43FluDZCQWELX4HXc74UYw0XYDWLDwsnszRQKyg'

}
url2 = 'https://web.facebook.com/?_rdc=1&_rdr'

# URL de la ressource protégée
url = 'http://localhost:8000/dashboard'

# Faire une requête avec les cookies
response = requests.get(url2, cookies=cookies2)

# Afficher la réponse
print(response.text)
