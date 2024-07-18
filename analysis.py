import pandas
import matplotlib.pyplot as plt

plt.style.use('dark_background')

colours = {
    'farmed': 'red',
    'lab': 'orange',
    'zoo': 'yellow',
    'companion': 'blue',
    'working': 'purple',
    'wild': 'green',
    'none': 'white',
    'mixed': 'grey'
}
for name in ['talks', 'posters']:

    data = pandas.read_csv('data/' + name + '.csv')
    total_number = len(data)

    plt.figure(figsize = (5.5, 5.5))

    values = data['type'].value_counts()
    labels = values.index
    plt.pie(
        values,
        labels      = labels + ' (' + values.map(str) + ')',
        startangle  = 90,
        counterclock= False,
        colors = [colours[v] for v in labels],
    )
    plt.title(name + ' by animal type\n total number of ' + name + ': ' + str(total_number))
    plt.savefig('output/' + name + '.png', dpi = 500)


