import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def lru_tests(e):
        def test_basic():
            try:

                from lru import LRU

                page.add(ft.Text("lru: import - OK"))

                data = LRU(3)
                data[1] = None
                data[2] = None
                data[3] = None
                data[1]
                data[4] = None
                assert data.keys == [4, 1, 3]

                page.add(ft.Text("lru-dict: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"lru-dict: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run lru-dict tests", on_click=lru_tests),
                ]
            )
        )
    )


ft.app(main)
