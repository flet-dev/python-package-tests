import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def fiona_tests(e):

        def test_basic():

            try:

                import datetime

                import fiona
                from fiona import Feature, Geometry, Properties

                def signed_area(coords):
                    """Return the signed area enclosed by a ring using the linear time
                    algorithm at http://www.cgafaq.info/wiki/Polygon_Area. A value >= 0
                    indicates a counter-clockwise oriented ring.
                    """
                    xs, ys = map(list, zip(*coords))
                    xs.append(xs[1])
                    ys.append(ys[1])
                    return (
                        sum(
                            xs[i] * (ys[i + 1] - ys[i - 1])
                            for i in range(1, len(coords))
                        )
                        / 2.0
                    )

                with fiona.open(
                    "zip+https://github.com/Toblerity/Fiona/files/11151652/coutwildrnp.zip"
                ) as src:

                    # Copy the source schema and add two new properties.
                    dst_schema = src.schema
                    dst_schema["properties"]["signed_area"] = "float"
                    dst_schema["properties"]["timestamp"] = "datetime"

                    # Create a sink for processed features with the same format and
                    # coordinate reference system as the source.
                    with fiona.open(
                        "example.gpkg",
                        mode="w",
                        layer="oriented-ccw",
                        crs=src.crs,
                        driver="GPKG",
                        schema=dst_schema,
                    ) as dst:
                        for feat in src:
                            # If any feature's polygon is facing "down" (has rings
                            # wound clockwise), its rings will be reordered to flip
                            # it "up".
                            geom = feat.geometry
                            assert geom.type == "Polygon"
                            rings = geom.coordinates
                            sa = sum(signed_area(ring) for ring in rings)

                            if sa < 0.0:
                                rings = [r[::-1] for r in rings]
                                geom = Geometry(type=geom.type, coordinates=rings)

                            # Add the signed area of the polygon and a timestamp
                            # to the feature properties map.
                            props = Properties.from_dict(
                                **feat.properties,
                                signed_area=sa,
                                timestamp=datetime.datetime.now().isoformat(),
                            )

                            dst.write(Feature(geometry=geom, properties=props))

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
