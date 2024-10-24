import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def blis_tests(e):
        def test_einsum():
            try:
                import numpy as np

                from blis.py import einsum

                a = np.array([[1.0, 2.0], [3.0, 4.0]])
                b = np.array([[2.0, 3.0], [5.0, 7.0]])
                np.testing.assert_equal(
                    np.array([[12.0, 17.0], [26.0, 37.0]]), einsum("ab,bc->ac", a, b)
                )

                page.add(ft.Text("blis: test_einsum - OK"))
            except Exception as e:
                page.add(ft.Text(f"blis: test_einsum - error: {e}", selectable=True))

        test_einsum()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run blis tests", on_click=blis_tests),
                ]
            )
        )
    )


ft.app(main)
