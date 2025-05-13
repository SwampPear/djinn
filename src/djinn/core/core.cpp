#include "djinn/core/core.hpp"

namespace Djinn {

ExecutionContext get_execution_context() {
    // read config
    nlohmann::json json_data;
    std::ifstream file("djinn.json");
    if (!file.is_open()) {
        throw std::runtime_error("'djinn.json' could not be found or is malformed");
    }
    file >> json_data;

    // build execution context
    std::string home = std::string(getenv("HOME"));

    Djinn::ExecutionContext context{};
    context.data        = home + "/Library/Application Support/djinn";
    context.root        = get_cwd();

    std::vector<std::string> keys = {
        "description",
        "stack",
        "environment"
    };

    for (const auto& key : keys) {
        if (!json_data.contains(key)) {
            throw std::runtime_error("Missing '" + key + "' in 'djinn.json'");
        }

        context[key] = json_data[key].get<std::string>();
    }

    return context;
}

}  // namespace Djinn