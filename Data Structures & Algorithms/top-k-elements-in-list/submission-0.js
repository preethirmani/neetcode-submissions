class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = new Map();
        let result = [];
        let count = 0 ;
        for(let i = 0; i < nums.length; i++) {
            if(map.has(nums[i])) {
                map.set(nums[i], map.get(nums[i]) + 1);
            } else {
                map.set(nums[i], 1);
            }
        }
        let sortedMap = new Map([...map.entries()].sort((a,b) => b[1] - a[1]));

        for(let [key,value] of sortedMap) {
            if(count < k) {
                result.push(key);
                count++;
            }
        }
        return result;

    }
}
