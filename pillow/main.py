import io
from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def pillow_tests(e):
        def test_basic():
            try:
                from PIL import Image

                img = Image.open(join(dirname(__file__), "mandrill.jpg"))
                assert img.width == 512
                assert img.height == 512

                out_file = io.BytesIO()
                img.save(out_file, "png")
                out_bytes = out_file.getvalue()

                EXPECTED_LEN = 313772
                assert len(out_bytes) > int(EXPECTED_LEN * 0.8)
                # assert len(out_bytes) < int(EXPECTED_LEN * 1.2)

                assert out_bytes[:24] == (
                    b"\x89PNG\r\n\x1a\n"
                    + b"\x00\x00\x00\rIHDR"  # File header
                    + b"\x00\x00\x02\x00"  # Header chunk header
                    + b"\x00\x00\x02\x00"  # Width 512  # Height 512
                )

                page.add(ft.Text("pillow: test_basic - OK"))

            except Exception as e:
                page.add(ft.Text(f"pillow: test_basic - error: {e}", selectable=True))

        def test_font():
            try:
                from PIL import ImageFont

                font = ImageFont.truetype(join(dirname(__file__), "Vera.ttf"), size=20)
                # ont.getsize("Hello") == (51, 19)
                # font.getsize("Hello world") == (112, 19)
                page.add(ft.Text(f"pillow: test_font - OK"))
            except Exception as e:
                page.add(ft.Text(f"pillow: test_font - error: {e}"))

        test_basic()
        test_font()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run Pillow tests", on_click=pillow_tests),
                ]
            )
        )
    )


ft.app(main)
