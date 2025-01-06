import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def numpy_tests(e):
        def test_basic():
            try:
                from numpy import array

                assert (array([1, 2]) + array([3, 5])).tolist() == [4, 7]

                page.add(ft.Text("numpy: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"numpy: test_basic - error: {e}"))

        def test_performance():
            try:
                from time import time

                import numpy as np

                start_time = time()
                SIZE = 500
                a = np.random.rand(SIZE, SIZE)
                b = np.random.rand(SIZE, SIZE)
                np.dot(a, b)

                # With OpenBLAS, the test devices take at most 0.4 seconds. Without OpenBLAS, they take
                # at least 1.0 seconds.
                duration = time() - start_time
                page.add(
                    ft.Text(f"numpy: test_performance - OK, duration: {duration:.3f}")
                )
                print(f"{duration:.3f}")
                assert duration < 0.7
            except Exception as e:
                page.add(ft.Text(f"numpy: test_performance - error: {e}"))

        test_basic()
        test_performance()

    def pandas_tests(e):
        def test_basic():
            try:
                from pandas import DataFrame

                df = DataFrame(
                    [("alpha", 1), ("bravo", 2), ("charlie", 3)],
                    columns=["Letter", "Number"],
                )
                assert df.to_csv() == (
                    ",Letter,Number\n" "0,alpha,1\n" "1,bravo,2\n" "2,charlie,3\n"
                )

                page.add(ft.Text("pandas: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"pandas: test_basic - error: {e}"))

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run Numpy tests", on_click=numpy_tests),
                    ft.ElevatedButton("Run Pandas tests", on_click=pandas_tests),
                ]
            )
        )
    )


ft.app(main)
