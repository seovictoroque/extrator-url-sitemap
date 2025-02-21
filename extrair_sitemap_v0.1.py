# Bibliotecas
import requests
from bs4 import BeautifulSoup
import time  

# Função para extrair URLs de uma página do sitemap, altere a URL para o site que deseja
def extract_urls_from_sitemap(page_number):
    sitemap_url = f"https://www.site.com.br/sitemap/products/{page_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        # Fazendo a requisição HTTP com o cabeçalho
        response = requests.get(sitemap_url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "xml")
            urls = [url.text for url in soup.find_all("loc")]
            return urls
        else:
            print(f"Erro ao acessar o sitemap {page_number}: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Erro na requisição do sitemap {page_number}: {e}")
        return []

# Função principal
def main():
    total_pages = 190
    all_urls = []

    # Loop para processar todas as páginas do sitemap
    for page in range(1, total_pages + 1):
        print(f"Processando sitemap {page}...")
        urls = extract_urls_from_sitemap(page)
        if urls:  # Verifica se a lista de URLs não está vazia
            all_urls.extend(urls)
            print(f"Extraídas {len(urls)} URLs da página {page}")
        else:
            print(f"Nenhuma URL encontrada na página {page} ou erro ao acessar.")

        # Delay de 1 segundo entre as requisições
        time.sleep(1)

    # Salva todas as URLs em um único arquivo
    # Altere "all_sitemap_urls.txt" pelo nome que deseja
    with open("all_sitemap_urls.txt", "w") as f:
        for url in all_urls:
            f.write(url + "\n")

    print(f"Total de URLs extraídas: {len(all_urls)}. Salvas no arquivo all_sitemap_urls.txt")

if __name__ == "__main__":
    main()
