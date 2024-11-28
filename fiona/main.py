import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def fiona_tests(e):

        def test_basic():

            try:

                import fiona

                page.add(ft.Text("fiona: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"fiona: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run fiona tests", on_click=fiona_tests),
                ]
            )
        )
    )


ft.app(main)
