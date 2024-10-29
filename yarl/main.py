import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def yarl_tests(e):
        def test_basic():
            try:

                from yarl import URL

                page.add(ft.Text("yarl: import - OK"))

                assert (
                    str(URL("http://εμπορικόσήμα.eu/путь/這裡"))
                    == "http://xn--jxagkqfkduily1i.eu/%D0%BF%D1%83%D1%82%D1%8C/%E9%80%99%E8%A3%A1"
                )

                page.add(ft.Text("yarl: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"yarl: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run yarl tests", on_click=yarl_tests),
                ]
            )
        )
    )


ft.app(main)
