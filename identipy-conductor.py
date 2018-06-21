from cmath import pi, sqrt

mat_values = {
    'air': (1, 0, 1.00000037),
    'fresh water': (80, 5e-4, 0.999992),
    'sea water': (80, 3, 1),
    'ice': (3.5, 1e-5, 1),
    'clay': (20, 5, 1),
    'saturated sand': (30, 1e-4, 1),
    'barium titanate': (3279, 1e-6, 1),
    'cold rolled steel': (1, 1e-7, 100),
    'purified iron': (1, 1e-7, 5e3),
    'mu metal': (1, 1.6e6, 2e5),
    '2-81 permalloy': (1, 1e2, 1e6),
    'copper': (1, 5.96e7, 0.999994),
    'gold': (1, 4.1e7, 1),
    'aluminium': (1, 3.5e7, 1.000022),
    'tungsten': (1, 1.79e7, 1),
    'graphite': (12.5, 2e5, 1),
    'diamond': (7.5, 1e-13, 0.99999975),
    'silicon': (11.68, 1.56e-3, 1),
    'glass': (65, 1e-15, 1),
    'kiln dried wood': (4, 1e-15, 1.000000435),
    'ptfe': (2.1, 1e-25, 1)
}


def main_funct(mat):
    """
    Main Function [main_funct()] takes the material provided in 'main_prompt'
    and uses it as an arguement for this function.
    * Example:
    If 'main_prompt' is 'air', the function will run as main_funct('air') and
    will plug-in its key values for use in the relevant math.
    """
    while True:
        try:
            freq = float(input('\nWhat frequency (in Hertz) is the material'
                               ' operating at? '))
        except ValueError:
            print('Please type in only numbers for operating frequency...')
        else:
            break

    eo = 8.854 * 10 ** -12
    uo = 1.26 * 10 ** -6
    w = 2 * pi * freq * mat[0] * eo
    test = mat[1] / w
    if test == 0:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as a Lowless Medium!')
        alpha = 0
        print('\n  The attenuation constant, alpha,'
              f' has a value of {alpha} Np/m, and ')
        beta = (w / (sqrt(uo * mat[2] * eo * mat[0])))
        print(f'  beta has a value of {beta} rad/m.')
        nc = ((mat[2] * uo) / (eo * mat[0]))
        print('  The intrinsic impedance of this lowless'
              f' medium is {nc} ohms.')
        up = (1 / (mat[0] * eo * mat[2] * uo))
        lam = float(up / freq)
        print(f'\n  The phase velocity is {up} meters per second\n'
              f'  with a wavelength of {lam} meters.\n')
        input('Press Enter to continue... \n')
    elif test <= 0.01:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as a Low-Less Medium!')
        alpha = ((mat[1] / 2) * sqrt((uo * mat[2])/(eo * mat[0])))
        print('\n  The attenuation constant, alpha,'
              f' has a value of {alpha} Np/m, and ')
        beta = (w / (sqrt(uo * mat[2] * eo * mat[0])))
        print(f'  beta has a value of {beta} rad/m.')
        nc = ((mat[2] * uo) / (eo * mat[0]))
        print('  The intrinsic impedance of this low-less'
              f' medium is {nc} ohms.')
        up = (1 / (mat[0] * eo * mat[2] * uo))
        lam = float(up / freq)
        print(f'\n  The phase velocity is {up} meters per second\n'
              f'  with a wavelength of {lam} meters.\n')
        input('Press Enter to continue... \n')
    elif test >= 100:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as a Good Conductor!')
        alpha = sqrt(pi * freq * uo * mat[2] * mat[1])
        print('\n  The attenuation constant, alpha,'
              f' has a value of {alpha} Np/m, and ')
        beta = sqrt(pi * freq * uo * mat[2] * mat[1])
        print(f'  beta has a value of {beta} rad/m.')
        nc = complex((1 + 1j) * (alpha / mat[1]))
        print('  The intrinsic impedance of this'
              f' good conductor is {nc} ohms.')
        up = sqrt(4 * pi * freq * uo * mat[2] * mat[1])
        lam = up / freq
        print(f'\n  The phase velocity is {up} meters per second\n'
              f'  with a wavelength of {lam} meters.\n')
        input('Press Enter to continue...\n')
    else:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as an Any Medium!')
        alpha = (w * (sqrt((uo * mat[2] * eo * mat[0]) *
                           sqrt(1 + ((test) ** 2)) - 1)))
        print('\n  The attenuation constant, alpha,'
              f' has a value of {alpha} Np/m, and ')
        beta = (w * (sqrt((uo * mat[2] * eo * mat[0]) *
                          sqrt(1 + ((test) ** 2)) + 1)))
        print(f'  beta has a value of {beta} rad/m.')
        nc = complex((sqrt((uo * mat[2]) / (eo * mat[0]))) *
                     sqrt((1 - (1j * test))))
        print(f'  The intrinsic impedance of this any medium is {nc} ohms.')
        up = (w / beta)
        lam = ((2 * pi) / beta)
        print(f'\n  The phase velocity is {up} meters per second\n'
              f'  with a wavelength of {lam} meters.\n')
        input('Press Enter to continue...\n')


while True:
    main_prompt = (input('\nWelcome to the Conductor Calculator!\n'
                         'For a list of materials currently '
                         'supported, enter \'help\'.\n'
                         'What material are you'
                         ' working with? ').lower())
    if main_prompt == 'help':
        print('\nCurrently supports the following materials:\n'
              '\n'
              'Air, Fresh Water, Sea Water, Ice, Clay, Saturated Sand,'
              ' Barium Titanate, Cold Rolled Steel, Purified Iron, Mu Metal,'
              ' 2-81 Permalloy, Copper, Gold, Aluminum, Tungsten, Graphite,'
              ' Diamond, Silicon, Glass, Kiln Dried Wood & PTFE.\n'
              '\n'
              'Please type one of the above materials when prompted.\n')
    else:
        try:
            main_funct(mat_values[main_prompt])
            while True:
                again_prompt = input('Would you like to try another'
                                     ' calculation?\n'
                                     'Please type either'
                                     ' Yes or No:\n\n').lower()
                if again_prompt == '':
                    print('No input given. Please type either Yes or No:\n\n')
                elif again_prompt[0] == 'n':
                    print('\nGoodbye!\n\n\n\n')
                    quit()
                elif again_prompt[0] == 'y':
                    break
                else:
                    print('\nI didn\'t quite understand that...')
        except KeyError:
            if main_prompt == '':
                print('\n You did not specify a material.\n'
                      ' Please use a valid material listed in the'
                      ' \'help\' command.\n')
            else:
                print(f'\n {main_prompt} is not a valid material.\n'
                       ' Please use a valid material listed in the'
                       ' \'help\' command.\n')