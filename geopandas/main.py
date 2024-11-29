import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def geopandas_tests(e):

        def test_basic():

            # https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html

            try:

                # from geodatasets import get_path

                import geopandas

                # import matplotlib.pyplot as plt
                import pandas as pd

                df = pd.DataFrame(
                    {
                        "City": [
                            "Buenos Aires",
                            "Brasilia",
                            "Santiago",
                            "Bogota",
                            "Caracas",
                        ],
                        "Country": [
                            "Argentina",
                            "Brazil",
                            "Chile",
                            "Colombia",
                            "Venezuela",
                        ],
                        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
                        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
                    }
                )

                gdf = geopandas.GeoDataFrame(
                    df,
                    geometry=geopandas.points_from_xy(df.Longitude, df.Latitude),
                    crs="EPSG:4326",
                )

                print(gdf.head())

                page.add(ft.Text("geopandas: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"geopandas: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        def test_other():

            try:

                page.add(ft.Text("geopandas: test_other - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"geopandas: test_other - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()
        test_other()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run geopandas tests", on_click=geopandas_tests),
                ]
            )
        )
    )


ft.app(main)
