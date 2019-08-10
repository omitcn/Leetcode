class Solution:
    def isRobotBounded(self, instructions):
        if 'G' in instructions and 'L' in instructions and 'R' in instructions:
            if instructions.count('L')==instructions.count('R'):
                return False
            else:
                return True
        elif 'G' in instructions and 'L' not in instructions and 'R' not in instructions:
            return False
        elif 'G' not in instructions:
            return True
        else:
            return True