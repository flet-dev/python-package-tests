import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def google_crc32c_tests(e):

        def test_basic():

            try:
                import google_crc32c

                page.add(ft.Text("google_crc32c: import google_crc32c - OK"))

                assert "c" == google_crc32c.implementation

                for data, expected in [
                    (b"", 0x00000000),
                    (b"\x00" * 32, 0x8A9136AA),
                    (bytes(range(32)), 0x46DD794E),
                ]:
                    assert expected == google_crc32c.value(data)

                page.add(ft.Text("google_crc32c: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"google_crc32c: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run google_crc32c tests", on_click=google_crc32c_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
