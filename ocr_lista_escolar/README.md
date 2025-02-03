# OCR Lista Escolar

Um projeto para extrair texto de listas de material escolar usando AWS Textract.

## Descrição

Este projeto utiliza o serviço AWS Textract para detectar e extrair texto de imagens de listas de material escolar. O código processa uma imagem e exibe as linhas de texto detectadas.

## Instalação

1. Clone o repositório:
   bash
        git clone https://github.com/seu-usuario/ocr-lista-escolar.git
        cd ocr-lista-escolar

2. Crie um ambiente virtual e ative-o:
    bash
        python -m venv venv
        source venv/bin/activate  # Para Linux/MacOS
        venv\Scripts\activate

3. Instale as dependências:
    pip install -r requirements.txt

## Uso
1. Defina as variáveis de ambiente com suas credenciais da AWS:
    bash
        export AWS_ACCESS_KEY_ID=seu_access_key_id
        export AWS_SECRET_ACCESS_KEY=seu_secret_access_key
        export AWS_REGION=us-east-1  # Ou a região de sua preferência

2. Coloque a imagem lista-material-escolar.jpeg na pasta images.

3. Execute o script:
    bash
        python ocr_lista_escolar.py

## Estrutura do Projeto

ocr_lista_escolar.py: Script principal que detecta e exibe o texto da imagem.

images/: Pasta onde a imagem a ser processada deve estar.

requirements.txt: Arquivo com as dependências do projeto.