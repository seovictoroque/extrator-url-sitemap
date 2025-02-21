# Extrator de URL para sitemap

Este script em Python foi criado para extrair todas as URLs de um ou mais sitemaps e salvá-las em um arquivo de texto ou XML. O principal objetivo do código é acessar o sitemap, coletar as URLs presentes nas tags <loc> e armazená-las em um arquivo para análise futura. Essa funcionalidade é particularmente útil em contextos como grandes e-commerces, onde é essencial verificar e gerenciar um grande número de páginas listadas no sitemap, garantindo posteriormente que estejam funcionando corretamente e indexadas de maneira adequada.

## Funcionalidades

- Acessa múltiplos arquivos de sitemap paginados
- Extrai todas as URLs dos sitemaps
- Salva as URLs extraídas em um arquivo `.txt`
- Adiciona um delay para evitar bloqueios

---

## Como usar o Sitemap URL Extractor

### 1. Pré-requisitos

Antes de executar o script, certifique-se de ter o Python instalado. Se não tiver o Python instalado, baixe-o [aqui](https://www.python.org/downloads/).

- **Python 3.6+**
- **Pip** (gerenciador de pacotes do Python)

### 2. Instalar dependências

### **Instalar o lxml**

No **VS Code**, abra o terminal e execute:

```bash
pip install lxml
```

Abra o terminal e execute:

```bash
pip install -r requirements.txt
```

> Se o arquivo requirements.txt não existir, instale manualmente:
> 

```bash
pip install requests beautifulsoup4
```

### 3. Executar o script

Para rodar o script, use:

```bash
python extrair_sitemap.py
```

Isso processará todas as páginas do sitemap e salvará as URLs em `all_sitemap_urls.txt`.

---

## <Código>

```python
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
```

---

## Estrutura do Projeto

```
📁 extrator_sitemap/
│── extrair_sitemap.py   # Script principal
│── requirements.txt     # Dependências do projeto
│── all_sitemap_urls.txt # Saída com as URLs extraídas
│── README.md            # Documentação
```

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um **fork** do repositório
2. Crie um **branch** (`git checkout -b minha-feature`)
3. Faça commit das mudanças (`git commit -m 'Adicionando nova feature'`)
4. Faça push para o branch (`git push origin minha-feature`)
5. Abra um **Pull Request**

---

## Licença

Este projeto é licenciado sob a **MIT License**. Sinta-se livre para utilizá-lo e modificá-lo. 

---

## Contato

Se tiver dúvidas ou sugestões, entre em contato:

- **E-mail:** seovictoroque@email.com
- X (twitter) **:** [@seovictor](https://x.com/seovictoroque)