# Solution Idea
If you just take the given path and reverse each move, so you will solve the maze and never replicate a move.
The proof is easy.
* Any path `P` that contains `N - 1` `E` characters and `N - 1` `S` characters is a valid path, since there are no barries in the maze.
* The given path is a valid path.
* Reversing `E` and `S` in the valid path will result in a valid path.
* This path will never overlap the given path
    * From the first step, the two paths will diverge.
    * They are symmetric - that is, if they overlap on a square, they will have taken the same number of moves
    * If on some move `i`, they are in the same square, the two paths will necessarily NOT take the same next step by construction (if `P[i] = `E`, then `P2[i] = `S`, so they will not replicate).



Google's Reasoning for the solution:
To solve this test set, let's just invert all of the moves in Lydia's path. That is, every time she moves east, let's move south, and every time she moves south, let's move east. For example, if Lydia's path is EESSSESE, then our path will be SSEEESES.

Let's understand why this inverted path is a correct answer to the problem.

First, notice that we still make N - 1 moves to the east and N - 1 moves to the south, so we will arrive at the southeast cell in the end as required, and we will not step out of the bounds of the maze.

Now let's see why we will not reuse any of Lydia's moves. Suppose this is not the case, and we reuse a move from the position that is X moves to the east and Y moves to the south in some order from the northwest cell. Recall that the order of moves does not matter, and there may be many ways to get to this position, but all of them will require exactly X moves to the east and Y moves to the south. What will be the next move? We know that Lydia's next move is the (X + Y + 1)-th symbol in the string representing her path (with indexing starting from one), and our next move is the (X + Y + 1)-th symbol in the string representing our path. But since our path string is an inverted version of Lydia's path string, we know that (X + Y + 1)-th symbols of the two strings will be different, which contradicts our assumption that we will have the same next move. By the same logic, we can see that the two paths will not reuse any other moves along the way.
