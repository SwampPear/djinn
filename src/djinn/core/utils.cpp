#include "djinn/core/utils.hpp"

namespace Djinn {

std::string get_time() {
    auto now = std::chrono::system_clock::now();

    // time sync and localization
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    std::tm* local_time = std::localtime(&now_time);

    // ss formatting
    std::ostringstream oss;
    oss << "[" << std::put_time(local_time, "%Y-%m-%d %H:%M:%S") << "]";

    return oss.str();
}

void log(LogColor color, const std::string& level, const std::string& message) {
    // format time
    std::string time = "\033[1m" + get_time() + "\033[0m";

    // format level
    std::string level_pre;
    switch(color) {
        case LogColor::RED      : { level_pre = " \033[91m["; break; }
        case LogColor::GREEN    : { level_pre = " \033[92m["; break; }
        case LogColor::YELLOW   : { level_pre = " \033[93m["; break; }
    }

    std::string fmt_level = level_pre + level + "]\033[0m";

    // formatted message
    std::cout << time << " " << fmt_level << " " << message << std::endl;
}

std::string read_file(const std::string& fp) {
    std::ifstream file(fp);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + fp);
    }

    std::stringstream buffer;
    buffer << file.rdbuf();     // read into buffer
    return buffer.str();        // return as string
}

std::string get_cwd() {
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) == nullptr) {
        throw std::runtime_error("Failed to get current working directory.");
    }

    return std::string(cwd);
}

std::string inject_text(const std::string& prompt, const std::string& key, const std::string& value) {
    std::string result = prompt;
    size_t pos = 0;
    while ((pos = result.find(key, pos)) != std::string::npos) {
        result.replace(pos, key.length(), value);
        pos += value.length();
    }
    return result;
}

std::string fmt_prompt(ExecutionContext context, PromptConfig config, const std::string& fp) {
    std::string prompt_fp = context.data + "/prompts/" + fp;
    std::string prompt = read_file(prompt_fp);

    for (const auto& [key, value] : config) {
        prompt = inject_text(prompt, "{" + key + "}", value);
    }

    return prompt;
}
}  // namespace Djinn