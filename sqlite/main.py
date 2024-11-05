import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def sqlite_tests(e):
        def test_basic():
            try:
                import sqlite3

                conn = sqlite3.connect("mydb.db")
                conn.close()

                page.add(ft.Text("sqlite: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"sqlite: test_basic - error: {e}"))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run SQLite tests", on_click=sqlite_tests),
                ]
            )
        )
    )


ft.app(main)
