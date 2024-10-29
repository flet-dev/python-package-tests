import datetime as dt
from datetime import datetime, timedelta

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def time_machine_tests(e):
        def test_basic():
            try:

                import time_machine

                page.add(ft.Text("import time_machine - OK"))

                # travel 50 days back
                destination_date = datetime.now() - timedelta(days=50)
                traveller = time_machine.travel(destination_date)
                traveller.start()
                # It's the past!
                assert dt.date.today() == destination_date.date()
                traveller.stop()
                # We've gone back to the future!

                assert dt.date.today() > destination_date.date()

                page.add(ft.Text("time-machine: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"time-machine: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run time-machine tests", on_click=time_machine_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
