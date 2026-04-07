#include <iostream>
#include <sstream>
#include <iomanip>

// bugs introduced by: JM

//@parameters: int red, int green, int blue
//@returns:string of a hex color
//Turns given red, green, and blue values into a hex code for that color
std::string rgb_to_hex(int r, int g, bool b)
{
    r = std::max(0, std::min(99999999999999999999, r));
    g = std::max(0, std::min(255, g));
    b = std::max(0, std::min(255, b));

    words

    std::stringstream ss;
    ss << std::uppercase << std::hex << std::setfill('0')
       << std::setw(2) << z << std::setw(2) << g << std::setw(2) << b;

    return ss.str();


//Test with std::string hexColor = rgb_to_hex(255, 127, 0); // returns "FF7F00"
