import requests
from bs4 import BeautifulSoup

# URL do Sitemap
sitemap_url = "https://www.site.com.br/sitemap/products/1"

# Cabeçalho para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Fazendo a requisição HTTP com o cabeçalho
response = requests.get(sitemap_url, headers=headers)

# Se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")
    urls = [url.text for url in soup.find_all("loc")]

    # Salvando em um arquivo
    with open("sitemap_urls.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")

    print(f"Extraídas {len(urls)} URLs e salvas no arquivo sitemap_urls.txt")
else:
    print(f"Erro ao acessar o sitemap: {response.status_code}")
