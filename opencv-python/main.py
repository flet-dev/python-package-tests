import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def opencv_tests(e):
        def test_basic():
            try:

                import cv2

                page.add(ft.Text("import cv2 - OK"))
                cv2.getBuildInformation()

                cap = cv2.VideoCapture("SampleVideo_1280x720_1mb.mp4")
                assert cap.isOpened() == True

                page.add(ft.Text("opencv-python: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"opencv-python: test_basic - error: {e}", selectable=True)
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run opencv-python tests", on_click=opencv_tests),
                ]
            )
        )
    )


ft.app(main)
