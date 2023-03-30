import numpy as np
import cmath
import matplotlib.pyplot as plt


def get_user_choice():
    """
    Prompt the user for the transfer function number (1 or 2).

    Returns
    -------
    int
        The user-selected transfer function number (1 or 2).
    """
    while True:
        try:
            choice = int(input("Enter the transfer function number (1 or 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_poles_and_zeros(choice):
    """
    Prompt the user for the poles and zeros
    based on the selected transfer function.

    Parameters
    ----------
    choice : int
        The user-selected transfer function number (1 or 2).

    Returns
    -------
    tuple of list of float
        The zeros and poles of the transfer function.
    """
    if choice == 1:
        z1 = float(input("Enter the zero z1 (0 to 1E8): "))
        p1 = float(input("Enter the pole p1 (0 to 1E8): "))
        return [z1], [p1]
    elif choice == 2:
        z1 = float(input("Enter the zero z1 (0 to 1E8): "))
        z2 = float(input("Enter the zero z2 (0 to 1E8): "))
        p1 = float(input("Enter the pole p1 (0 to 1E8): "))
        p2 = float(input("Enter the pole p2 (0 to 1E8): "))
        return [z1, z2], [p1, p2]


def get_frequency_range():
    """
    Prompt the user for the start and stop frequency.

    Returns
    -------
    tuple of float
        The start and stop frequencies.
    """
    start_freq = float(input("Input start frequency (minimum 1): "))
    stop_freq = float(input("Input stop frequency (maximum 1E9): "))
    return start_freq, stop_freq


def transfer_function(choice, zeros, poles, s):
    """
    Calculate the transfer function for the given parameters.

    Parameters
    ----------
    choice : int
        The user-selected transfer function number (1 or 2).
    zeros : list of float
        The zeros of the transfer function.
    poles : list of float
        The poles of the transfer function.
    s : complex
        The complex variable s.

    Returns
    -------
    complex
        The transfer function H(s) value.
    """
    if choice == 1:
        H = (s + zeros[0]) / (s + poles[0])
    elif choice == 2:
        H = (s + zeros[0]) * (s + zeros[1]) / ((s + poles[0]) * (s + poles[1]))
    return H


def calculate_magnitude_and_phase(choice, zeros, poles, start_freq, stop_freq):
    """
    Calculate the magnitude and phase of the
    transfer function over the specified frequency range.

    Parameters
    ----------
    choice : int
        The user-selected transfer function number (1 or 2).
    zeros : list of float
        The zeros of the transfer function.
    poles : list of float
        The poles of the transfer function.
    start_freq : float
        The start frequency.
    stop_freq : float
        The stop frequency.

    Returns
    -------
    list of tuple
        A list of tuples containing frequency, magnitude, and phase.
    """
    num_points = 1000
    frequencies = np.logspace(
        np.log10(start_freq), np.log10(stop_freq), num_points)
    magnitude_phase_list = []

    for freq in frequencies:
        s = complex(0, 2 * np.pi * freq)
        H = transfer_function(choice, zeros, poles, s)
        magnitude = abs(H)
        phase = np.degrees(cmath.phase(H))
        magnitude_phase_list.append((freq, magnitude, phase))

    return magnitude_phase_list


def display_table(magnitude_phase_list):
    """
    Display the magnitude and phase in a tabular format.

    Parameters
    ----------
    magnitude_phase_list : list of tuple
        A list of tuples containing frequency, magnitude, and phase.
    """
    print("Frequency (Hz) | Magnitude | Phase (degrees)")
    for freq, magnitude, phase in magnitude_phase_list:
        print(f"{freq:.2f} | {magnitude:.4f} | {phase:.2f}")


def plot_bode(magnitude_phase_list):
    """
    Plot the Bode plot with magnitude and phase.

    Parameters
    ----------
    magnitude_phase_list : list of tuple
        A list of tuples containing frequency, magnitude, and phase.
    """
    frequencies, magnitudes, phases = zip(*magnitude_phase_list)

    _, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.semilogx(frequencies, 20 * np.log10(magnitudes))
    ax1.set_ylabel('Magnitude (dB)')
    ax1.grid(which='both', linestyle='-', linewidth=0.5)
    ax1.set_title('Bode plot')

    ax2.semilogx(frequencies, phases)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.grid(which='both', linestyle='-', linewidth=0.5)

    plt.show()


def main():
    """
    Main function to execute the program.
    """
    while True:
        choice = get_user_choice()
        zeros, poles = get_poles_and_zeros(choice)
        start_freq, stop_freq = get_frequency_range()

        magnitude_phase_list = calculate_magnitude_and_phase(
            choice, zeros, poles, start_freq, stop_freq)
        display_table(magnitude_phase_list)
        plot_bode(magnitude_phase_list)

        user_input = input(
            "Do you want to input another case? Enter 'y' to continue or "
            "any other key to exit: ")
        if user_input.lower() != 'y':
            break


if __name__ == "__main__":
    main()
