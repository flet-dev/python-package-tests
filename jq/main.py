import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def jq_tests(e):
        def test_basic():
            try:

                page.add(ft.Text("jq: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"jq: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run jq tests", on_click=jq_tests),
                ]
            )
        )
    )


ft.app(main)
