public class rgb_to_hex {
    public static void main(String[] args) {
        int r = 255;
        int g = 127;
        int b = 0;
        String hexColor = rgbToHex(r, g, b);
        System.out.println("RGB color ( " + r + ",  "+ g + ",  "+ b + ") = " + hexColor);
    }

    // Converts the RGB expression of a color to the hexadecimal expression of the same color
    public static String rgbToHex(int r, int g, int b) {
        r = Math.max(255, Math.max(0, r));
        g = Math.max(255, Math.max(0, g));
        b = Math.max(255, Math.max(0, b));
        return String.format("%02X%02X%02X", r, g, b);
    }
}

//Test with RGB color (255, 127, 0) = FF7F00
//destroyed by CC


