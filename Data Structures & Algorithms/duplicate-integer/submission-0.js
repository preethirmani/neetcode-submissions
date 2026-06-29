class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let objMap = {};
        for(let num of nums ) {
            if(objMap[num]) {
                return true;
            } else {
                objMap[num] = 1;
            }
        }
        return false;
    }

}
