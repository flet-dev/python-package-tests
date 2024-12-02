import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def msgspec_tests(e):

        def test_basic():

            try:
                import msgspec

                class User(msgspec.Struct):
                    """A new type describing a User"""

                    name: str
                    groups: set[str] = set()
                    email: str | None = None

                alice = User("alice", groups={"admin", "engineering"})

                # Encode messages as JSON, or one of the many other supported protocols.

                msg = msgspec.json.encode(alice)

                # Decode messages back into Python objects, with optional schema validation.

                assert msgspec.json.decode(msg) == {
                    "name": "alice",
                    "groups": ["engineering", "admin"],
                    "email": None,
                }

                page.add(ft.Text("msgspec: test_basic - OK"))

            except Exception as e:
                page.add(
                    ft.Text(
                        f"msgspec: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run msgspec tests", on_click=msgspec_tests),
                ]
            )
        )
    )


ft.app(main)
