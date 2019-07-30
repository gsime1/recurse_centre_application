## How to run

- clone this repo
- `cd` to `./game_of_fifteen` folder
- run the following from terminal:

`$ python3 game_of_fifteen.py 4` (let's use a dimension of 4x4 board)

what you should see is the following:

```
Hello <YOUR os.uname> from the Recurse Centre!

        WELCOME TO THE GAME OF FIFTEEN

        The game is very simple, you just have to choose the tile you want to swap with the empty tile [_] and move them 
        until the board, which is now upside down, starts again with [1] [2] [3] ... and ends with the empty tile [_].

        Can you do it?
 
        Try! The board is here below, choose your first move!


[15] [14] [13] [12] 
[11] [10]  [9]  [8] 
 [7]  [6]  [5]  [4] 
 [3]  [1]  [2]  [_] 
Please enter the tile you want to move: 
```

## Errors handling

Should you insert a dimension outside of the legal range (3 and 9) or an illegal input you should see the following:

```
Usage: python fifteen.py D.
The desired dimension (D) must be a number between 3 and 9.
```

After board has been initiated you will be prompted with the tile you want to move to replace with the empty tile [_] 
If you provide an invalid input you will be prompted again, you should see:

```
Please enter the tile you want to move: 44444
Invalid input. Try again!
Please enter the tile you want to move: wrong_
Invalid input. Try again!
Please enter the tile you want to move: ..-?
Invalid input. Try again!
Please enter the tile you want to move:  
Invalid input. Try again!
Please enter the tile you want to move: 
```

If you provide a valid tile, but the tile cannot be moved, the move will be considered illegal and you'll be prompted again.

```
Please enter the tile you want to move: 15
You chose a tile which does not seem to be movable, please choose anew.
[15] [14] [13] [12] 
[11] [10]  [9]  [8] 
 [7]  [6]  [5]  [4] 
 [3]  [1]  [2]  [_] 
Please enter the tile you want to move: 
```

