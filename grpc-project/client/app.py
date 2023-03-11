from __future__ import print_function

import grpc
import users_pb2
import users_pb2_grpc


def run():

    print("Attempting to get all users ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUser(users_pb2.GetUserRequest())
    print(response.users)


if __name__ == '__main__':

    run()
