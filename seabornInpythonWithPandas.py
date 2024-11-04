
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



sns.set(color_codes=True)

auto = pd.read_csv('automobileDataFromGrtLrgPractice.csv');

print( auto.head())

# sns.displot(auto['city_mpg'])
# sns.displot(auto['city_mpg'] , kde = True ,rug=True)
# sns.jointplot(auto['city_mpg'])
# sns.jointplot(x='city_mpg' , y='horsepower' , data=auto)
# sns.jointplot(x='city_mpg' , y='horsepower' , data=auto , kind='resid')

# error
# sns.displot(auto['city_mpg' , 'engine_size' , 'horsepower'])

# sns.stripplot( x = 'fuel_type', y ='horsepower' , data=auto )
# sns.stripplot( x = 'fuel_type', y ='horsepower' , data=auto , jitter=False )
# sns.swarmplot( x = 'fuel_type', y ='horsepower' , data=auto  )
# sns.boxenplot( x = 'fuel_type', y ='horsepower' , data=auto  )
sns.boxenplot( x = 'fuel_type', y ='horsepower' , data=auto , hue=auto['fuel_type'] )


plt.savefig('plot.jpg')
plt.show()


