// Copyright 2024 Michael Vaden
#pragma once

#include <cstdlib>
#include <string>
#include "mavan/web/browser.hpp"

namespace Mavan {
/**
 * @class Controller
 * @brief Controls all of the kernels in this project.
 */
class Controller {
 public:
    explicit Controller(std::string cdPath);
    ~Controller();

    int run();

 private:
    std::string cdPath;
    Browser browser;
};
}  // namespace Mavan
