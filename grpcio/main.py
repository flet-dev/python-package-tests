import traceback

import flet as ft


def main(page: ft.Page):
    page.title = "Flet libs test"

    def grpcio_tests(e):

        def test_basic():

            try:
                from concurrent import futures

                import grpc
                import helloworld_pb2
                import helloworld_pb2_grpc

                page.add(ft.Text("grpc: import grpc - OK"))

                # Set up
                class Greeter(helloworld_pb2_grpc.GreeterServicer):
                    def SayHello(self, request, context):
                        return helloworld_pb2.HelloReply(
                            message="Hello, %s!" % request.name
                        )

                server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
                helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
                port = server.add_insecure_port("localhost:0")
                assert port
                server.start()
                page.add(ft.Text("grpc: setup - OK"))

                channel = grpc.insecure_channel("localhost:{}".format(port))
                stub = helloworld_pb2_grpc.GreeterStub(channel)
                response = stub.SayHello(helloworld_pb2.HelloRequest(name="world"))
                assert "Hello, world!" == response.message

                page.add(ft.Text("grpc: test_basic - OK"))
            except Exception as e:
                page.add(
                    ft.Text(
                        f"grpc: test_basic - error: {traceback.format_exc()}",
                        selectable=True,
                    )
                )

        test_basic()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.ElevatedButton("Run grpc tests", on_click=grpcio_tests),
                ]
            )
        )
    )


ft.app(main)
