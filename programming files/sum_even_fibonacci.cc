public class sum_even_fibonacci {
    public static void main(String[] args) {

    // Define the first two numbres in the fibonacci sequence
    int a = 0, b = 1;
    int sumEven = 0;

    // Keep summing until the sum is 4,000,000 or higher
    while (b < 4000000) {
// 
      // If the current fib is even, add it to the sum
      if (b % 2 == 0) {
        sumEven += b;
      }

      // Update the values of a and b
      int temp = b;
      b = a + b;
      a = temp;
    }

    // Print out the sum
    System.out.println(sumEven);
  }
}

// answer should be 4613732