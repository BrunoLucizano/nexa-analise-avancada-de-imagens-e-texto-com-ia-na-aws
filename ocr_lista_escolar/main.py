import json
import os
from pathlib import Path
from typing import List

import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef


def detect_file_text(file_path: str) -> DetectDocumentTextResponseTypeDef:
    """
    Detecta texto em um documento usando o AWS Textract.

    Args:
        file_path (str): Caminho do arquivo de imagem a ser processado.

    Returns:
        DetectDocumentTextResponseTypeDef: Resposta do Textract contendo os blocos de texto detectados.
    """
    # Configura o cliente do Textract usando variáveis de ambiente
    client = boto3.client(
        "textract",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "us-east-1")  # Define uma região padrão
    )

    with open(file_path, "rb") as f:
        document_bytes = f.read()

    try:
        response = client.detect_document_text(Document={"Bytes": document_bytes})
        return response
    except ClientError as e:
        print(f"Erro processando documento: {e}")
        return {}


def get_lines(response: DetectDocumentTextResponseTypeDef) -> List[str]:
    """
    Extrai as linhas de texto da resposta do Textract.

    Args:
        response (DetectDocumentTextResponseTypeDef): Resposta do Textract.

    Returns:
        List[str]: Lista de linhas de texto detectadas.
    """
    blocks = response.get("Blocks", [])
    return [block["Text"] for block in blocks if block["BlockType"] == "LINE"]  # type: ignore


if __name__ == "__main__":
    # Define o caminho do arquivo de imagem
    file_path = str(Path(__file__).resolve().parent / "images" / "lista-material-escolar.jpeg")

    # Detecta o texto no arquivo
    response = detect_file_text(file_path)

    # Exibe as linhas de texto detectadas
    for line in get_lines(response):
        print(line)