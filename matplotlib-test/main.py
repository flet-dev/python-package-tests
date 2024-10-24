# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def matplotlib_tests(e):
        def test_basic():
            try:
                import matplotlib

                page.add(ft.Text("import matplotlib: OK"))

                import matplotlib.pyplot as plt
                from flet.matplotlib_chart import MatplotlibChart

                matplotlib.use("svg")
                fig, ax = plt.subplots()
                fruits = ["apple", "blueberry", "cherry", "orange"]
                counts = [40, 100, 30, 55]
                bar_labels = ["red", "blue", "_red", "orange"]
                bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]
                ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
                ax.set_ylabel("fruit supply")
                ax.set_title("Fruit supply by kind and color")
                ax.legend(title="Fruit color")
                page.add(MatplotlibChart(fig, expand=True))
                plt.figure()
                plt.plot([1, 2])
                bio = io.BytesIO()
                plt.savefig(bio, format="png")
                b = bio.getvalue()
                EXPECTED_LEN = 16782
                assert len(b) > int(EXPECTED_LEN * 0.8)
                assert len(b) < int(EXPECTED_LEN * 1.2)
                assert b[:24] == (
                    b"\x89PNG\r\n\x1a\n"
                    + b"\x00\x00\x00\rIHDR"  # File header
                    + b"\x00\x00\x02\x80"  # Header chunk header
                    + b"\x00\x00\x01\xe0"  # Width 640  # Height 480
                )

                page.add(ft.Text("matplotlib: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"matplotlib: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run Matplotlib tests", on_click=matplotlib_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
