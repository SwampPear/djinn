// Copyright 2024 Michael Vaden
#include "mavan/web/http/session.hpp"

namespace Mavan {
Session::Session(std::string address, Port port)
    : address{address}, port{port} { }
Session::~Session() { }

std::string Session::request(std::string request) {
    struct sockaddr_in serv_addr;
    int pid;

    // create socket
    if ((pid = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        throw std::runtime_error("socket creation error");
    }

    // configure socket
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(9515);

    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        throw std::runtime_error("invalid address/ Address not supported");
    }

    // connect socket
    if (connect(pid, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        throw std::runtime_error("socket connection error");
    }

    // send request
    if (send(pid, request.c_str(), strlen(request.c_str()), 0) == -1) {
        throw std::runtime_error("error sending request");
    }

    // receive raw response
    char buffer[2048];
    ssize_t bytes_received;
    bytes_received = read(pid, buffer, 2048 - 1);
    buffer[bytes_received] = '\0';

    close(pid);

    return std::string(buffer);
}
}  // namespace Mavan
