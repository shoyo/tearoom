## Tearoom of Zero/One

### About
"Tearoom of Zero/One" by Tatsuo Miyajima is an art piece displayed at the Miraikan National Museum of Emerging Science
and Innovation. It represents the chaotic, continuous change of society and human consciousness as a black digital screen
filled with shifting random numbers. Details can be read [here](http://www.miraikan.jst.go.jp/en/info/1105261612933.html).
This art piece seemed like fun to implement so I created this rendition.

### Prerequisites
Be sure to have Python3 (any version should be fine) and Tkinter installed.

### How to Use
To run the art piece, create a local copy of this repository and run:
    
    python3 main.py
    
This should run the art piece that looks something like this:

![alt text](https://github.com/shoyo-inokuchi/tearoom/blob/master/samples/tearoom.png)
    
### Details
The art piece itself (the "Tearoom") is a 7x7 grid of cells, where each cell is either empty or counting up from
1 to 9. The chance that a cell starts counting and the rate at which a cell counts up is determined randomly. The
Tearoom has a lifespan, where after a certain amount of time elapses, all cells become empty and never count again.

### License
Use the code in this repository however you wish. View details in [LICENSE.md](LICENSE.md).
