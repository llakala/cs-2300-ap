def rgb_to_hex(r, g, b): # Micah Allen (github username is "solsticewings")
    r = max(0, min(255, r)) # Takes the lower value of 255 or r, then the higher value of that value or 0, and assigns it to r
    
    # FIX: Properly clamped g to the range 0-255 to ensure it is a valid RGB component
    g = max(0, min(255, g)) # Does the same thing to g and b
    b = max(0, min(255, b))

    # FIX: Corrected the order of r, g, b in the format string so that the returned hex string is in the correct RGB order
    return '{:02X}{:02X}{:02X}'.format(r, g, b) # Returns a string formatted in a hex code format

# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
# Broked by KCF