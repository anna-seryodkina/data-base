import datamain
import analysis
import data_backend


def get_site(userinput):
    user_input_array = userinput.split(' ')
    if data_backend.website_exists_by_name(user_input_array[1]):
        return user_input_array[1]
    else:
        print('>> website does not exist.')


print('\ncommands:\n> generate\n> counter {site name}\n> graph\n> popular-pages {site name}\n> exit\n')

inp = input('enter command: ')

while True:
    try:
        if inp == 'generate':
            datamain.run()

        elif inp.startswith('counter'):
            sitename = get_site(inp)
            analysis.counter(sitename)

        elif inp.startswith('graph'):
            fname = analysis.make_graph()
            print(f'graph saved to {fname}.png')

        elif inp.startswith('popular-pages'):
            sitename = get_site(inp)
            fname = analysis.make_popular_diagram(sitename)
            print(f'diagram saved to {fname}.png')

        elif inp == '' or inp == 'exit':
            break
        else:
            print('>> oops. wrong command.')
    except:
        print('>> incorrect input.')

    inp = input('enter command: ')

