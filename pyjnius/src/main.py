import os
import traceback

import flet as ft


def main(page: ft.Page):

    def get_activity(e):
        try:
            from jnius import autoclass

            activity_host_class = os.getenv("MAIN_ACTIVITY_HOST_CLASS_NAME")
            assert activity_host_class
            results.controls.append(
                ft.Text(f"activity_host_class: {activity_host_class}")
            )
            activity_host = autoclass(activity_host_class)
            activity = activity_host.mActivity
            results.controls.append(ft.Text(f"Main Activity: {activity}"))
            results.update()

        except Exception as e:
            results.controls.append(
                ft.Text(
                    f"pyjnius get_activity error: {traceback.format_exc()}",
                    selectable=True,
                )
            )
        finally:
            results.update()

    def get_os_details(e):
        try:
            from jnius import autoclass

            # Get Build and Version classes
            Build = autoclass("android.os.Build")
            Version = autoclass("android.os.Build$VERSION")

            # Get OS details
            device_model = Build.MODEL
            manufacturer = Build.MANUFACTURER
            brand = Build.BRAND
            hardware = Build.HARDWARE
            product = Build.PRODUCT
            device = Build.DEVICE
            cpu_abi = Build.SUPPORTED_ABIS[0]
            os_version = Version.RELEASE
            sdk_version = Version.SDK_INT
            security_patch = Version.SECURITY_PATCH

            # Print Android OS details
            results.controls.append(ft.Text(f"Device Model: {device_model}"))
            results.controls.append(ft.Text(f"Manufacturer: {manufacturer}"))
            results.controls.append(ft.Text(f"Brand: {brand}"))
            results.controls.append(ft.Text(f"Hardware: {hardware}"))
            results.controls.append(ft.Text(f"Product: {product}"))
            results.controls.append(ft.Text(f"Device: {device}"))
            results.controls.append(ft.Text(f"Android OS Version: {os_version}"))
            results.controls.append(ft.Text(f"SDK Version: {sdk_version}"))
            results.controls.append(ft.Text(f"Security Patch Level: {security_patch}"))
            results.controls.append(ft.Text(f"CPU Architecture: {cpu_abi}"))

        except Exception as e:
            results.controls.append(
                ft.Text(
                    f"pyjnius get_os_details error: {traceback.format_exc()}",
                    selectable=True,
                )
            )
        finally:
            results.update()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Button("Get OS details", on_click=get_os_details),
                    ft.Button("Get Main Activity", on_click=get_activity),
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
