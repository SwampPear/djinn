// Copyright 2024 Michael Vaden
#include "mavan/web/http/http.hpp"

namespace Mavan {
Request::Request(
    std::string address,
    uint16_t port,
    std::string method,
    std::string url,
    std::string version,
    Headers headers
) : address{address},
    port{port},
    method{method},
    url{url},
    version{version},
    headers{headers} {
        formattedRequest = fmtRequest();
}

std::string Request::fmtRequest() {
    std::ostringstream stream;

    stream << method << " ";
    stream << url << " ";
    stream << version << "\r\n";
    // set headers
    stream << "\r\n";

    return std::move(stream).str();
}

std::string Request::send() {
    Session session = Session(address, port);
    return session.request(formattedRequest);
}

Response::Response(std::string rawResponse) : rawResponse{rawResponse} {
    parseRawResponse(rawResponse);
}

void Response::parseRawResponse(std::string rawResponse) { }

Headers::Headers() { }
Headers::~Headers() { }

void Headers::set(std::string header, std::string value) {
    container.insert(std::make_pair(header.c_str(), value.c_str()));
}
}  // namespace Mavan
