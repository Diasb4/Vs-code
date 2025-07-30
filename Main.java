// class Solution {
//     public double findMedianSortedArrays(int[] nums1, int[] nums2) {
//         int m = nums1.length, n = nums2.length;
//         int total = m + n;
//         int mid1 = (total - 1) / 2;
//         int mid2 = total / 2;

//         int i = 0, j = 0, count = 0;
//         int current = 0, prev = 0;

//         while (count <= mid2) {
//             prev = current;

//             if (i < m && (j >= n || nums1[i] <= nums2[j])) {
//                 current = nums1[i++];
//             } else {
//                 current = nums2[j++];
//             }

//             count++;
//         }

//         if (total % 2 == 0) {
//             return (prev + current) / 2.0;
//         } else {
//             return current;
//         }
//     }

//     public static void main(String[] args) {
//         System.out.println(new Solution().findMedianSortedArrays(new int[] { 1, 3 }, new int[] { 2 })); // Output: 2.0
//         System.out.println(new Solution().findMedianSortedArrays(new int[] { 1, 2 }, new int[] { 8, 4 })); // Output:
//                                                                                                            // 2.5
//     }
// }

import java.util.*;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.length;
        double[][] workers = new double[n][2]; // [ratio, quality]

        for (int i = 0; i < n; i++) {
            workers[i][0] = (double) wage[i] / quality[i];
            workers[i][1] = quality[i];
        }

        Arrays.sort(workers, (a, b) -> Double.compare(a[0], b[0])); // сортировка по ratio

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int qualitySum = 0;
        double result = Double.MAX_VALUE;

        for (double[] worker : workers) {
            int q = (int) worker[1];
            qualitySum += q;
            maxHeap.offer(q);

            if (maxHeap.size() > k) {
                qualitySum -= maxHeap.poll(); // удаляем самого "дорогого" по качеству
            }

            if (maxHeap.size() == k) {
                result = Math.min(result, qualitySum * worker[0]); // текущий ratio * суммарное качество
            }
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.mincostToHireWorkers(new int[] { 10, 20, 5 }, new int[] { 70, 50, 30 }, 2)); // Output:
                                                                                                                 // 105.0
        System.out
                .println(solution.mincostToHireWorkers(new int[] { 3, 1, 10, 10, 1 }, new int[] { 4, 8, 2, 2, 7 }, 3)); // Output:
                                                                                                                        // 30.666666666666668
    }
}