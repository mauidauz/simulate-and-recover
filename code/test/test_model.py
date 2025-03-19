import unittest
from src.inverse import inverse_EZ
from src.forward import forward_EZ  # Assuming forward_EZ is in forward.py

class TestModels(unittest.TestCase):
    
    # Test for valid inputs in inverse_EZ function
    def test_inverse(self):
        Robs = 0.3  # Example of valid observed accuracy
        Mobs = 0.5  # Example of valid observed mean response time
        Vobs = 0.05  # Example of valid observed variance
        
        # Expected output values (replace with correct expected results)
        expected = (2.9493069149023845, 0.31068002019195834, 0.4976992178162654)  # Replace with actual expected values for nu_est, alpha_est, tau_est

        # Call inverse_EZ function
        result = inverse_EZ(Robs, Mobs, Vobs)
        
        # Assert that the result matches the expected values (with a tolerance)
        self.assertAlmostEqual(result[0], expected[0], places=5)  # nu_est
        self.assertAlmostEqual(result[1], expected[1], places=5)  # alpha_est
        self.assertAlmostEqual(result[2], expected[2], places=5)  # tau_est

    # Test for invalid inputs in inverse_EZ function (discriminant < 0)
    def test_inverse_invalid(self):
        # Input values that will cause a negative discriminant (invalid for inverse_EZ)
        Robs = 0.4  # Close to 0.5, might lead to invalid sqrt
        Mobs = 0.05
        Vobs = 0.1  # Adjust values that might lead to complex sqrt
        
        # Expect a ValueError to be raised due to negative discriminant
        with self.assertRaises(ValueError):
            inverse_EZ(Robs=Robs, Mobs=Mobs, Vobs=Vobs)

    # Test for valid inputs in forward_EZ function
    """def test_forward(self):
        v = 0.3  # Example of drift rate
        a = 0.5  # Example of boundary separation
        t = 0.2  # Example of non-decision time
        
        # Expected output (replace with actual expected value)
        expected = (0.3,0.5,0.2)  # Replace with actual expected result for forward_EZ

        # Call forward_EZ function
        result = forward_EZ(v=v, a=a, t=t)
        
        # Assert that the result matches the expected value (with a tolerance)
        self.assertAlmostEqual(result, expected, places=5)"""
if __name__ == '__main__':
    unittest.main()
