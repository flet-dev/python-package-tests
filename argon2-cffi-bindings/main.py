# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def argon2_cffi_bindings_tests(e):
        def test_basic():
            try:
                import argon2
                import pytest

                ph = argon2.PasswordHasher()
                hashed = ph.hash("s3kr3tp4ssw0rd")
                assert hashed.startswith("$argon2")
                assert ph.verify(hashed, "s3kr3tp4ssw0rd")
                with pytest.raises(argon2.exceptions.VerifyMismatchError):
                    ph.verify(hashed, "s3kr3tp4sswOrd")

                page.add(ft.Text("argon2-cffi-bindings: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"argon2-cffi-bindings: test_basic - error: {e}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run argon2-cffi-bindings tests",
                        on_click=argon2_cffi_bindings_tests,
                    ),
                ]
            )
        )
    )


ft.app(main)
