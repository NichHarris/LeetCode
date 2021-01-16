class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = 0;
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0, j =0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                // map.get returns value for the which the key (char at i) is mapped
                // math.max compares value and j adn returns highest value
                j = Math.max(map.get(s.charAt(i)), j);
            }
            length = Math.max(length, i - j + 1); // updates current max length without duplicates
            map.put(s.charAt(i), i + 1); // Adds next character from string to hashmap 
        }
        return length;
    }
}