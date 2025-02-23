import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet pysodium test"
    page.scroll = ft.ScrollMode.AUTO

    def pysodium_tests(e):

        def test_basic():

            try:
                import pysodium

                r = pysodium.crypto_generichash(b"howdy")
                pysodium.crypto_generichash(b"howdy", outlen=4)
                r6 = pysodium.crypto_generichash(b"howdy", outlen=6)
                pysodium.crypto_generichash(b"howdy", outlen=8)
                state = pysodium.crypto_generichash_init()
                pysodium.crypto_generichash_update(state, b"howdy")
                r1 = pysodium.crypto_generichash_final(state)

                state = pysodium.crypto_generichash_init(outlen=6)
                pysodium.crypto_generichash_update(state, b"howdy")
                r61 = pysodium.crypto_generichash_final(state, outlen=6)
                assert r == r1
                assert r6 == r61

                page.add(ft.Text("pysodium: test_basic - OK"))
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
                        f"pysodium: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run pysodium tests", on_click=pysodium_tests),
                ]
            )
        )
    )


ft.app(main)
