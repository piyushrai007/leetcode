  class Solution { 
    public int bs(int a[], int i, int j, int target) {
        // Base case: if the left index exceeds the right index, return -1 (not found)
        if (i > j) {
            return -1;
        }
        
        int mid = (i + j) / 2; // Find the middle element
        
        // Check if the middle element is the target
        if (a[mid] == target) {
            return mid;
        } 
        // If target is less than mid, search in the left half
        else if (target < a[mid]) {
            return bs(a, i, mid - 1, target);
        } 
        // If target is greater than mid, search in the right half
        else {
            return bs(a, mid + 1, j, target);
        }
    }
    
    public int search(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1; // Correct way to get the length of the array
        return bs(nums, i, j, target); // Call the binary search function
    }
}
