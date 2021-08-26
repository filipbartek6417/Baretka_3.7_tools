import baretka_fib
import baretka_pascal
import baretka_pi_calculation
import baretka_perm_comb_var

if __name__ == '__main__':
    while (y := int(input('Nth fibonacci number or -1 to exit: '))) != -1:
        print('Recursive:', baretka_fib.recursive_fib(y))
        print('Iterative field:', baretka_fib.iterative_field_fib(y))
        print('Iterative variable:', baretka_fib.iterative_variable_fib(y))
        print('Explicit:', baretka_fib.explicit_fib(y))
        y = int(input('Number of pascal triangle rows: '))
        print('Explicit:', baretka_pascal.explicit_pascal(y))
        print('Recursive:', baretka_pascal.recursive_pascal(y))
        print('Dynamic programming:', baretka_pascal.dynamic_pascal(y))
        y = int(input('Pi calculation, number of simulations (will be automatically multiplied by 100000): '))
        print('Gregory-leibniz:', baretka_pi_calculation.gregory_leibniz(y * 100000))  # To adjust for the difference in needed input
        print('Archmiedes:', baretka_pi_calculation.archimedes_method(y * 100000))
        print('Monte carlo:', baretka_pi_calculation.monte_carlo(y * 100000))
        print('Buffon needle:', baretka_pi_calculation.buffon_needle(y * 100000))
        x = input('Perm_comb_var set of characters: ')
        y = int(input('Length of resulting elements: '))
        print('Permutations:', baretka_perm_comb_var.permutations(x))
        print('Combinations:', baretka_perm_comb_var.combinations(x, y))
        print('Repeating combinations:', baretka_perm_comb_var.repeating_combinations(x, y))
        print('Variations:', baretka_perm_comb_var.variations(x, y))
        print('Repeating variations:', baretka_perm_comb_var.repeating_variations(x, y))
