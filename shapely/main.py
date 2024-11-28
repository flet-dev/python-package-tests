import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def shapely_tests(e):

        def test_basic():

            try:

                from shapely import Point

                patch = Point(0.0, 0.0).buffer(10.0)
                assert patch.area == 313.654849054594

                page.add(ft.Text("shapely: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"shapely: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        def test_with_numpy():

            try:

                import numpy as np
                import shapely
                from shapely import Point

                geoms = np.array([Point(0, 0), Point(1, 1), Point(2, 2)])
                polygon = shapely.box(0, 0, 2, 2)
                assert shapely.contains(polygon, geoms)[0] == False
                assert shapely.contains(polygon, geoms)[1] == True
                assert shapely.contains(polygon, geoms)[2] == False

                page.add(ft.Text("shapely: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"shapely: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()
        test_with_numpy()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run shapely tests", on_click=shapely_tests),
                ]
            )
        )
    )


ft.app(main)
