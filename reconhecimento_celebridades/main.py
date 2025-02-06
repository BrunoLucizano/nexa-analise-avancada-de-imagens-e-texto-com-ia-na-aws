from pathlib import Path
import boto3
from botocore.exceptions import NoCredentialsError, BotoCoreError, ClientError
from mypy_boto3_rekognition.type_defs import CelebrityTypeDef, RecognizeCelebritiesResponseTypeDef
from PIL import Image, ImageDraw, ImageFont
import os
import sys

# Configuração do cliente Rekognition com credenciais explícitas
def get_rekognition_client() -> boto3.client:
    try:
        client = boto3.client(
            "rekognition",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name="us-east-1"  # Substitua pela sua região
        )
        return client
    except NoCredentialsError:
        print("Credenciais AWS não encontradas. Configure suas credenciais.")
        sys.exit(1)
    except BotoCoreError as e:
        print(f"Erro ao configurar o cliente Rekognition: {e}")
        sys.exit(1)

client = get_rekognition_client()

# Função para obter o caminho da imagem
def get_path(file_name: str) -> str:
    return str(Path(__file__).parent / "images" / file_name)

# Função para reconhecer celebridades
def recognize_celebrities(photo: str) -> RecognizeCelebritiesResponseTypeDef:
    try:
        with open(photo, "rb") as image:
            return client.recognize_celebrities(Image={"Bytes": image.read()})
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {photo}")
        return {"CelebrityFaces": []}
    except ClientError as e:
        print(f"Erro ao chamar a API do Rekognition: {e}")
        return {"CelebrityFaces": []}

# Função para desenhar caixas e nomes nas imagens
def draw_boxes(image_path: str, output_path: str, face_details: list[CelebrityTypeDef]):
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        
        try:
            font = ImageFont.truetype("Ubuntu-R.ttf", 20)
        except IOError:
            font = ImageFont.load_default()

        width, height = image.size

        for face in face_details:
            box = face["Face"]["BoundingBox"]
            left = int(box["Left"] * width)
            top = int(box["Top"] * height)
            right = int((box["Left"] + box["Width"]) * width)
            bottom = int((box["Top"] + box["Height"]) * height)

            confidence = face.get("MatchConfidence", 0)
            if confidence > 90:
                draw.rectangle([left, top, right, bottom], outline="red", width=3)

                text = face.get("Name", "")
                position = (left, top - 20)
                bbox = draw.textbbox(position, text, font=font)
                draw.rectangle(bbox, fill="red")
                draw.text(position, text, font=font, fill="white")

        image.save(output_path)
        print(f"Imagem salva com resultados em: {output_path}")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Função principal
if __name__ == "__main__":
    photo_paths = [
        get_path("bbc.jpg"),
        get_path("msn.jpg"),
        get_path("neymar-torcedores.jpg"),
    ]

    for photo_path in photo_paths:
        if not os.path.exists(photo_path):
            print(f"Arquivo não encontrado: {photo_path}")
            continue

        response = recognize_celebrities(photo_path)
        faces = response["CelebrityFaces"]
        if not faces:
            print(f"Não foram encontrados famosos para a imagem: {photo_path}")
            continue

        output_path = get_path(f"{Path(photo_path).stem}-resultado.jpg")
        draw_boxes(photo_path, output_path, faces)
