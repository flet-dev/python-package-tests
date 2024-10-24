import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def contourpy_tests(e):
        def test_basic():
            try:

                from contourpy import contour_generator

                page.add(ft.Text("imports - OK"))

                cont_gen = contour_generator(
                    z=[
                        [1.4, 1.2, 0.9, 0.0],
                        [0.6, 3.0, 0.4, 0.7],
                        [0.2, 0.2, 0.5, 3.0],
                    ],
                    name="serial",
                    chunk_count=(1, 2),
                )

                assert cont_gen.chunk_count == (1, 2)
                assert cont_gen.chunk_size == (2, 2)

                assert cont_gen.thread_count < 10

                page.add(ft.Text("contourpy: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"contourpy: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run contourpy tests", on_click=contourpy_tests),
                ]
            )
        )
    )


ft.app(main)
