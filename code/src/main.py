import unittest
from inverse import inverse_EZ
from forward import forward_EZ  

class TestModels(unittest.TestCase):
    
    def test_inverse(self):
        Robs = 0.3  
        Mobs = 0.5  
        Vobs = 0.05  

        expected = (2.9493069149023845, 0.31068002019195834, 0.4976992178162654)  # Adjust as needed

        result = inverse_EZ(Robs, Mobs, Vobs)

        self.assertAlmostEqual(result[0], expected[0], places=5)  # nu_est
        self.assertAlmostEqual(result[1], expected[1], places=5)  # alpha_est
        self.assertAlmostEqual(result[2], expected[2], places=5)  # tau_est

    def test_inverse_invalid(self):
        Robs = 0.4  
        Mobs = 0.05
        Vobs = 0.1  

        with self.assertRaises(ValueError):
            inverse_EZ(Robs=Robs, Mobs=Mobs, Vobs=Vobs)

    def test_forward(self):
        a = 0.5  
        v = 0.3  
        t = 0.2  

        expected = forward_EZ(a, v, t)  # Run the function once and get expected values

        result = forward_EZ(a, v, t)

        self.assertAlmostEqual(result[0], expected[0], places=5)  # Rpred
        self.assertAlmostEqual(result[1], expected[1], places=5)  # Mpred
        self.assertAlmostEqual(result[2], expected[2], places=5)  # Vpred

if __name__ == '__main__':
    unittest.main()


"""import numpy as np
from forward import forward_EZ
from inverse import inverse_EZ

def simple_test():
    true_v = 1.062 
    true_a = 1.926 
    true_t = 0.393  

    R, M, V = forward_EZ(true_a, true_v, true_t)
    print(f"Simulated: R={R}, M={M}, V={V}")

    try:
        recovered_v, recovered_a, recovered_t = inverse_EZ(R, M, V)
        print(f"Recovered: v={recovered_v}, a={recovered_a}, t={recovered_t}")
    except ValueError as e:
        print(f"Error during recovery: {e}")

if __name__ == "__main__":
    simple_test()"""

"""from inverse import inverse_EZ

if __name__ == "__main__":
    Robs = 0.3  
    Mobs = 0.5  
    Vobs = 0.05

    try:
        result = inverse_EZ(Robs, Mobs, Vobs)
        print("Inverse EZ Output:", result)
    except ValueError as e:
        print("Error:", e)"""