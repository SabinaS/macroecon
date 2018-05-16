import pandas as pd


def prepareData( returnType ):
    ''' Prepare the data that we will work with.
   	
	Parameters
	----------
	returnType: string
 	     either "df", "series" or "list"

	Return
	------
	depending on the input, return either a df,
	a tuples of pandas series, or tuple of lists
    '''
    filepath = '~/home/sabina/programming/git/macroecon/temps_csv.csv'
    data = pd.read_csv( filepath, errort_bad_lines = False )
    oil_prices = data[ 'Oil Price' ] #Series
    prices = oil_prices.tolist() #List
    nyc_temps = data[ 'NYC Temps' ] #Series
    temps = nyc_temps.tolist() #List
    if returnType == 'df':
        return data
    elif returnType == 'series':
        return ( nyc_temps, oil_prices )
    else:
        return ( temps, prices )


def runLinearRegression_SciPy( independ_data, depend_data ):
    ''' Run linear regression on two data sets using 
        SciPy stats lib

        Parameters
        ----------
        independ_data: list 
              list containing independent data
        depend_data: list
              list containing dependent data

        Return
        ------
        r_sqaured: float
              the r dqaured value of the linear regression
    '''
    import scipy.stats
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(
        independ_data, depend_data )
    r_squared = r_value ** 2
    return r_squared


def runLinearRegression_SkLearn( data, depend_data ):
    ''' Run linear regression on two data sets using sklearn
    
        Parameters
        ----------
        data: Pandas dataframe
              dataframe containing both independent and dependent data
        depend_data: Pandas series
              series containing just the dependent data

	Return
	------
	r_sqaured: float
	      the r dqaured value of the linear regression 
    '''
    from sklearn import linear_model
    lm = linear_model.LinearRegression()
    temp_data = pd.DataFrame( data, columns = [ 'NYC Temps' ] ) #Temperature data
    temp_data.dropna( axis = 0, how = 'any' )
    model = lm.fit( temp_data_ depend_data )
    r_squared = lm.score( temp_data, depend_data )
    return r_sqaured 
