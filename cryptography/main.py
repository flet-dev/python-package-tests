# import io
# from os.path import dirname, join

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def cryptography_tests(e):
        def test_x509():
            try:
                from textwrap import dedent

                import cryptography

                page.add(ft.Text("import cryptography - OK"))
                from cryptography import x509

                page.add(ft.Text("from cryptography import x509 - OK"))
                from cryptography.hazmat.backends import default_backend
                from cryptography.x509.oid import NameOID

                cert_pem = dedent(
                    """
        -----BEGIN CERTIFICATE-----
        MIIEhDCCA2ygAwIBAgIIF2d9E030vlcwDQYJKoZIhvcNAQELBQAwVDELMAkGA1UE
        BhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczElMCMGA1UEAxMc
        R29vZ2xlIEludGVybmV0IEF1dGhvcml0eSBHMzAeFw0xODA0MTcxMzI0MzhaFw0x
        ODA3MTAxMjM5MDBaMGkxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlh
        MRYwFAYDVQQHDA1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKDApHb29nbGUgSW5jMRgw
        FgYDVQQDDA93d3cuYW5kcm9pZC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
        ggEKAoIBAQC3t8zd3s9oSLFUkogYhD//BoFwvtHnpUHW2n9g3KiAXCHHG5+8QD4Q
        abgAzrpeQqewWngE9B3Feq4rUo9vsk0UpB7Pj97TAgkkmpRMcW0lU4p4rKNhDfri
        c+SvnuZuy048v8Ta7DtMymuCIyejekjTg7Gf/U46PqK87ZbV5RTadSgfvlymnkQb
        SwJLUA8qe/H98bEARpQLyJvWi8dUSurpfKHdbXfd1Dk9GACHNAX9A4bV0BdQBmPu
        6BMGeY5O4CYwwM51U/W+ptyc5eFRMi10up1cck3Udwl/jw5OAx5NP7geuxuIc4uu
        l41Zwbnr5v6sdJJsWMvMg7ot/97+EHvXAgMBAAGjggFDMIIBPzATBgNVHSUEDDAK
        BggrBgEFBQcDATAaBgNVHREEEzARgg93d3cuYW5kcm9pZC5jb20waAYIKwYBBQUH
        AQEEXDBaMC0GCCsGAQUFBzAChiFodHRwOi8vcGtpLmdvb2cvZ3NyMi9HVFNHSUFH
        My5jcnQwKQYIKwYBBQUHMAGGHWh0dHA6Ly9vY3NwLnBraS5nb29nL0dUU0dJQUcz
        MB0GA1UdDgQWBBSYOxV7LRH/9yKSFL5jLJfhwZxCUDAMBgNVHRMBAf8EAjAAMB8G
        A1UdIwQYMBaAFHfCuFCaZ3Z2sS3ChtCDoH6mfrpLMCEGA1UdIAQaMBgwDAYKKwYB
        BAHWeQIFAzAIBgZngQwBAgIwMQYDVR0fBCowKDAmoCSgIoYgaHR0cDovL2NybC5w
        a2kuZ29vZy9HVFNHSUFHMy5jcmwwDQYJKoZIhvcNAQELBQADggEBAI4fv5P+VLSE
        /f+hOoPuxWx2TEDdc/Gt2u3XUiGkMrOSW2k1ob0kUjBDILhear3tpp+V5N5H0NzZ
        Ymvpbbl3ZD5Bk5Co9FIJwFNMfGAlzSAduuYdAblOXTkLzlyLwn5qbzDjbkBIS+0O
        l+1zga+3gZGYbDQiByFyq8P/uAKzc0BAX82bgXDkIC3E26YvvTnUpkKh6l6bOOTB
        xaTg8Uh6KsKGch837BDbNegs3wHw3T3s7PC+H7dvqjELqN7y2GNNA361/aPPCWgs
        jUsy3XnYSd8og34IzY3+W2b3TrU8P+p+pBwOjgXuNHZwobU+3/e2s4/0AfDilpI0
        KX/1hroho1I=
        -----END CERTIFICATE-----
    """
                ).encode("ASCII")
                cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
                domain = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[
                    0
                ].value
                assert domain == "www.android.com"

                page.add(ft.Text("cryptography: test_x509 - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"cryptography: test_x509 - error: {e}", selectable=True)
                )

        def test_fernet():
            try:
                from cryptography.fernet import Fernet

                page.add(ft.Text("from cryptography.fernet import Fernet - OK"))

                key = Fernet.generate_key()
                f = Fernet(key)
                msg = b"my deep dark secret"
                token = f.encrypt(msg)
                assert f.decrypt(token) == msg
                page.add(ft.Text(f"cryptography: test_fernet - OK"))
            except Exception as e:
                page.add(
                    ft.Text(f"cryptography: test_fernet - error: {e}", selectable=True)
                )

        test_x509()
        test_fernet()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton(
                        "Run cryptography tests", on_click=cryptography_tests
                    ),
                ]
            )
        )
    )


ft.app(main)
