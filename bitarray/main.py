import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def bitarray_tests(e):
        def test_basic():
            try:
                from bitarray import bitarray

                a = bitarray()
                a.append(True)
                a.extend([False, True, True])
                assert a == bitarray("1011")
                assert a != bitarray("1111")

                b = bitarray("1100")
                assert a & b == bitarray("1000")
                assert a | b == bitarray("1111")
                assert a ^ b == bitarray("0111")

                a[:] = True
                assert a == bitarray("1111")

                page.add(ft.Text("bitarray: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"bitarray: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run bitarray tests", on_click=bitarray_tests),
                ]
            )
        )
    )


ft.app(main)
