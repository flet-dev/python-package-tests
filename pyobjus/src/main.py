import traceback

import flet as ft


def main(page: ft.Page):

    def test_nstring(e):
        try:
            from pyobjus import autoclass

            NSString = autoclass('NSString')
            text = NSString.alloc().initWithUTF8String_('Hello world')
            results.controls.append(ft.Text(f"text: {text.UTF8String()}"))

        except Exception as e:
            results.controls.append(
                ft.Text(
                    f"pyobjus test_nstring error: {traceback.format_exc()}",
                    selectable=True,
                )
            )
        finally:
            results.update()

    def get_os_details(e):
        try:
            from pyobjus import autoclass
            from pyobjus.dylib_manager import load_framework, INCLUDE

            # Load Foundation framework
            load_framework(INCLUDE.Foundation)

            # Get NSProcessInfo instance
            NSProcessInfo = autoclass('NSProcessInfo')
            process_info = NSProcessInfo.processInfo()

            # Retrieve OS version as a string
            os_version = process_info.operatingSystemVersionString.UTF8String()

            # Output OS details
            results.controls.append(ft.Text(f"iOS Version: {os_version}"))

        except Exception as e:
            results.controls.append(
                ft.Text(
                    f"pyobjus get_os_details error: {traceback.format_exc()}",
                    selectable=True,
                )
            )
        finally:
            results.update()

    def get_set_keystore(e):
        try:
            from pyobjus import autoclass, objc_str

            NSUserDefaults = autoclass('NSUserDefaults')

            key = "pyobjus_hello_world_key"
            value = "Hello, world!"

            # set key
            NSUserDefaults.standardUserDefaults().setObject_forKey_(objc_str(value), objc_str(key))

            # get key
            ret = NSUserDefaults.standardUserDefaults().stringForKey_(objc_str(key))

            results.controls.append(ft.Text(f"retrieved from store: {ret.UTF8String()}"))

        except Exception as e:
            results.controls.append(
                ft.Text(
                    f"pyobjus get_set_keystore error: {traceback.format_exc()}",
                    selectable=True,
                )
            )
        finally:
            results.update()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Button("Test NSString", on_click=test_nstring),
                    ft.Button("Get OS details", on_click=get_os_details),
                    ft.Button("Set/Get Keystore", on_click=get_set_keystore),
                    results := ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    ),
                ],
            ),
            expand=True,
        )
    )


ft.app(main)
