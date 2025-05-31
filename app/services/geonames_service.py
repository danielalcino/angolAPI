import requests

# Dicionário com as províncias de Angola e suas capitais
CAPITAIS = {
    "Bengo": "Caxito",
    "Benguela": "Benguela",
    "Bié": "Kuito",
    "Cabinda": "Cabinda",
    "Cuando Cubango": "Menongue",
    "Cuanza Norte": "Ndalatando",
    "Cuanza Sul": "Sumbe",
    "Cunene": "Ondjiva",
    "Huambo": "Huambo",
    "Huíla": "Lubango",
    "Luanda": "Luanda",
    "Lunda Norte": "Dundo",
    "Lunda Sul": "Saurimo",
    "Malanje": "Malanje",
    "Moxico": "Luena",
    "Namibe": "Moçâmedes",
    "Uíge": "Uíge",
    "Zaire": "M'banza Kongo",
    # Caso queira incluir outras regiões (ex. cidades que aparecem no JSON)
    "Cassongue": "Cassongue",
    "Cacuso": "Cacuso",
    "Luena Norte": "Lucusse",
    "Lumbala Nguimbo": "Lumbala Nguimbo",
    "Luengue": "Luengue"
}

def buscar_provincias_geonames(username: str):
    url = "http://api.geonames.org/searchJSON"
    params = {
        "country": "AO",
        "featureCode": "ADM1",
        "maxRows": 50,
        "username": username
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        dados = response.json()
        provincias = []
        for item in dados.get("geonames", []):
            nome = item.get("name")
            provincias.append({
                "nome": nome,
                "capital": CAPITAIS.get(nome, "N/D"),  # Capital do dicionário ou "N/D" (não disponível)
                "latitude": item.get("lat"),
                "longitude": item.get("lng")
            })
        return provincias
    else:
        return []
