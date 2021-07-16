# StockBot, a simple weekend project to stave off boredom!

## Description
StockBot is a Python application that takes in a list of stocks and produces a csv file that contains all relevant stock information (Name, High, Low, Opening Price, Closing Price, Volume, Adj Close)

## Steps
1. Open a text file and write down a list of stocks. Make sure each stock takes up only 1 line. The program will filter away all incorrect stock names.
2. Save the text file in the same folder as test.py. Otherwise, make sure to specify the correct path name when you run.
3. Open terminal to run test.py and add the text file after "python test.py" in the command line -> "python test.py abc.txt" 
4. Wait for program to finish running, then navigate to the generated csv file in the folder. 

## Libraries
Make sure the following libraries are installed:
- pandas -> standard data manipulation library
- pandas_datareader -> stock information, pulled from Yahoo Finance
- Datetime -> date and time
- Os -> modify files (removing them in this case)
- Csv -> creates csv file
- Sys -> enables command line arguments

## A bangin' presentation
https://docs.google.com/presentation/d/1NwA_tamA2cE_hol5gxJFU1VeB4zjZcKt6j8WeOwEN7s/edit?usp=sharing
