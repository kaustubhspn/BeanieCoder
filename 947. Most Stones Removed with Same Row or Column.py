class Solution:
    def __init__(self):
        self.par = []  # List to store parent indices
        self.rank = []  # List to store ranks (sizes) of disjoint sets

    def find_parent(self, x):
        # Recursive function to find the parent of a given element x
        if x == self.par[x]:  # If x is the parent of itself
            return x
        self.par[x] = self.find_parent(self.par[x])  # Path compression
        return self.par[x]

    def union(self, x, y):
        par_x = self.find_parent(x)  # Find the parent of x
        par_y = self.find_parent(y)  # Find the parent of y

        if par_x == par_y:  # If x and y already belong to the same set
            return False

        if self.rank[par_x] < self.rank[par_y]:
            # Merge the smaller set (par_x) into the larger set (par_y)
            par_x, par_y = par_y, par_x

        self.rank[par_x] += self.rank[par_y]  # Update the size of the merged set
        self.par[par_y] = par_x  # Set the parent of par_y to par_x
        return True

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)  # Number of stones
        self.par = [i for i in range(n)]  # Initialize parent list with each stone as its own parent
        self.rank = [1 for i in range(n)]  # Initialize rank list with each rank set to 1 (initial size)
        X = {}  # Dictionary to store occupied rows
        Y = {}  # Dictionary to store occupied columns
        count = 0  # Counter for the number of stones removed

        for i, (x, y) in enumerate(stones):
            if x in X:
                count += self.union(i, X[x])  # Union current stone with the stone in the same row
            else:
                X[x] = i  # Set the current stone as the representative for the row x

            if y in Y:
                count += self.union(i, Y[y])  # Union current stone with the stone in the same column
            else:
                Y[y] = i  # Set the current stone as the representative for the column y

        return count  # Return the number of stones removed
