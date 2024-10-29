import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def markupsafe_tests(e):
        def test_basic():
            try:

                from markupsafe import Markup, escape

                page.add(ft.Text("from markupsafe import Markup, escape - OK"))

                assert escape("\"<>&'") == "&#34;&lt;&gt;&amp;&#39;"
                assert (
                    Markup(
                        "<!-- outer comment -->"
                        "<em>Foo &amp; Bar"
                        " <!-- inner comment about <em> -->\n "
                        "</em>"
                        "<!-- comment\nwith\nnewlines\n-->"
                        "<meta content='tag\nwith\nnewlines'>"
                    ).striptags()
                    == "Foo & Bar"
                )

                page.add(ft.Text("markupsafe: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"markupsafe: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run markupsafe tests", on_click=markupsafe_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
