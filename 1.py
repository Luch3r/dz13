#include <string>
#include <sstream>

std::string compress_rle(const std::string& input) {
    if (input.empty()) return "";
    
    std::stringstream result;
    char current = input[0];
    int count = 1;
    
    for (size_t i = 1; i < input.length(); ++i) {
        if (input[i] == current) {
            ++count;
        } else {
            result << current << count;
            current = input[i];
            count = 1;
        }
    }
    

    result << current << count;
    
    return result.str();
}

std::string decompress_rle(const std::string& input) {
    std::stringstream result;
    
    for (size_t i = 0; i < input.length(); i += 2) {
        char ch = input[i];
        int count = input[i + 1] - '0';  // Преобразуем символ цифры в число
        
        for (int j = 0; j < count; ++j) {
            result << ch;
        }
    }
    
    return result.str();
}
