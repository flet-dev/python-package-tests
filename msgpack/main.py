import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def msgpack_tests(e):

        def test_basic():

            try:
                import msgpack

                a = msgpack.packb([1, 2, 3])
                assert a == b"\x93\x01\x02\x03"

                assert msgpack.unpackb(a) == [1, 2, 3]

                page.add(ft.Text("msgpack: test_basic - OK"))

            except Exception as e:
                page.add(
                    ft.Text(
                        f"msgpack: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run msgpack tests", on_click=msgpack_tests),
                ]
            )
        )
    )


ft.app(main)
