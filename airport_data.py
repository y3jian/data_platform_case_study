import pandas as pd
from io import StringIO

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

# Parse the string and convert to data frame
data_frame = pd.read_csv(StringIO(data), sep = ';')

# 1. FlightCodes column
# Flight codes increase by 10 with each row
for i in range (1, len(data_frame)):
    # if the column at row i is missing
    if pd.isna(data_frame.loc[i, 'FlightCodes']):
        # The flight code is the previous flight code + 10
        data_frame.loc[i, 'FlightCodes'] = data_frame.loc[i - 1, 'FlightCodes'] + 10

# Convert to integer column 
data_frame['FlightCodes'] = data_frame['FlightCodes'].astype(int)
print(data_frame)