import os
import sys
from pathlib import Path
from pdf2image import convert_from_path


class PDF2ImageConverter:
    def __init__(self):
        self.poppler_path = "./poppler/Library/bin"
        self.img_format = "JPEG"
        self.img_extension = self.search_img_format()
        self.poppler_setting()  # popplerの設定

    def poppler_setting(self):
        poppler_dir = Path(__file__).parent.absolute() / self.poppler_path
        os.environ['PATH'] += os.pathsep + str(poppler_dir)

    def search_img_format(self):
        if self.img_format == "JPEG":
            return ".jpeg"
        else:
            print("フォーマットが正しく設定されてません")
            sys.exit()

    def convert_pdf_to_images(self, pdf_path, output_dir):
        pdf_file_name = pdf_path.stem
        image_dir = output_dir / pdf_file_name

        # フォルダ作成
        image_dir.mkdir(parents=True, exist_ok=True)

        pages = convert_from_path(pdf_path)
        if len(pages) > 1:  # ページが複数ある場合
            try:
                for i, page in enumerate(pages):
                    file_name = pdf_path.stem + '_{:02d}'.format(i + 1) + self.img_extension
                    image_path = image_dir / file_name
                    page.save(str(image_path), self.img_format)
            except Exception as e:
                print(f"エラーが発生しました: {e}")
        else:
            try:
                file_name = pdf_path.stem + self.img_extension
                image_path = image_dir / file_name
                pages[0].save(str(image_path), self.img_format)
            except Exception as e:
                print(f"エラーが発生しました: {e}")


def main():
    try:
        # Pathの取得
        if len(sys.argv) != 2:
            input_path = Path(input('PDFファイルPath on フォルダバス：').replace('"', ''))
        else:
            input_path = Path(sys.argv[1])
    
        pdf2image = PDF2ImageConverter()
        if input_path.is_dir():  # フォルダだった場合
            pdf_files = list(input_path.glob('*.pdf'))
            for pdf_file in pdf_files:
                pdf2image.convert_pdf_to_images(pdf_file, input_path)
        else:  # PDFファイルだった場合
            pdf2image.convert_pdf_to_images(input_path, input_path.parent)
    except Exception as e:
        print(f"エラーが発生しました: {e}")

    input("終了するにはエンターキーを押してください...")


if __name__ == '__main__':
    main()
