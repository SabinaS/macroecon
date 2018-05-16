import pandas as pd

def prepareData():
    ''' Prepare the data we will work with.
        
	Return
	------
	data: pandas df
	      csv data cleaned up and converted into df
    '''
    filepath = '~/home/sabina/programming/git/macroecon/dax_components.csv'
    data = pd.read_csv( filepath, error_bad_lines = False )
    data.dropna( axis = 0, how = 'any' )
    return data



