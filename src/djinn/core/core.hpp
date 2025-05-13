#pragma once

#include <string>

namespace Djinn {

struct ExecutionContext {
    std::string data;           // location of data directory
    std::string root;           // location of working directory
    std::string project;        // project description
    std::string stack;          // technology stack description
    std::string environment;    // environment description 
};

}  // namespace Djinn

/*
"description": "write a function in python in bell_curve.py to make a matplotlibe bell graph.",
"stack": "python, matplotlib",
"environment": "Apple Silicon"
*/
