import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def gdal_tests(e):

        def test_basic():

            try:

                page.add(ft.Text("GDAL: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"GDAL: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        def test_other():

            try:

                page.add(ft.Text("GDAL: test_other - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"GDAL: test_other - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()
        test_other()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run GDAL tests", on_click=gdal_tests),
                ]
            )
        )
    )


ft.app(main)
