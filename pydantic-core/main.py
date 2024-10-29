import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def pydantic_tests(e):
        def test_basic():
            try:
                from pydantic_core import SchemaValidator

                v = SchemaValidator(
                    {
                        "type": "typed-dict",
                        "fields": {
                            "name": {
                                "type": "typed-dict-field",
                                "schema": {
                                    "type": "str",
                                },
                            },
                            "age": {
                                "type": "typed-dict-field",
                                "schema": {
                                    "type": "int",
                                    "ge": 18,
                                },
                            },
                            "is_developer": {
                                "type": "typed-dict-field",
                                "schema": {
                                    "type": "default",
                                    "schema": {"type": "bool"},
                                    "default": True,
                                },
                            },
                        },
                    }
                )
                r1 = v.validate_python({"name": "Samuel", "age": 35})
                assert r1 == {"name": "Samuel", "age": 35, "is_developer": True}

                page.add(ft.Text("pydantic_core: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"pydantic_core: test_basic - error: {e}"))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run Pydantic tests", on_click=pydantic_tests),
                ]
            )
        )
    )


ft.app(main)
