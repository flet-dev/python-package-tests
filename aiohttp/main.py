# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def aiohttp_tests(e):
        def test_basic():
            try:
                import asyncio

                import aiohttp

                async def main():
                    async with aiohttp.ClientSession() as session:
                        async with session.get("http://python.org") as response:
                            assert response.status == 200
                            # assert re.match(
                            #     r"^text/html", response.headers["content-type"]
                            # )

                asyncio.run(main())

                page.add(ft.Text("aiohhtp: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"aiohttp: test_basic - error: {e}", selectable=True))

        def test_extension():
            try:
                from aiohttp import _http_parser, http_parser

                assert http_parser.HttpResponseParser is _http_parser.HttpResponseParser
                assert (
                    http_parser.HttpResponseParser
                    is not http_parser.HttpResponseParserPy
                )
                page.add(ft.Text("aiohhtp: test_extension - OK"))
            except:
                page.add(
                    ft.Text(f"aiohttp: test_extension - error: {e}", selectable=True)
                )

        test_basic()
        test_extension()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run aiohttp tests", on_click=aiohttp_tests),
                ]
            )
        )
    )


ft.app(main)
