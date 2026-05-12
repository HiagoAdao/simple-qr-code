# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "qrcode[pil]",
# ]
# ///

import argparse
import sys
import qrcode
from pathlib import Path

def generate_qr_code(url: str, output_path: Path) -> None:
    """
    Gera um QR Code a partir de uma URL fornecida e salva no disco.

    Args:
        url (str): A URL ou texto que será codificado no QR Code.
        output_path (Path): O caminho completo onde a imagem será salva.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save(output_path)
        print(f"✅ Sucesso! QR Code gerado e salvo em: {output_path.absolute()}")

    except Exception as e:
        print(f"❌ Erro ao gerar o QR Code: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    """Ponto de entrada principal da CLI."""
    parser = argparse.ArgumentParser(
        description="Utilitário de linha de comando para gerar QR Codes a partir de URLs.",
        epilog="Exemplo de uso: python gerador_qr.py https://github.com -o meu_github.png"
    )

    parser.add_argument(
        "url", 
        type=str, 
        help="A URL ou texto que será convertido em QR Code."
    )
    default_output = Path.home() / "Downloads" / "qrcode.png"
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default=str(default_output), 
        help=f"Caminho e nome do arquivo de saída (padrão: {default_output})."
    )
    
    args = parser.parse_args()

    output_path = Path(args.output)
    if output_path.parent != Path('.'):
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    generate_qr_code(args.url, output_path)

if __name__ == "__main__":
    main()
