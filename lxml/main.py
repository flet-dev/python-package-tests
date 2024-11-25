import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def parseXML(xmlFile):
        """
        Parse the xml
        """
        from lxml import etree

        with open(xmlFile) as fobj:
            xml = fobj.read()

            root = etree.fromstring(xml)

        for appt in root.getchildren():
            for elem in appt.getchildren():
                if not elem.text:
                    text = "None"
                else:
                    text = elem.text
                print(elem.tag + " => " + text)

    def lxml_tests(e):

        def test_basic():

            try:

                parseXML("example.xml")

                page.add(ft.Text("lxml: test_basic - OK"))
            except Exception as e:
                page.add(ft.Text(f"lxml: test_basic - error: {e}", selectable=True))

        def test_xsl():
            try:
                from lxml import etree

                dom = etree.parse("test.xml")
                xsl = etree.parse("test_xsl.xsl")
                transform = etree.XSLT(xsl)
                output_json = str(transform(dom))
                cleaned_json = output_json.replace("\n", "")
                print(cleaned_json)
                page.add(ft.Text("lxml: test_xsl - OK"))

            except Exception as e:
                page.add(ft.Text(f"lxml: test_xsl - error: {e}", selectable=True))

        test_basic()
        test_xsl()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run lxml tests", on_click=lxml_tests),
                ]
            )
        )
    )


ft.app(main)
