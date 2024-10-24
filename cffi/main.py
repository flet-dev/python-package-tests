# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def cffi_tests(e):
        def test_basic():
            try:
                from cffi import FFI

                page.add(ft.Text("from cffi import FFI - OK"))

                ffi = FFI()
                ffi.cdef("size_t strlen(char *str);")
                page.add(ft.Text('ffi.cdef("size_t strlen(char *str);") - OK'))
                lib = ffi.dlopen(None)
                page.add(ft.Text("ffi.dlopen(None) - OK"))
                assert lib.strlen(ffi.new("char[]", b"hello world")) == 11

                page.add(ft.Text("cffi: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"cffi: test_basic - error: {e}", selectable=True))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run cffi tests", on_click=cffi_tests),
                ]
            )
        )
    )


ft.app(main)
