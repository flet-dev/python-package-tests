import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def kiwisolver_tests(e):
        def test_basic():
            try:

                from kiwisolver import Solver, Variable

                page.add(ft.Text("kiwisolver: import - OK"))
                x1 = Variable("x1")
                x2 = Variable("x2")
                xm = Variable("xm")

                constraints = [x1 >= 0, x2 <= 100, x2 >= x1 + 10, xm == (x1 + x2) / 2]
                solver = Solver()
                for cn in constraints:
                    solver.addConstraint(cn)

                solver.addConstraint((x1 == 40) | "weak")
                solver.addEditVariable(xm, "strong")
                solver.suggestValue(xm, 60)
                solver.updateVariables()

                assert xm.value() == 60
                assert x1.value() == 40
                assert x2.value() == 80

                page.add(ft.Text("kiwisolver: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"kiwisolver: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run kiwisolver tests", on_click=kiwisolver_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
