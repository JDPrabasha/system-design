
from concurrent import futures


import grpc
import users_pb2
import users_pb2_grpc


class Users(users_pb2_grpc.UsersServicer):

    def GetUser(self, request, context):
        users = [
            users_pb2.User(
                id='1',
                name='John Doe',
                email='dulaj@gmail.com',
                password='1234'
            ),
        ]
        return users_pb2.GetUserResponse(users=users)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':

    serve()
