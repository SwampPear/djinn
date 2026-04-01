#include <map>
#include "djinn/core/context.hpp"
#include "djinn/core/utils.hpp"
#include "djinn/core/prompt.hpp"


namespace Djinn {

void execute(nlohmann::json tasks) {
    for (auto& task : tasks) {
        // Assuming each task is a JSON object, you can access its fields like this:
        std::string description = task["description"];
        std::string type = task["type"];
        std::string action = task["action"];
        std::string file = task["file"];

        // You can then perform operations based on these fields
        // For example, you might want to print them or execute the action
        std::cout << "Description: " << description << std::endl;
        std::cout << "Type: " << type << std::endl;
        std::cout << "Action: " << action << std::endl;
        std::cout << "File: " << file << std::endl;

        // Execute the action if needed
        // system(action.c_str()); // Uncomment this line to execute the action
    }
}

nlohmann::json encode(ExecutionContext context) {
    // prompt
    std::string system_prompt = fmt_prompt(context, nullptr, "/encoding/system.md");
    std::string user_prompt = fmt_prompt(context, nullptr, "/encoding/user.md");
    std::string res = prompt(system_prompt, user_prompt);

    return nlohmann::json::parse(res);
}

}  // namespace Djinn