class Solution(object):
    def isValid(self, s):
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the top element, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were properly matched
        return len(stack) == 0