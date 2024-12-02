import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def pendulum_tests(e):

        def test_basic():

            try:
                import pendulum

                tomorrow = pendulum.now().add(days=1)
                last_week = pendulum.now().subtract(weeks=1)
                delta = tomorrow - last_week
                assert delta.hours == 23

                page.add(ft.Text("pendulum: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"pendulum: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run pendulum tests", on_click=pendulum_tests),
                ]
            )
        )
    )


ft.app(main)
