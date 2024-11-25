from DescentEvent import DescentEvent

class Vehicle:
    gravity = 100

    # Various end-of-game messages and status result codes.
    dead = "\nCRASH!!\n\tThere were no survivors.\n\n";
    DEAD = -3;
    crashed = "\nThe Starship crashed. Good luck getting back home. Elon is pissed.\n\n";
    CRASHED = -2;
    emptyfuel = "\nThere is no fuel left. You're floating around like Major Tom.\n\n";
    EMPTYFUEL = -1;
    success = "\nYou made it! Good job!\n\n";
    SUCCESS = 0;
    FLYING = 1;
    
    

    def __init__(self, initial_altitude):
        # initialize the altitude AND previous altitude to initialAltitude
        #self.altitude = 8000
        #self.prev_altitude = 8000
        self.altitude = initial_altitude 
        self.prev_altitude = initial_altitude 

        self.velocity= 1000
        self.fuel = 12000
        self.burn = 0
        self.flying = Vehicle.FLYING

    def check_final_status(self):
        s = ""
        if self.altitude <= 0:
            if self.velocity > 10:
                s = self.dead
                self.flying = self.DEAD
            elif 3 < self.velocity <= 10:
                s = self.crashed
                self.flying = self.CRASHED
            elif self.velocity <= 3:
                s = self.success
                self.flying = self.SUCCESS
        else:
            if self.altitude > 0:
                s = self.emptyfuel
                self.flying = self.EMPTYFUEL
        return s


    def compute_deltaV(self):
       return self.velocity + Vehicle.gravity - self.burn


    def adjust_for_burn(self, burnAmount):
        if self.fuel >= burnAmount:
            # Subtract fuel based on the burn amount
            self.fuel = self.fuel - burnAmount
        else:
            burnAmount = self.fuel  # Use all remaining fuel if not enough

        # Set burn to burnAmount requested
        self.burn = burnAmount

        # Save the previous altitude
        self.prev_altitude = self.altitude
    
        # Calculate new velocity based on burn and gravity
        self.velocity = self.compute_deltaV()

        # Adjust altitude based on the change in velocity (assuming a simple model)
        self.altitude = self.altitude - self.velocity
    
    def still_flying(self):

        return self.altitude > 0
    
    def out_of_fuel(self):

        return self.fuel <= 0
     
    def get_status(self, tick):
        return DescentEvent(tick, self.velocity, self.fuel, self.altitude, self.flying)
    
    