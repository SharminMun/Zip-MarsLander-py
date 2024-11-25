class DescentEvent:
    def __init__(self, t, sp, f, h, st):
        self.seconds = t * 10
        self.velocity = sp
        self.fuel = f
        self.altitude = h
        self.status = st
        
    def get_velocity(self):
        return self.velocity
    
    def get_fuel(self):
        return self.fuel
    
    def get_altitude(self):
        return self.altitude

    def get_status(self):
        return self.status

    def __str__(self):
        return f"{self.seconds}\t\t{self.velocity}\t\t{self.fuel}\t\t{self.altitude}"
    
    def calculate_altitude_change(delta_v, g=9.81):
        """
        Calculate the change in altitude based on change in velocity.

    Parameters:
    - delta_v (float): Change in velocity (in meters per second)
    - g (float): Gravitational acceleration (in meters per second squared), default is 9.81 m/s²

    Returns:
    - delta_h (float): Change in altitude (in meters)
    """
    # Calculate the change in altitude
        delta_h = delta_v / g
        return delta_h
    delta_v = float(input("Enter the change in velocity (m/s): "))  # in meters per second
    altitude_change = calculate_altitude_change(delta_v)

    print(f"The change in altitude is: {altitude_change:.2f} meters")

