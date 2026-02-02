import os

# --- CONFIGURAÇÃO ---
usuario = "INCOVIArep"
repositorio = "image"
branch = "main" # Se der erro de link quebrado, tente trocar por "master"

# Base da URL do GitHub para arquivos RAW (que o Excel aceita)
base_url = f"https://raw.githubusercontent.com/{usuario}/{repositorio}/{branch}/"

print(f"--- INICIANDO GERADOR DE LINKS ---")
print(f"Repo: {base_url}")

# Nome do arquivo de saída
arquivo_saida = "links_para_excel.csv"

# Abre o arquivo para escrita (encoding utf-8 para aceitar acentos se houver)
with open(arquivo_saida, "w", encoding="utf-8") as f:
    # Escreve o cabeçalho das colunas (Ponto e vírgula é o padrão do Excel BR)
    f.write("Nome do Arquivo;Link do GitHub;Formula Excel\n")
    
    contador = 0
    
    # Varre todos os arquivos da pasta atual
    for arquivo in os.listdir():
        # Verifica se é imagem (adicione mais extensões se precisar)
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            
            # Monta o link final
            link_raw = base_url + arquivo
            
            # Monta a fórmula mágica do Excel
            formula = f'=IMAGEM("{link_raw}")'
            
            # Escreve a linha no CSV
            f.write(f"{arquivo};{link_raw};{formula}\n")
            contador += 1

print(f"--- CONCLUÍDO ---")
print(f"Encontrei {contador} imagens.")
print(f"Abra o arquivo '{arquivo_saida}' no Excel.")
