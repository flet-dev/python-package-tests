import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def pyyaml_tests(e):

        def test_basic():

            try:
                import yaml

                yaml.dump(["foo"])

                page.add(ft.Text("pyyaml: test_basic - OK"))

            except Exception as e:
                page.add(
                    ft.Text(
                        f"pyyaml: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run pyyaml tests", on_click=pyyaml_tests),
                ]
            )
        )
    )


ft.app(main)
