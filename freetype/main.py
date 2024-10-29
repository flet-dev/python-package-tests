import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def freetype_tests(e):
        def test_basic():
            try:
                # Example from https://freetype-py.readthedocs.io/en/latest/usage.html
                import freetype

                page.add(ft.Text("import freetype - OK"))

                face = freetype.Face("Vera.ttf")

                page.add(ft.Text("freetype.Face() - OK"))

                face.set_char_size(48 * 64)
                face.load_char("S")
                bitmap = face.glyph.bitmap
                print(bitmap.buffer)

                page.add(ft.Text("freetype: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"freetype: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run freetype tests", on_click=freetype_tests),
                ]
            )
        )
    )


ft.app(main)
