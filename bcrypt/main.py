# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def bcrypt_tests(e):
        def test_basic():
            try:
                import bcrypt

                hashed = b"$2b$12$9cwzD/MRnVT7uvkxAQvkIejrif4bwRTGvIRqO7xf4OYtDQ3sl8CWW"
                assert bcrypt.checkpw(b"password", hashed)
                assert not bcrypt.checkpw(b"passwerd", hashed)

                page.add(ft.Text("bcrypt: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"bcrypt: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run bcrypt tests", on_click=bcrypt_tests),
                ]
            )
        )
    )


ft.app(main)
