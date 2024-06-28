import math
import sys

def calculate_pipe_specs(L: float, H: float, q: float) -> float:
    """
    Thomas Box Formula
    d = pow(((q**2 * 25 * L * 10**5) / H), 0.2)
    """
    return math.pow(((q**2 * 25 * L * 10**5)/H), 0.2)

def calculate_head_loss(f: float, L: float, v: float, d: float):
    g = 9.81
    """
    D'arcy-weber head loss formula

    Description
    ------------
    Head loss is attributed to:
    + Pipe diameter and length
    + Nature of flow (turbulent or lamina flow)
    + viscosity and temperature of the fluid (fluid state)
    + Flow rate

    Formula
    --------
    h = (4 * f * L * v**2)/(2 * g * d)
    """
    return (4 * f * L * v**2)/(2*g*d)

def calculate_reynolds(rho: float, v: float, d: float, mu: float ):
    """
    Description
    ------------
    Reynolds number is dimensionless quantity attributed to the turbulent or lamina nature of fluid flow, i.e greater than 2000 is turbulent and less than 2000 is lamina.

    Formula
    ------------
    R = (rho * v * d)/mu
    """
    return (rho * v * d)/mu
    

if __name__ == "__main__":
    params = {"Length": None,  "Head": None, "F_Rate": None}
    if str(sys.stdin.readline) == "sizing":
        for key in params:
            print(f"enter {key}")
            params[key] = float(sys.stdin.readline())
        print(calculate_pipe_specs(params["Length"], params["Head"], params["F_Rate"]))
    
    elif str(sys.stdin.readline) == "loss":
        params = {"frictional coefficient", "length", "velocity", "diameter"}
        for key in params:
            print(f"enter {key}")
            params[key] = float(sys.stdin.readline())
        print(calculate_head_loss(params["fricitional coefficient"], params["length"], params["velocity"], params["diameter"]))

    else:
        params = {"density", "velocity", "diameter", "viscosity"}
        for key in params:
            print(f"enter {key}")
            params[key] = float(sys.stdin.readline())
        print(calculate_reynolds(params["density"], params["velocity"], params["diameter"], params["viscosity"]))
