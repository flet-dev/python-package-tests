import os
import shutil
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

                shp_path = os.path.join(os.environ["FLET_APP_STORAGE_TEMP"], "123.shp")
                shutil.copy(
                    os.path.join(os.getcwd(), "ne_10m_admin_0_countries.shp"), shp_path
                )

                from pyogrio import get_gdal_data_path, list_layers

                page.add(
                    ft.Text(
                        f"GDAL data path: {os.environ['GDAL_DATA']}", selectable=True
                    )
                )
                page.add(
                    ft.Text(
                        f"FLET_APP_STORAGE_TEMP path: {os.environ['FLET_APP_STORAGE_TEMP']}",
                        selectable=True,
                    )
                )
                page.add(
                    ft.Text(
                        f"FLET_APP_STORAGE_DATA path: {os.environ['FLET_APP_STORAGE_DATA']}",
                        selectable=True,
                    )
                )

                os.environ["SHAPE_RESTORE_SHX"] = "YES"

                list_layers(shp_path)

                page.add(ft.Text("pyogrio: test_basic - OK"))
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
        # test_with_dataframes()

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
