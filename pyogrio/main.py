import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def pyogrio_tests(e):

        def test_basic():

            try:
                from pyogrio import list_drivers

                print(list_drivers())

                from pyogrio import list_layers

                os.environ["SHAPE_RESTORE_SHX"] = "YES"

                list_layers("ne_10m_admin_0_countries.shp")

                page.add(ft.Text("pyogrio: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"pyogrio: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        def test_with_dataframes():

            try:
                from pyogrio import read_info

                read_info("ne_10m_admin_0_countries.shp")

                page.add(ft.Text("pyogrio: test_with_dataframes - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"pyogrio: test_with_dataframes - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()
        test_with_dataframes()

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
