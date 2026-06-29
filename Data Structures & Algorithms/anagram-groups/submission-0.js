class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();
        for(let str of strs) {
            let charSeq = new Array(26).fill(0);
            for(let s of str) {
                charSeq[s.charCodeAt(0)-'a'.charCodeAt(0)]++;
            }
            const key = charSeq.join(',');
            if(!map.has(key)) {
                map.set(key,[]);
            }
            map.get(key).push(str);
        }
         return Array.from(map.values());
    }

   
}
