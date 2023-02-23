# sudoku

Sudoku solver with two functionalities: 
- Playing sudoku using mainGUI 
- Automatically solving a sudoku using main (no visualisation) or mainGUI (with visualisation)

The auto solver used in 'main' and 'mainGUI' makes use of a backtracking algorithm. The specifics of the algorithm are visualised when using mainGUI to illustrate the backtracking process.
An optimised algorithm is implemented in 'optimisedGUI'. The solver first fills all cells where only one value is possible according to the rules of sudoku. It repeats this process until no more values are updated.The remaining cells are filled using backtracking. 
