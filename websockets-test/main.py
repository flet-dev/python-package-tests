# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def websockets_tests(e):
        def test_basic():
            try:
                from websockets.sync.client import connect

                page.add(ft.Text("from websockets.sync.client import connect - OK"))
                with connect("wss://echo.websocket.org") as websocket:
                    websocket.send("Hello world!")
                    message = websocket.recv()
                    print(f"Received: {message}")

                page.add(ft.Text("websockets: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"websockets: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run websockets tests", on_click=websockets_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
