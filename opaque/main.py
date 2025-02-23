import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet opaque test"
    page.scroll = ft.ScrollMode.AUTO

    def pysodium_tests(e):

        def test_basic():

            try:
                import opaque

                ids = opaque.Ids("user", "server")

                page.add(ft.Text("opaque: test_basic - OK"))
            except Exception as e:
                with open(os.environ["FLET_APP_CONSOLE"]) as f:
                    page.add(
                        ft.Text(
                            f.read(),
                            selectable=True,
                        )
                    )
                page.add(
                    ft.Text(
                        f"pysodium: opaque - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run opaque tests", on_click=pysodium_tests),
                ]
            )
        )
    )


ft.app(main)
