import numpy as np

def position_change(z_score, entry_threshold, exit_threshold):
    """
    Generate a vector of trading positions based on z-score levels. 
    
    Parameters:
        z_score (pd.Series): the z-score time series of the spread.
        entry_threshold (float): threshold to enter a position.
        exit_threshold (float): threshold to exit a position.
    
    Returns:
        List[int]: a list of positions at each time step:
            +1 for LK/SP
            -1 for SK/LP
             0 for no position.
    """
    
    position = 0
    positions = []
    
    for z in z_score: 
        if position == 0:
            if z > entry_threshold:
                position = -1 # SK/LP
            elif z < -entry_threshold:
                position = 1 # LK/SP
        elif np.abs(z) < exit_threshold:
            position = 0 # close position
        positions.append(position)
    return positions
    