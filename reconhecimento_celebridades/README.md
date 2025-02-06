# Reconhecimento de Celebridades com AWS Rekognition

Um projeto para identificar celebridades em imagens usando AWS Rekognition.

## Descrição

Este projeto utiliza o serviço AWS Rekognition para detectar e identificar celebridades em imagens. O código processa imagens e desenha caixas ao redor dos rostos reconhecidos, mostrando o nome das celebridades.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/reconhecimento-celebridades.git
    cd reconhecimento-celebridades
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/MacOS
    venv\Scripts\activate     # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Defina as variáveis de ambiente com suas credenciais da AWS:
    ```bash
    export AWS_ACCESS_KEY_ID=seu_access_key_id
    export AWS_SECRET_ACCESS_KEY=seu_secret_access_key
    export AWS_REGION=us-east-1  # Ou a região de sua preferência
    ```

2. Coloque as imagens que você deseja processar na pasta `images`.

3. Execute o script:
    ```bash
    python seu_script.py
    ```

## Estrutura do Projeto

- `seu_script.py`: Script principal que detecta celebridades e desenha caixas nas imagens.
- `images/`: Pasta onde as imagens a serem processadas devem estar.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Melhorias Feitas

1. **Uso de Variáveis de Ambiente para Credenciais**: As credenciais da AWS são armazenadas em variáveis de ambiente para melhorar a segurança.
2. **Tratamento de Exceções**: Adicionadas exceções específicas para capturar e lidar com diferentes tipos de erros.
3. **Tipagem de Retorno**: Adição de tipagem explícita de retorno para melhorar a legibilidade e manutenção do código.
4. **Desenho de Caixas em Imagens**: Caixas vermelhas são desenhadas ao redor dos rostos das celebridades reconhecidas com alta confiança, juntamente com seus nomes.

## Conclusão

Este projeto é uma introdução ao uso do AWS Rekognition para reconhecimento de celebridades em imagens. Com as melhorias feitas, o código está mais seguro, robusto e fácil de manter.
