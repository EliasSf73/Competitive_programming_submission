class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
       
        friends = list(range(1, n + 1))
        index = 0  # Starting index

        while len(friends) > 1:
            # Calculate the index of the friend to remove
            index = (index + k - 1) % len(friends)
            friends.pop(index)  # Remove the friend at the calculated index

        # The last remaining friend is the winner
        return friends[0]

# # Example usage:
# n_example = 5
# k_example = 2
# winner = findTheWinner(n_example, k_example)
# print(f"The winner is friend number {winner}.")
