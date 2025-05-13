#include <map>
#include "djinn/core/utils.hpp"


namespace Djinn {

typedef std::map<std::string, std::string> PromptConfig;

std::string fmt_prompt(const std::string& fp, PromptConfig config) {
    return read_file(fp);
}

}  // namespace Djinn