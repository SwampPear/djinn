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

    return nlohmann::json::parse(res);
}

}  // namespace Djinn