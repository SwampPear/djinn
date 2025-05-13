#pragma once 

#include <iostream>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <map>
#include <unistd.h>
#include "nlohmann/json.hpp"
#include "djinn/core/context.hpp"

namespace Djinn {

enum LogColor {
    RED,
    GREEN,
    YELLOW 
};

typedef std::map<std::string, std::string> PromptConfig;

/**
 * @brief Retrieves the current local time as a formatted string.
 *
 * This function captures the current time from the system clock, converts it
 * to a local time representation, and formats it into a string with the 
 * pattern "[YYYY-MM-DD HH:MM:SS]". The formatted string is then returned.
 *
 * @return std::string The current local time formatted as 
 * "[YYYY-MM-DD HH:MM:SS]".
 */
std::string get_time();

/**
 * @brief Logs a message with a specified color and level.
 *
 * This function outputs a log message to the console with a given color and 
 * level. The message is prefixed with the current time.
 *
 * @param color The color to display the log level.
 * @param level The level of the log message (e.g., INFO, ERROR).
 * @param message The message to log.
 */
void log(LogColor color, const std::string& level, const std::string& message);

/**
 * @brief Reads the contents of a file.
 *
 * This function opens a file specified by the file path and reads its 
 * contents into a string.
 *
 * @param fp The file path to read from
 * @return std::string The contents of the file
 * @throws std::runtime_error if the file cannot be opened
 */
std::string read_file(const std::string& fp);

/**
 * @brief Retrieves the current working directory.
 *
 * This function gets the current working directory of the process.
 *
 * @return std::string The current working directory.
 * @throws std::runtime_error if the current working directory cannot be retrieved.
 */
std::string get_cwd();

/**
 * @brief Replaces all occurrences of a key in a prompt with a specified value.
 *
 * This function searches for all instances of a given key within a prompt string
 * and replaces them with the provided value. The search and replace operation
 * continues until all occurrences of the key are replaced.
 *
 * @param prompt The original string containing placeholders.
 * @param key The placeholder key to be replaced.
 * @param value The value to replace the key with.
 * @return std::string The modified string with all key occurrences replaced by the value.
 */
std::string inject_text(const std::string& prompt, const std::string& key, const std::string& value);

/**
 * @brief Formats a prompt by injecting configuration values into placeholders.
 *
 * This function reads a prompt file, then iterates over a configuration map to
 * replace placeholders in the prompt with corresponding values from the map.
 * Placeholders in the prompt are denoted by curly braces around the key names.
 *
 * @param context The execution context containing data directory information.
 * @param config A map of key-value pairs for placeholder replacement.
 * @param fp The file path of the prompt relative to the data directory.
 * @return std::string The formatted prompt with placeholders replaced by config values.
 */
std::string fmt_prompt(ExecutionContext context, PromptConfig* config, const std::string& fp);

}  // namespace Djinn