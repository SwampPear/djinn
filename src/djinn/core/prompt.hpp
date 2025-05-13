#pragma once

#include <iostream>
#include <map>
#include <cstdlib>
#include "nlohmann/json.hpp"
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/version.hpp>
#include <boost/asio/connect.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/asio/ssl.hpp>

namespace Djinn {

enum class Role {
    SYSTEM,
    USER
};

struct Prompt {
    std::string content;
    Role        role;
};

enum class HTTPMethod {
    GET,
    POST
};

struct HTTPRequest {
    std::map<std::string, std::string> headers;
    HTTPMethod  method;
    uint16_t    port;
    std::string host;
    std::string target;
    std::string body;
};

namespace beast = boost::beast;
namespace http  = beast::http;
namespace net   = boost::asio;
namespace ssl   = net::ssl;
using tcp       = net::ip::tcp;
using HTTPResponse = http::response<http::dynamic_body>;

HTTPResponse send_request(const HTTPRequest& request) {
    const std::string& host = request.host;
    const std::string port  = std::to_string(request.port);
    const std::string& target = request.target;
    int version = 11;

    net::io_context ioc;
    ssl::context ctx(ssl::context::sslv23_client);
    ctx.set_default_verify_paths();

    ssl::stream<beast::tcp_stream> stream(ioc, ctx);

    // Resolve and connect
    tcp::resolver resolver(ioc);
    auto const results = resolver.resolve(host, port);
    beast::get_lowest_layer(stream).connect(results);

    if (!SSL_set_tlsext_host_name(stream.native_handle(), host.c_str())) {
        beast::error_code ec{static_cast<int>(::ERR_get_error()), net::error::get_ssl_category()};
        throw beast::system_error{ec};
    }

    stream.handshake(ssl::stream_base::client);

    // Build request
    http::request<http::string_body> req{
        request.method == HTTPMethod::POST ? http::verb::post : http::verb::get,
        target,
        version
    };

    req.set(http::field::host, host);
    req.set(http::field::user_agent, BOOST_BEAST_VERSION_STRING);

    for (const auto& [k, v] : request.headers)
        req.set(k, v);

    req.body() = request.body;
    req.prepare_payload();

    http::write(stream, req);

    beast::flat_buffer buffer;
    HTTPResponse res;
    http::read(stream, buffer, res);

    beast::error_code ec;
    stream.shutdown(ec);

    return res;
}

std::string prompt(const std::string& user_prompt, const std::string& system_prompt) {
    const char* api_key = std::getenv("OPENAI_API_KEY");
    if (!api_key) throw std::runtime_error("Error: OPENAI_API_KEY not set.");

    // build request
    HTTPRequest req;
    req.method = HTTPMethod::POST;
    req.port = 443;
    req.host = "api.openai.com";
    req.target = "/v1/chat/completions";
    req.headers = {
        {"Content-Type", "application/json"},
        {"Authorization", std::string("Bearer ") + api_key}
    };

    nlohmann::json body = {
        {"model", "gpt-4"},
        {"messages", {
            {{"role", "system"}, {"content", system_prompt}},
            {{"role", "user"}, {"content", user_prompt}}
        }}
    };

    req.body = body.dump();
    
    // send request
    HTTPResponse res = send_request(req);

    // parse response
    auto res_body = boost::beast::buffers_to_string(res.body().data());
    nlohmann::json json_response = nlohmann::json::parse(res_body);
    std::string message = json_response["choices"][0]["message"]["content"];

    return message;
}
} // namespace Djinn
