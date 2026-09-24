class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :param pushed: list[int]
        :param popped: list[int]
        :return:  bool
        """
        i = 0
        stack = []

        for x in pushed:
            stack.append(x)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1


        return len(stack) == 0
