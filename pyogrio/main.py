import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def pyogrio_tests(e):

        def test_basic():

            try:
                from pyogrio import list_drivers

                print(list_drivers())

                page.add(ft.Text("pyogrio: test_basic - OK"))

            except Exception as e:
                page.add(
                    ft.Text(
                        f"pyogrio: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run pyogrio tests", on_click=pyogrio_tests),
                ]
            )
        )
    )


ft.app(main)
