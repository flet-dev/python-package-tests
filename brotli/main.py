import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def brotli_tests(e):
        def test_basic():
            try:
                import brotli

                page.add(ft.Text("import brotli - OK"))
                plain = b"it was the best of times, it was the worst of times"
                compressed = brotli.compress(plain)
                page.add(ft.Text("compress - OK"))

                # compressed = compressed.hex()
                print(compressed)
                assert len(compressed) < len(plain)

                page.add(
                    ft.Text(
                        f"assert len(compressed): {len(compressed)} < len(plain): {len(plain)} - OK"
                    )
                )
                assert plain == brotli.decompress(compressed)

                page.add(ft.Text("brotli: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"brotli: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run brotli tests", on_click=brotli_tests),
                ]
            )
        )
    )


ft.app(main)
