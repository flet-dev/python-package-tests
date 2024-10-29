import flet as ft
from tests import numpy_tests


def main(page: ft.Page):
    page.title = "Flet libs test"

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run Numpy tests", on_click=numpy_tests),
                    ft.ElevatedButton("Run Pandas tests", on_click=pandas_tests),
                ]
            )
        )
    )


ft.app(main)
