#include <cstdlib>
#include <iostream>
#include <vector>
#include <variant>
#include <string>
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

#include "mavan.hpp"

int main() {
  // test logic
  //////////////////////////////////////////////////////////////////////////////
  const char *driverPath = "~/Desktop/projects/mavan/src/mavan/web/chromedriver";

  Mavan::Controller controller = Mavan::Controller(driverPath);

  controller.run();
  //////////////////////////////////////////////////////////////////////////////

  // test http
  //////////////////////////////////////////////////////////////////////////////
  // GET /status HTTP/1.1\r\n\r\n
  Mavan::Request req = Mavan::Request(
    "127.0.0.1",
    9515,
    Mavan::Method::GET,
    "/status"
  );

  std::cout << req.send() << std::endl;
  std::cout << "\n\n" << std::endl;
  //////////////////////////////////////////////////////////////////////////////

  // test json
  //////////////////////////////////////////////////////////////////////////////
  const char* json = "{\"project\":\"rapidjson\",\"stars\":10}";
  rapidjson::Document d;
  d.Parse(json);

  // 2. Modify it by DOM.
  rapidjson::Value& s = d["stars"];
  s.SetInt(s.GetInt() + 1);

  // 3. Stringify the DOM
  rapidjson::StringBuffer buffer;
  rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);
  d.Accept(writer);

  // Output {"project":"rapidjson","stars":11}
  std::cout << buffer.GetString() << std::endl;

  return EXIT_SUCCESS;
}