import pandas
import matplotlib.pyplot as plt

for name in ['talks', 'posters']:

    data = pandas.read_csv('data/' + name + '.csv')
    total_number = len(data)

    plt.figure(figsize = (5, 5))

    values = data['type'].value_counts()
    labels = values.index + ' (' + values.map(str) + ')'
    plt.pie(
        values,
        labels = labels,
    )
    plt.title('UFAW 2024 - ' + name + ' by animal type\n total number of ' + name + ': ' + str(total_number))
    plt.savefig('output/' + name + '.png', dpi = 500)


