A simple toy tool to experiment with pictures taken from a commercial flight.

The program can load data from a Flightaware log and match the image times to the position of the flight and help 
you figure out where they taken.

# How to use

Set up your python environment with poetry.

Put all your pictures in a folder, together with a saved Flightaware html flight log. See the example in test/data.
Run the following command:

```
python flightsnap.py test/data/ --time_zone_offset 1 --name lebb_egkk
```

That will generate an html file named lebb_egkk.html, you can open it and explore with your browser.
