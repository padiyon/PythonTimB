def banner_text(text):
    screen_width = 50
    if len(text) > screen_width -4:
        raise ValueError('String {0} is larger then specified width {1}' .format(text, screen_width))

    if text == '*':
        print('*' * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = '**{0}**'.format(centred_text)
        print(output_string)

banner_text('*')
banner_text('Always look on the bright side of life...')
banner_text('If life seems jolly rotten')
