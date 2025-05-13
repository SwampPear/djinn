#include <map>
#include "djinn/core/context.hpp"
#include "djinn/core/utils.hpp"
#include "djinn/core/prompt.hpp"


namespace Djinn {

nlohmann::json encode(ExecutionContext context) {
    // prompt
    std::string system_prompt = fmt_prompt(context, nullptr, "/encoding/system.md");
    std::string user_prompt = fmt_prompt(context, nullptr, "/encoding/user.md");
    std::string res = prompt(system_prompt, user_prompt);

    nlohmann::json res_data = nlohmann::json::parse(res);

    for (const auto& task : res_data) {
        std::string action = task["action"];
        std::string description = task["description"];
        std::string type = task["type"];

        // Log the description of the task
        Djinn::log(Djinn::LogColor::GREEN, type, description);
    }

    return res_data;
}

}  // namespace Djinn