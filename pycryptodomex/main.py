import os
import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"
    page.scroll = ft.ScrollMode.AUTO

    def pycryptodomex_tests(e):

        def test_basic():

            try:
                from Cryptodome.Cipher import AES
                from Cryptodome.Hash import HMAC, SHA256
                from Cryptodome.Random import get_random_bytes

                data = "secret data to transmit".encode()

                aes_key = get_random_bytes(16)
                hmac_key = get_random_bytes(16)

                cipher = AES.new(aes_key, AES.MODE_CTR)
                ciphertext = cipher.encrypt(data)

                hmac = HMAC.new(hmac_key, digestmod=SHA256)
                tag = hmac.update(cipher.nonce + ciphertext).digest()

                with open("encrypted.bin", "wb") as f:
                    f.write(tag)
                    f.write(cipher.nonce)
                    f.write(ciphertext)

                # Somehow, the receiver securely get aes_key and hmac_key
                # encrypted.bin can be sent over an unsecure channel

                with open("encrypted.bin", "rb") as f:
                    tag = f.read(32)
                    nonce = f.read(8)
                    ciphertext = f.read()

                try:
                    hmac = HMAC.new(hmac_key, digestmod=SHA256)
                    tag = hmac.update(nonce + ciphertext).verify(tag)
                except ValueError:
                    print("The message was modified!")
                    sys.exit(1)

                cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
                message = cipher.decrypt(ciphertext)
                print("Message:", message.decode())
                assert message.decode() == "secret data to transmit"

                page.add(ft.Text("pycryptodomex: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"pycryptodomex: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run pycryptodomex tests", on_click=pycryptodomex_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
