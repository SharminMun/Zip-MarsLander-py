class OnBoardComputer:
    def __init__(self):
        pass
    def get_next_burn(self, status):
       ###return burn
       # Here we implement a simple strategy for landing safely.
       # The burn recommendation will depend on current altitude and velocity.
    
        if status.altitude > 1000 and status.velocity > 100:
            return 200  # High burn to slow down rapidly
        elif status.altitude > 500 and status.velocity > 50:
            return 150  # Moderate burn to decelerate
        elif status.altitude > 200 and status.velocity > 20:
            return 100  # Reduce descent rate to 100 m/s
        elif status.altitude > 50 and status.velocity > 10:
            return 50  # Final burns to slow down more
        elif status.altitude <= 10:
            return 10  # Minimal burn near the surface
        return 0  # No burn if we're already descending slowly enough
    
    