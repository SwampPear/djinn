#pragma once

#include <string>

namespace Djinn {

struct ExecutionContext {
    std::string data;           // location of data directory
    std::string root;           // location of working directory
    std::string description;    // project description
    std::string stack;          // technology stack description
    std::string environment;    // environment description 

    std::string& operator[](const std::string& key) {
        if (key == "data")        return data;
        if (key == "root")        return root;
        if (key == "description") return description;
        if (key == "stack")       return stack;
        if (key == "environment") return environment;
        throw std::out_of_range("Invalid key: " + key);
    }
};

}  // namespace Djinn