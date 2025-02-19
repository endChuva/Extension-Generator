import os

def criar_arquivo(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

def criar_extensao():
    nome_extensao = input("Digite o nome da extensão: ")
    versao = input("Digite a versão da extensão (ex: 1.0): ")
    descricao = input("Digite a descrição da extensão: ")

    imagem_substituta = input("Digite a URL da imagem substituta: ").strip()
    if not imagem_substituta:
        print("Você deve fornecer uma URL de imagem substituta!")
        return

    pasta_extensao = nome_extensao.replace(" ", "_")
    os.makedirs(pasta_extensao, exist_ok=True)

    manifest = f"""
{{
  "manifest_version": 3,
  "name": "{nome_extensao}",
  "version": "{versao}",
  "description": "{descricao}",
  "permissions": ["activeTab", "scripting"],
  "content_scripts": [
    {{
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "run_at": "document_end" // Garante que o script seja executado após o carregamento da página
    }}
  ],
  "icons": {{
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  }}
}}
"""
    criar_arquivo(os.path.join(pasta_extensao, "manifest.json"), manifest.strip())

    content_js = f"""
// Função para substituir imagens
function substituirImagens() {{
    const imagens = document.querySelectorAll("img");
    imagens.forEach(img => {{
        if (!img.dataset.substituido) {{
            img.src = "{imagem_substituta}";
            img.dataset.substituido = true; // Marca a imagem como substituída
        }}
    }});
}}

// Observa mudanças no DOM
const observer = new MutationObserver((mutations) => {{
    mutations.forEach(mutation => {{
        // Verifica se novos nós foram adicionados
        if (mutation.type === "childList") {{
            mutation.addedNodes.forEach(node => {{
                // Se o nó for uma imagem, substitui
                if (node.tagName === "IMG") {{
                    node.src = "{imagem_substituta}";
                    node.dataset.substituido = true;
                }}
                // Se o nó contiver imagens, substitui todas
                if (node.querySelectorAll) {{
                    const novasImagens = node.querySelectorAll("img");
                    novasImagens.forEach(img => {{
                        if (!img.dataset.substituido) {{
                            img.src = "{imagem_substituta}";
                            img.dataset.substituido = true;
                        }}
                    }});
                }}
            }});
        }}
    }});
}});

// Configura o observer para observar mudanças no DOM
observer.observe(document.body, {{
    childList: true, // Observa adição de nós filhos
    subtree: true // Observa toda a árvore do DOM
}});

// Executa a substituição inicial
substituirImagens();
"""
    criar_arquivo(os.path.join(pasta_extensao, "content.js"), content_js.strip())

    from PIL import Image
    def criar_icone(tamanho, caminho):
        imagem = Image.new("RGB", (tamanho, tamanho), "white")
        imagem.save(caminho)
    criar_icone(16, os.path.join(pasta_extensao, "icon16.png"))
    criar_icone(48, os.path.join(pasta_extensao, "icon48.png"))
    criar_icone(128, os.path.join(pasta_extensao, "icon128.png"))

    readme = f"""
COMO USAR A EXTENSÃO "{nome_extensao}"

1. **Carregar a Extensão no Chrome:**
   - Abra o Chrome e vá para `chrome://extensions/`.
   - Ative o "Modo de Desenvolvedor" no canto superior direito.
   - Clique em "Carregar sem compactação" e selecione a pasta "{pasta_extensao}".

2. **Funcionamento:**
   - A extensão substituirá automaticamente todas as imagens das páginas carregadas pela imagem:
     {imagem_substituta}
   - Ela também substituirá novas imagens carregadas dinamicamente (por exemplo, ao rolar a página).

3. **Observações:**
   - Certifique-se de que a URL da imagem substituta seja acessível publicamente.
   - A extensão funciona em todas as páginas carregadas após a ativação.
"""
    criar_arquivo(os.path.join(pasta_extensao, "README.txt"), readme.strip())

    print(f"\nExtensão '{nome_extensao}' criada com sucesso na pasta '{pasta_extensao}'!")
    print("Siga as instruções no arquivo README.txt para carregar e usar a extensão no Chrome.")

if __name__ == "__main__":
    criar_extensao()